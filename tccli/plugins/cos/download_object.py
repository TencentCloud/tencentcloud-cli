# -*- coding: utf-8 -*-
"""
download 操作：从 COS 下载文件到本地
对齐 coscli cp (COS->本地) 命令
- thread_num: 单文件分块下载并发线程数（传给 SDK 的 MAXThread）
- routines: 文件间并发数（同时下载的文件数）
"""
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters, TransferProgressMonitor


def download_object(args, parsed_globals):
    """从 COS 下载文件到本地"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    local_path = args["local_path"]
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    thread_num = args.get("thread_num", 5) or 5
    routines = args.get("routines", 3) or 3
    part_size = args.get("part_size", 20) or 20
    rate_limiting = args.get("rate_limiting", 0) or 0
    version_id = args.get("version_id", "") or ""
    log_file = args.get("log_file", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)

    try:
        if recursive:
            _download_directory(client, bucket, cos_key, local_path, include, exclude,
                                thread_num, routines, part_size, rate_limiting, version_id, log_file, retry)
        else:
            # 确保本地目录存在
            local_dir = os.path.dirname(local_path)
            if local_dir and not os.path.exists(local_dir):
                os.makedirs(local_dir)

            _download_single(client, bucket, cos_key, local_path,
                             thread_num, part_size, rate_limiting, version_id, log_file, retry)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))


def _build_download_kwargs(bucket, cos_key, local_path, thread_num, part_size, rate_limiting, version_id):
    """构造 download_file 的参数"""
    kwargs = {
        "Bucket": bucket,
        "Key": cos_key,
        "DestFilePath": local_path,
        "PartSize": part_size,
        "MAXThread": thread_num,
    }
    if rate_limiting:
        kwargs["TrafficLimit"] = str(int(rate_limiting) * 1024 * 1024 * 8)
    if version_id:
        kwargs["VersionId"] = version_id
    return kwargs


def _download_single(client, bucket, cos_key, local_path,
                     thread_num, part_size, rate_limiting, version_id, log_file="", retry=3):
    """下载单个文件（带进度监控）"""
    monitor = TransferProgressMonitor("download")

    # 先获取文件大小
    try:
        head_resp = client.head_object(Bucket=bucket, Key=cos_key)
        file_size = int(head_resp.get("Content-Length", 0))
    except Exception:
        file_size = 0

    monitor.set_scan_info(1, file_size)
    monitor.start()

    progress_cb, file_id = monitor.create_progress_callback(file_size)
    last_err = None
    for attempt in range(max(1, retry + 1)):
        try:
            kwargs = _build_download_kwargs(bucket, cos_key, local_path,
                                            thread_num, part_size, rate_limiting, version_id)
            kwargs["progress_callback"] = progress_cb
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
                           dest_path=local_path,
                           reason=err_reason,
                           request_id=last_err.get_request_id())
    monitor.stop(log_file=log_file)
    if last_err is not None:
        raise last_err


def _download_directory(client, bucket, prefix, local_dir, include, exclude,
                        thread_num, routines, part_size, rate_limiting, version_id, log_file="", retry=3):
    """递归下载 COS 前缀下的所有对象
    - thread_num: 单文件分块并发（传给 SDK MAXThread）
    - routines: 文件间并发（同时下载的文件数）
    """
    monitor = TransferProgressMonitor("download")
    monitor.start()

    # 先收集所有待下载的文件任务
    tasks = []
    empty_local_dirs = []  # COS 上 / 结尾的空目录对象，需在本地创建对应目录
    total_size = 0
    skip_count = 0
    marker = ""

    while True:
        response = client.list_objects(
            Bucket=bucket,
            Prefix=prefix,
            Marker=marker,
            MaxKeys=1000,
        )

        if "Contents" in response:
            for content in response["Contents"]:
                key = content["Key"]
                rel_key = key[len(prefix):].lstrip("/") if prefix else key

                # 处理 COS 上的空目录对象（以 / 结尾，Size=0）
                if key.endswith("/") and int(content.get("Size", 0)) == 0:
                    if rel_key:
                        # include/exclude 过滤目录
                        dir_rel = rel_key.rstrip("/")
                        if not match_filters(dir_rel, include, exclude):
                            skip_count += 1
                            continue
                        local_subdir = os.path.join(local_dir, dir_rel.replace("/", os.sep))
                        empty_local_dirs.append(local_subdir)
                    continue

                # include/exclude 过滤
                if not match_filters(rel_key, include, exclude):
                    skip_count += 1
                    continue

                file_size = int(content.get("Size", 0))
                local_file = os.path.join(local_dir, rel_key.replace("/", os.sep))
                total_size += file_size
                tasks.append((key, local_file, file_size))

        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break

    # 设置扫描结果（文件数 + 空目录数 + 跳过数）
    monitor.set_scan_info(len(tasks) + len(empty_local_dirs) + skip_count, total_size)
    for _ in range(skip_count):
        monitor.update_skip(0)

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

    def _do_download(key, local_file, file_size):
        """单个文件下载任务（含重试）"""
        last_err = None
        progress_cb, file_id = monitor.create_progress_callback(file_size)
        for attempt in range(max(1, retry + 1)):
            try:
                _ensure_dir(local_file)
                kwargs = _build_download_kwargs(bucket, key, local_file,
                                                thread_num, part_size, rate_limiting, version_id)
                kwargs["progress_callback"] = progress_cb
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
                               src_path="cos://%s/%s" % (bucket, key),
                               dest_path=local_file,
                               reason=err_reason,
                               request_id=last_err.get_request_id())

    # 使用线程池并发下载多个文件，routines 控制文件间并发
    if tasks:
        max_workers = min(routines, len(tasks))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for key, local_file, file_size in tasks:
                futures.append(executor.submit(_do_download, key, local_file, file_size))
            for future in as_completed(futures):
                future.result()

    # 在本地创建 COS 上的空目录
    for local_subdir in empty_local_dirs:
        if local_subdir and not os.path.exists(local_subdir):
            os.makedirs(local_subdir, exist_ok=True)
        monitor.update_ok(0)

    monitor.stop(log_file=log_file)