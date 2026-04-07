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
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)
    log_file = args.get("log_file", "") or ""

    # 解析自定义元数据
    metadata = parse_meta(meta)

    try:
        if recursive and os.path.isdir(local_path):
            # 对齐 coscli cp 行为：
            # - local_path 以 / 结尾（如 /tmp/dir/）：不保留目录名，直接映射内容
            # - local_path 不以 / 结尾（如 /tmp/dir）：保留目录名，映射为 cos_key/dir/
            if not local_path.endswith(os.sep) and not local_path.endswith("/"):
                dir_name = os.path.basename(local_path.rstrip(os.sep))
                if cos_key:
                    cos_key = cos_key.rstrip("/") + "/" + dir_name + "/"
                else:
                    cos_key = dir_name + "/"
            _upload_directory(client, bucket, local_path, cos_key, include, exclude,
                              storage_class, content_type, metadata, thread_num, routines,
                              part_size, rate_limiting, retry, log_file)
        else:
            if not os.path.exists(local_path):
                print("Error: 本地文件不存在: %s" % local_path)
                return
            if not os.path.isfile(local_path):
                print("Error: 指定路径不是文件: %s（如需上传目录请使用 --recursive true）" % local_path)
                return

            _upload_single(client, bucket, local_path, cos_key,
                           storage_class, content_type, metadata, thread_num, part_size, rate_limiting, retry, log_file)

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
                   storage_class, content_type, metadata, thread_num, part_size, rate_limiting, retry=3, log_file=""):
    """上传单个文件（带进度监控）"""
    monitor = TransferProgressMonitor("upload")
    file_size = os.path.getsize(local_path)
    monitor.set_scan_info(1, file_size)
    monitor.start()

    progress_cb, file_id = monitor.create_progress_callback(file_size)
    last_err = None
    for attempt in range(max(1, retry + 1)):
        try:
            kwargs = _build_upload_kwargs(bucket, local_path, cos_key, storage_class, content_type,
                                          metadata, thread_num, part_size, rate_limiting)
            kwargs["progress_callback"] = progress_cb
            client.upload_file(**kwargs)
            monitor.update_ok(file_size, file_id)
            last_err = None
            break
        except CosServiceError as e:
            last_err = e
            if attempt < retry:
                # 重置该文件的进度，准备重试
                progress_cb, file_id = monitor.create_progress_callback(file_size)
    if last_err is not None:
        err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
        monitor.update_err(file_id,
                           src_path=local_path,
                           dest_path="cos://%s/%s" % (bucket, cos_key),
                           reason=err_reason,
                           request_id=last_err.get_request_id())
    monitor.stop(log_file=log_file)
    if last_err is not None:
        raise last_err


def _upload_directory(client, bucket, local_dir, cos_prefix, include, exclude,
                      storage_class, content_type, metadata, thread_num, routines,
                      part_size, rate_limiting, retry=3, log_file=""):
    """递归上传目录
    - thread_num: 单文件分块并发（传给 SDK MAXThread）
    - routines: 文件间并发（同时上传的文件数）
    """
    monitor = TransferProgressMonitor("upload")
    monitor.start()

    # 先收集所有待上传的文件任务，同时统计总大小
    tasks = []
    empty_dir_keys = []  # 空目录对应的 COS key（以 / 结尾的空对象）
    total_size = 0
    skip_count = 0
    for root, dirs, files in os.walk(local_dir):
        # 检测空目录：当前目录下没有文件，且没有子目录（或子目录也都是空的）
        # 简单判断：当前 root 下既无文件也无子目录，则为空目录
        if not files and not dirs:
            rel_dir = os.path.relpath(root, local_dir).replace(os.sep, "/")
            if rel_dir == ".":
                # 根目录本身为空
                dir_key = cos_prefix.rstrip("/") + "/" if cos_prefix else ""
            else:
                # include/exclude 过滤目录
                if not match_filters(rel_dir, include, exclude):
                    skip_count += 1
                    continue
                if cos_prefix:
                    if cos_prefix.endswith("/"):
                        dir_key = cos_prefix + rel_dir + "/"
                    else:
                        dir_key = cos_prefix + "/" + rel_dir + "/"
                else:
                    dir_key = rel_dir + "/"
            if dir_key:
                empty_dir_keys.append(dir_key)

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

    # 设置扫描结果（文件数 + 空目录数 + 跳过数）
    monitor.set_scan_info(len(tasks) + len(empty_dir_keys) + skip_count, total_size)
    for _ in range(skip_count):
        monitor.update_skip(0)

    def _do_upload(full_path, key, file_size):
        """单个文件上传任务（含重试）"""
        last_err = None
        progress_cb, file_id = monitor.create_progress_callback(file_size)
        for attempt in range(max(1, retry + 1)):
            try:
                kwargs = _build_upload_kwargs(bucket, full_path, key, storage_class, content_type,
                                              metadata, thread_num, part_size, rate_limiting)
                kwargs["progress_callback"] = progress_cb
                client.upload_file(**kwargs)
                monitor.update_ok(file_size, file_id)
                last_err = None
                break
            except CosServiceError as e:
                last_err = e
                if attempt < retry:
                    # 重置该文件的进度，准备重试
                    progress_cb, file_id = monitor.create_progress_callback(file_size)
        if last_err is not None:
            err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
            monitor.update_err(file_id,
                               src_path=full_path,
                               dest_path="cos://%s/%s" % (bucket, key),
                               reason=err_reason,
                               request_id=last_err.get_request_id())

    # 使用线程池并发上传多个文件，routines 控制文件间并发
    if tasks:
        max_workers = min(routines, len(tasks))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for full_path, key, file_size in tasks:
                futures.append(executor.submit(_do_upload, full_path, key, file_size))
            for future in as_completed(futures):
                future.result()

    # 在 COS 上创建空目录标记（以 / 结尾的空对象）
    for dir_key in empty_dir_keys:
        try:
            client.put_object(Bucket=bucket, Key=dir_key, Body=b"")
            monitor.update_ok(0)
        except CosServiceError as e:
            monitor.update_err(src_path=dir_key,
                               reason="创建空目录失败: %s (Code: %s)" % (e.get_error_msg(), e.get_error_code()),
                               request_id=e.get_request_id())

    monitor.stop(log_file=log_file)