# -*- coding: utf-8 -*-
"""
copy 操作：复制 COS 上的文件
对齐 coscli cp (COS->COS) 命令
- routines: 文件间并发数（同时复制的文件数）
"""
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import init_cos_client, match_filters, parse_meta, build_cos_key, TransferProgressMonitor


def copy_object(args, parsed_globals):
    """复制 COS 上的文件"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    dest_bucket = args.get("dest_bucket", bucket) or bucket
    dest_key = args["dest_key"]
    dest_region = args.get("dest_region", region) or region
    storage_class = args.get("storage_class", "") or ""
    meta = args.get("meta", "") or ""
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    routines = args.get("routines", 3) or 3
    log_file = args.get("log_file", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)

    # 解析自定义元数据
    metadata = parse_meta(meta)

    try:
        if recursive:
            _copy_by_prefix(client, bucket, cos_key, dest_bucket, dest_key,
                            region, dest_region, storage_class, metadata, include, exclude, routines, log_file, retry)
        else:
            _copy_single(client, bucket, cos_key, dest_bucket, dest_key,
                         region, storage_class, metadata, log_file, retry)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def _copy_single(client, bucket, cos_key, dest_bucket, dest_key,
                 region, storage_class, metadata, log_file="", retry=3):
    """复制单个文件（带进度监控）"""
    monitor = TransferProgressMonitor("copy")

    # 获取源文件大小
    try:
        head_resp = client.head_object(Bucket=bucket, Key=cos_key)
        file_size = int(head_resp.get("Content-Length", 0))
    except Exception:
        file_size = 0

    monitor.set_scan_info(1, file_size)
    monitor.start()

    last_err = None
    for attempt in range(max(1, retry + 1)):
        try:
            source = {
                "Bucket": bucket,
                "Key": cos_key,
                "Region": region,
            }
            kwargs = {
                "Bucket": dest_bucket,
                "Key": dest_key,
                "CopySource": source,
            }
            if storage_class:
                kwargs["StorageClass"] = storage_class
            if metadata:
                kwargs["Metadata"] = metadata
                kwargs["CopyStatus"] = "Replaced"

            client.copy(**kwargs)
            monitor.update_ok(file_size)
            last_err = None
            break
        except CosServiceError as e:
            last_err = e
    if last_err is not None:
        err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
        monitor.update_err(src_path="cos://%s/%s" % (bucket, cos_key),
                           dest_path="cos://%s/%s" % (dest_bucket, dest_key),
                           reason=err_reason,
                           request_id=last_err.get_request_id())
    monitor.stop(log_file=log_file)
    if last_err is not None:
        raise last_err


def _copy_by_prefix(client, bucket, prefix, dest_bucket, dest_prefix,
                    src_region, dest_region, storage_class, metadata, include, exclude, routines, log_file="", retry=3):
    """递归复制指定前缀下的所有对象
    - routines: 文件间并发（同时复制的文件数）
    """
    monitor = TransferProgressMonitor("copy")
    monitor.start()

    # 先收集所有待复制的文件任务
    tasks = []
    empty_dir_keys = []  # COS 上 / 结尾的空目录对象，需在目标 COS 上同步创建
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
                src_key = content["Key"]
                rel_key = src_key[len(prefix):].lstrip("/") if prefix else src_key

                # 处理 COS 上的空目录对象（以 / 结尾，Size=0），在目标 COS 上同步创建
                if src_key.endswith("/") and int(content.get("Size", 0)) == 0:
                    if rel_key:
                        # include/exclude 过滤目录
                        dir_rel = rel_key.rstrip("/")
                        if not match_filters(dir_rel, include, exclude):
                            skip_count += 1
                            continue
                        d_key = build_cos_key(dest_prefix, rel_key)
                        if not d_key.endswith("/"):
                            d_key += "/"
                        empty_dir_keys.append(d_key)
                    continue

                # include/exclude 过滤
                if not match_filters(rel_key, include, exclude):
                    skip_count += 1
                    continue

                file_size = int(content.get("Size", 0))
                d_key = build_cos_key(dest_prefix, rel_key)
                total_size += file_size
                tasks.append((src_key, d_key, file_size))

        if response.get("IsTruncated") == "true":
            marker = response.get("NextMarker", "")
        else:
            break

    # 设置扫描结果（文件数 + 空目录数 + 跳过数）
    monitor.set_scan_info(len(tasks) + len(empty_dir_keys) + skip_count, total_size)
    for _ in range(skip_count):
        monitor.update_skip(0)

    def _do_copy(src_key, d_key, file_size):
        """单个文件复制任务（含重试）"""
        last_err = None
        for attempt in range(max(1, retry + 1)):
            try:
                source = {
                    "Bucket": bucket,
                    "Key": src_key,
                    "Region": src_region,
                }
                kwargs = {
                    "Bucket": dest_bucket,
                    "Key": d_key,
                    "CopySource": source,
                }
                if storage_class:
                    kwargs["StorageClass"] = storage_class
                if metadata:
                    kwargs["Metadata"] = metadata
                    kwargs["MetadataDirective"] = "Replaced"

                client.copy(**kwargs)
                monitor.update_ok(file_size)
                last_err = None
                break
            except CosServiceError as e:
                last_err = e
        if last_err is not None:
            err_reason = "%s (Code: %s)" % (last_err.get_error_msg(), last_err.get_error_code())
            monitor.update_err(src_path="cos://%s/%s" % (bucket, src_key),
                               dest_path="cos://%s/%s" % (dest_bucket, d_key),
                               reason=err_reason,
                               request_id=last_err.get_request_id())

    # 使用线程池并发复制多个文件，routines 控制文件间并发
    if tasks:
        max_workers = min(routines, len(tasks))
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for src_key, d_key, file_size in tasks:
                futures.append(executor.submit(_do_copy, src_key, d_key, file_size))
            for future in as_completed(futures):
                future.result()

    # 在目标 COS 上创建空目录标记
    for d_key in empty_dir_keys:
        try:
            client.put_object(Bucket=dest_bucket, Key=d_key, Body=b"")
            monitor.update_ok(0)
        except CosServiceError as e:
            monitor.update_err(src_path="cos://%s/%s" % (dest_bucket, d_key),
                               reason="创建空目录失败: %s (Code: %s)" % (e.get_error_msg(), e.get_error_code()),
                               request_id=e.get_request_id())

    monitor.stop(log_file=log_file)