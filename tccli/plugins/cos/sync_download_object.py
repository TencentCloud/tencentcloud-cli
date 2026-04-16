# -*- coding: utf-8 -*-
"""
sync_download 操作：COS -> 本地同步下载
对齐 coscli sync (COS->本地) 命令
- thread_num: 单文件分块下载并发线程数（传给 SDK 的 MAXThread）
- routines: 文件间并发数（同时下载的文件数）
"""
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import (init_cos_client, match_filters, build_cos_key,
                    list_all_objects, list_all_objects_with_dirs, list_local_files, TransferProgressMonitor)


def sync_download_object(args, parsed_globals):
    """同步下载：COS -> 本地目录"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_prefix = args.get("cos_key", "") or ""
    recursive = args.get("recursive", False)
    delete_extra = args.get("delete_extra", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    thread_num = args.get("thread_num", 5) or 5
    routines = args.get("routines", 3) or 3
    part_size = args.get("part_size", 20) or 20
    rate_limiting = args.get("rate_limiting", 0) or 0
    log_file = args.get("log_file", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)

    if not os.path.exists(local_path):
        os.makedirs(local_path)

    try:
        cos_objects = list_all_objects_with_dirs(client, bucket, cos_prefix)
        local_files = list_local_files(local_path)

        monitor = TransferProgressMonitor("download")
        monitor.start()

        # 收集待下载的文件任务，同时识别 COS 上的空目录对象
        tasks = []
        empty_dirs = []  # COS 上以 / 结尾的空目录对象，需在本地创建对应目录
        total_size = 0
        skip_count = 0
        skip_size = 0
        for cos_key, obj_info in cos_objects.items():
            rel_key = cos_key[len(cos_prefix):].lstrip("/") if cos_prefix else cos_key

            # 处理 COS 上的空目录对象（以 / 结尾）
            if obj_info.get("IsDir"):
                if rel_key:
                    # include/exclude 过滤目录
                    dir_rel = rel_key.rstrip("/")
                    if not match_filters(dir_rel, include, exclude):
                        skip_count += 1
                        continue
                    local_dir = os.path.join(local_path, dir_rel.replace("/", os.sep))
                    if local_dir and not os.path.exists(local_dir):
                        empty_dirs.append(local_dir)
                continue

            # include/exclude 过滤
            if not match_filters(rel_key, include, exclude):
                skip_count += 1
                continue

            local_file = os.path.join(local_path, rel_key.replace("/", os.sep))

            # 检查本地是否已存在且大小一致（增量同步）
            if rel_key in local_files and local_files[rel_key]["Size"] == obj_info["Size"]:
                skip_count += 1
                skip_size += obj_info["Size"]
                continue

            total_size += obj_info["Size"]
            tasks.append((cos_key, local_file, obj_info["Size"]))

        # 设置扫描结果（文件数 + 空目录数 + 跳过数）
        monitor.set_scan_info(len(tasks) + len(empty_dirs) + skip_count, total_size + skip_size)
        for i in range(skip_count):
            monitor.update_skip(skip_size // skip_count if skip_count > 0 else 0)

        # 预先创建所有需要的本地目录（避免并发时目录创建冲突）
        dir_lock = threading.Lock()
        created_dirs = set()

        def _ensure_dir(file_path):
            """线程安全地创建目录"""
            file_dir = os.path.dirname(file_path)
            if file_dir and file_dir not in created_dirs:
                with dir_lock:
                    if file_dir not in created_dirs:
                        if not os.path.exists(file_dir):
                            os.makedirs(file_dir)
                        created_dirs.add(file_dir)

        def _do_download(cos_key, local_file, file_size):
            """单个文件下载任务（含重试）"""
            last_err = None
            progress_cb, file_id = monitor.create_progress_callback(file_size)
            for attempt in range(max(1, retry + 1)):
                try:
                    _ensure_dir(local_file)
                    kwargs = {
                        "Bucket": bucket,
                        "Key": cos_key,
                        "DestFilePath": local_file,
                        "PartSize": part_size,
                        "MAXThread": thread_num,
                        "progress_callback": progress_cb,
                    }
                    if rate_limiting:
                        kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)

                    client.download_file(**kwargs)
                    monitor.update_ok(file_size, file_id)
                    last_err = None
                    break
                except CosServiceError as e:
                    last_err = e
                    if attempt < retry:
                        progress_cb, file_id = monitor.create_progress_callback(file_size)
            if last_err is not None:
                err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
                monitor.update_err(file_id,
                                   src_path="cos://%s/%s" % (bucket, cos_key),
                                   dest_path=local_file,
                                   reason=err_reason,
                                   request_id=last_err.get_request_id())

        # 使用线程池并发下载多个文件，routines 控制文件间并发
        if tasks:
            max_workers = min(routines, len(tasks))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for cos_key, local_file, file_size in tasks:
                    futures.append(executor.submit(_do_download, cos_key, local_file, file_size))
                for future in as_completed(futures):
                    future.result()

        # 在本地创建 COS 上的空目录
        for local_dir in empty_dirs:
            os.makedirs(local_dir, exist_ok=True)
            monitor.update_ok(0)

        # 删除本地多余的文件和空目录
        deleted = 0
        if delete_extra:
            # 第一步：删除多余的文件
            for rel_path, file_info in local_files.items():
                cos_key = build_cos_key(cos_prefix, rel_path)
                if cos_key not in cos_objects:
                    os.remove(file_info["FullPath"])
                    deleted += 1
            # 第二步：删除多余的本地目录（从最深层开始，文件删除后目录可能已变空）
            for root, dirs, files in os.walk(local_path, topdown=False):
                if root == local_path:
                    continue
                rel_dir = os.path.relpath(root, local_path).replace(os.sep, "/")
                cos_dir_key = build_cos_key(cos_prefix, rel_dir) + "/"
                # 目录在 COS 上不存在（既无目录对象也无该前缀下的文件）
                dir_exists_in_cos = (cos_dir_key in cos_objects or
                                     any(k.startswith(cos_dir_key) for k in cos_objects))
                if not dir_exists_in_cos:
                    # 文件已在第一步删除，此时目录若为空则删除
                    if not os.listdir(root):
                        os.rmdir(root)
                        deleted += 1

        monitor.stop(log_file=log_file)

        if deleted > 0:
            print("已删除本地多余文件: %d" % deleted)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
