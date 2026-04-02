# -*- coding: utf-8 -*-
"""
upload 操作：上传本地文件到 COS
对齐 coscli cp (本地->COS) 命令
- thread_num: 单文件分块上传并发线程数（传给 SDK 的 MAXThread）
- routines: 文件间并发数（同时上传的文件数）
"""
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters, parse_meta, TransferProgressMonitor


def upload_object(args, parsed_globals):
    """上传本地文件到 COS"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    local_path = args["local_path"]
    cos_key = args["cos_key"]
    storage_class = args.get("storage_class", "") or ""
    content_type = args.get("content_type", "") or ""
    meta = args.get("meta", "") or ""
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    thread_num = args.get("thread_num", 5) or 5
    routines = args.get("routines", 3) or 3
    part_size = args.get("part_size", 20) or 20
    rate_limiting = args.get("rate_limiting", 0) or 0

    # 解析自定义元数据
    metadata = parse_meta(meta)

    try:
        if recursive and os.path.isdir(local_path):
            _upload_directory(client, bucket, local_path, cos_key, include, exclude,
                              storage_class, content_type, metadata, thread_num, routines,
                              part_size, rate_limiting)
        else:
            if not os.path.exists(local_path):
                print("Error: 本地文件不存在: %s" % local_path)
                return
            if not os.path.isfile(local_path):
                print("Error: 指定路径不是文件: %s（如需上传目录请使用 --recursive true）" % local_path)
                return

            _upload_single(client, bucket, local_path, cos_key,
                           storage_class, content_type, metadata, thread_num, part_size, rate_limiting)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))


def _build_upload_kwargs(bucket, local_path, cos_key, storage_class, content_type,
                         metadata, thread_num, part_size, rate_limiting):
    """构造 upload_file 的参数"""
    kwargs = {
        "Bucket": bucket,
        "LocalFilePath": local_path,
        "Key": cos_key,
        "PartSize": part_size,
        "MAXThread": thread_num,
    }
    if storage_class:
        kwargs["StorageClass"] = storage_class
    if content_type:
        kwargs["ContentType"] = content_type
    if metadata:
        kwargs["Metadata"] = metadata
    if rate_limiting:
        kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)
    return kwargs


def _upload_single(client, bucket, local_path, cos_key,
                   storage_class, content_type, metadata, thread_num, part_size, rate_limiting):
    """上传单个文件（带进度监控）"""
    monitor = TransferProgressMonitor("upload")
    file_size = os.path.getsize(local_path)
    monitor.set_scan_info(1, file_size)
    monitor.start()

    progress_cb, file_id = monitor.create_progress_callback(file_size)
    try:
        kwargs = _build_upload_kwargs(bucket, local_path, cos_key, storage_class, content_type,
                                      metadata, thread_num, part_size, rate_limiting)
        kwargs["progress_callback"] = progress_cb
        client.upload_file(**kwargs)
        monitor.update_ok(file_size, file_id)
    except CosServiceError:
        monitor.update_err(file_id)
        raise
    finally:
        monitor.stop()


def _upload_directory(client, bucket, local_dir, cos_prefix, include, exclude,
                      storage_class, content_type, metadata, thread_num, routines,
                      part_size, rate_limiting):
    """递归上传目录
    - thread_num: 单文件分块并发（传给 SDK MAXThread）
    - routines: 文件间并发（同时上传的文件数）
    """
    monitor = TransferProgressMonitor("upload")
    monitor.start()

    # 先收集所有待上传的文件任务，同时统计总大小
    tasks = []
    total_size = 0
    skip_count = 0
    for root, dirs, files in os.walk(local_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, local_dir).replace(os.sep, "/")

            # include/exclude 过滤
            if not match_filters(rel_path, include, exclude):
                skip_count += 1
                continue

            # 构造 COS key
            if cos_prefix:
                if cos_prefix.endswith("/"):
                    key = cos_prefix + rel_path
                else:
                    key = cos_prefix + "/" + rel_path
            else:
                key = rel_path

            file_size = os.path.getsize(full_path)
            total_size += file_size
            tasks.append((full_path, key, file_size))

    # 设置扫描结果
    monitor.set_scan_info(len(tasks) + skip_count, total_size)
    for _ in range(skip_count):
        monitor.update_skip(0)

    def _do_upload(full_path, key, file_size):
        """单个文件上传任务"""
        progress_cb, file_id = monitor.create_progress_callback(file_size)
        try:
            kwargs = _build_upload_kwargs(bucket, full_path, key, storage_class, content_type,
                                          metadata, thread_num, part_size, rate_limiting)
            kwargs["progress_callback"] = progress_cb
            client.upload_file(**kwargs)
            monitor.update_ok(file_size, file_id)
        except CosServiceError as e:
            monitor.update_err(file_id)

    # 使用线程池并发上传多个文件，routines 控制文件间并发
    if tasks:
        max_workers = min(routines, len(tasks))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for full_path, key, file_size in tasks:
                futures.append(executor.submit(_do_upload, full_path, key, file_size))
            for future in as_completed(futures):
                future.result()

    monitor.stop()