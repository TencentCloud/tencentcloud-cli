# -*- coding: utf-8 -*-
"""
sync_upload 操作：本地 -> COS 同步上传
对齐 coscli sync (本地->COS) 命令
- thread_num: 单文件分块上传并发线程数（传给 SDK 的 MAXThread）
- routines: 文件间并发数（同时上传的文件数）
"""
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import (init_cos_client, match_filters, build_cos_key, parse_meta,
                    list_all_objects, list_local_files, TransferProgressMonitor,
                    should_skip_sync_upload)


def sync_upload_object(args, parsed_globals):
    """同步上传：本地目录 -> COS"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_prefix = args.get("cos_key", "") or ""
    recursive = args.get("recursive", False)
    delete = args.get("delete", False)
    ignore_existing = args.get("ignore_existing", False)
    update = args.get("update", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    storage_class = args.get("storage_class", "") or ""
    content_type = args.get("content_type", "") or ""
    meta = args.get("meta", "") or ""
    thread_num = args.get("thread_num", 5) or 5
    routines = args.get("routines", 3) or 3
    part_size = args.get("part_size", 20) or 20
    rate_limiting = args.get("rate_limiting", 0) or 0
    log_file = args.get("log_file", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)

    # 解析自定义元数据
    metadata = parse_meta(meta)

    if not os.path.isdir(local_path):
        print("Error: 本地路径不是目录: %s" % local_path)
        return

    try:
        local_files = list_local_files(local_path)
        cos_objects = list_all_objects(client, bucket, cos_prefix)

        # 收集本地空目录
        empty_dir_keys = []
        for root, dirs, files in os.walk(local_path):
            if not files and not dirs:
                rel_dir = os.path.relpath(root, local_path).replace(os.sep, "/")
                if rel_dir == ".":
                    dir_key = cos_prefix.rstrip("/") + "/" if cos_prefix else ""
                else:
                    # include/exclude 过滤目录
                    if not match_filters(rel_dir, include, exclude):
                        continue
                    dir_key = build_cos_key(cos_prefix, rel_dir) + "/"
                if dir_key and dir_key not in cos_objects:
                    empty_dir_keys.append(dir_key)

        monitor = TransferProgressMonitor("upload")
        monitor.start()

        # 收集待上传的文件任务
        tasks = []
        total_size = 0
        skip_count = 0
        skip_size = 0
        for rel_path, file_info in local_files.items():
            # include/exclude 过滤
            if not match_filters(rel_path, include, exclude):
                skip_count += 1
                continue

            cos_key = build_cos_key(cos_prefix, rel_path)

            # 增量同步：对齐 coscli sync 跳过逻辑
            # - 默认：对比本地 CRC64 与 COS CRC64（x-cos-hash-crc64ecma）
            # - --ignore-existing：目标存在即跳过
            # - --update：按 Last-Modified 时间比较
            if cos_key in cos_objects and should_skip_sync_upload(
                    client, bucket, cos_key,
                    file_info["FullPath"], file_info.get("MTime", 0),
                    ignore_existing=ignore_existing, update=update):
                skip_count += 1
                skip_size += file_info["Size"]
                continue

            total_size += file_info["Size"]
            tasks.append((file_info, cos_key))

        # 设置扫描结果（文件数 + 空目录数 + 跳过数）
        monitor.set_scan_info(len(tasks) + len(empty_dir_keys) + skip_count, total_size + skip_size)
        for i in range(skip_count):
            monitor.update_skip(skip_size // skip_count if skip_count > 0 else 0)

        def _do_upload(file_info, cos_key):
            """单个文件上传任务（含重试）"""
            last_err = None
            progress_cb, file_id = monitor.create_progress_callback(file_info["Size"])
            for attempt in range(max(1, retry + 1)):
                try:
                    kwargs = {
                        "Bucket": bucket,
                        "LocalFilePath": file_info["FullPath"],
                        "Key": cos_key,
                        "PartSize": part_size,
                        "MAXThread": thread_num,
                        "progress_callback": progress_cb,
                    }
                    if storage_class:
                        kwargs["StorageClass"] = storage_class
                    if content_type:
                        kwargs["ContentType"] = content_type
                    if metadata:
                        kwargs["Metadata"] = metadata
                    if rate_limiting:
                        kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)

                    client.upload_file(**kwargs)
                    monitor.update_ok(file_info["Size"], file_id)
                    last_err = None
                    break
                except CosServiceError as e:
                    last_err = e
                    if attempt < retry:
                        progress_cb, file_id = monitor.create_progress_callback(file_info["Size"])
            if last_err is not None:
                err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
                monitor.update_err(file_id,
                                   src_path=file_info["FullPath"],
                                   dest_path="cos://%s/%s" % (bucket, cos_key),
                                   reason=err_reason,
                                   request_id=last_err.get_request_id())

        # 使用线程池并发上传多个文件，routines 控制文件间并发
        if tasks:
            max_workers = min(routines, len(tasks))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for file_info, cos_key in tasks:
                    futures.append(executor.submit(_do_upload, file_info, cos_key))
                for future in as_completed(futures):
                    future.result()

        # 在 COS 上创建空目录标记
        for dir_key in empty_dir_keys:
            try:
                client.put_object(Bucket=bucket, Key=dir_key, Body=b"")
                monitor.update_ok(0)
            except CosServiceError as e:
                monitor.update_err(src_path=dir_key,
                                   reason="创建空目录失败: %s (Code: %s)" % (e.get_error_msg(), e.get_error_code()),
                                   request_id=e.get_request_id())

        # 删除 COS 上多余的文件和文件夹
        deleted = 0
        if delete:
            # 重新获取包含目录对象的完整列表
            from .utils import list_all_objects_with_dirs
            cos_all_objects = list_all_objects_with_dirs(client, bucket, cos_prefix)
            for cos_key, obj_info in cos_all_objects.items():
                rel_key = cos_key[len(cos_prefix):].lstrip("/") if cos_prefix else cos_key
                if obj_info.get("IsDir"):
                    # 目录对象：检查本地是否存在对应目录
                    dir_rel = rel_key.rstrip("/")
                    if dir_rel and not os.path.isdir(os.path.join(local_path, dir_rel.replace("/", os.sep))):
                        client.delete_object(Bucket=bucket, Key=cos_key)
                        deleted += 1
                else:
                    if rel_key not in local_files:
                        client.delete_object(Bucket=bucket, Key=cos_key)
                        deleted += 1

        monitor.stop(log_file=log_file)

        if deleted > 0:
            print("已删除 COS 上多余文件: %d" % deleted)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
