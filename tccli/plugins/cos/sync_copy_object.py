# -*- coding: utf-8 -*-
"""
sync_copy 操作：COS -> COS 同步复制
对齐 coscli sync (COS->COS) 命令
- routines: 文件间并发数（同时复制的文件数）
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import (init_cos_client, match_filters, build_cos_key, parse_meta,
                    list_all_objects, list_all_objects_with_dirs, TransferProgressMonitor)


def sync_copy_object(args, parsed_globals):
    """同步复制：COS -> COS"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_prefix = args.get("cos_key", "") or ""
    dest_bucket = args.get("dest_bucket", bucket) or bucket
    dest_prefix = args.get("dest_key", "") or ""
    dest_region = args.get("dest_region", region) or region
    recursive = args.get("recursive", False)
    delete_extra = args.get("delete_extra", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""
    storage_class = args.get("storage_class", "") or ""
    meta = args.get("meta", "") or ""
    routines = args.get("routines", 3) or 3
    log_file = args.get("log_file", "") or ""
    retry = args.get("retry", 3)
    if retry is None:
        retry = 3
    retry = int(retry)

    # 解析自定义元数据
    metadata = parse_meta(meta)

    try:
        src_objects = list_all_objects_with_dirs(client, bucket, cos_prefix)
        dest_objects = list_all_objects(client, dest_bucket, dest_prefix)

        monitor = TransferProgressMonitor("copy")
        monitor.start()

        # 收集待复制的文件任务
        tasks = []
        empty_dir_keys = []  # COS 上 / 结尾的空目录对象，需在目标 COS 上同步创建
        total_size = 0
        skip_count = 0
        skip_size = 0
        for src_key, obj_info in src_objects.items():
            rel_key = src_key[len(cos_prefix):].lstrip("/") if cos_prefix else src_key

            # 处理 / 结尾的空目录对象，在目标 COS 上同步创建
            if obj_info.get("IsDir"):
                if rel_key:
                    # include/exclude 过滤目录
                    dir_rel = rel_key.rstrip("/")
                    if not match_filters(dir_rel, include, exclude):
                        skip_count += 1
                        continue
                    d_key = build_cos_key(dest_prefix, rel_key)
                    if not d_key.endswith("/"):
                        d_key += "/"
                    if d_key not in dest_objects:
                        empty_dir_keys.append(d_key)
                continue

            # include/exclude 过滤
            if not match_filters(rel_key, include, exclude):
                skip_count += 1
                continue

            dest_key = build_cos_key(dest_prefix, rel_key)

            # 检查目标是否已存在且大小一致（增量同步）
            if dest_key in dest_objects and dest_objects[dest_key]["Size"] == obj_info["Size"]:
                skip_count += 1
                skip_size += obj_info["Size"]
                continue

            total_size += obj_info["Size"]
            tasks.append((src_key, dest_key, obj_info["Size"]))

        # 设置扫描结果（文件数 + 空目录数 + 跳过数）
        monitor.set_scan_info(len(tasks) + len(empty_dir_keys) + skip_count, total_size + skip_size)
        for i in range(skip_count):
            monitor.update_skip(skip_size // skip_count if skip_count > 0 else 0)

        def _do_copy(src_key, dest_key, file_size):
            """单个文件复制任务（含重试）"""
            last_err = None
            for attempt in range(max(1, retry + 1)):
                try:
                    source = {
                        "Bucket": bucket,
                        "Key": src_key,
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
                monitor.update_err(src_path="cos://%s/%s" % (bucket, src_key),
                                   dest_path="cos://%s/%s" % (dest_bucket, dest_key),
                                   reason=err_reason,
                                   request_id=last_err.get_request_id())

        # 使用线程池并发复制多个文件，routines 控制文件间并发
        if tasks:
            max_workers = min(routines, len(tasks))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for src_key, dest_key, file_size in tasks:
                    futures.append(executor.submit(_do_copy, src_key, dest_key, file_size))
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

        # 删除目标多余的文件和文件夹
        deleted = 0
        if delete_extra:
            # 重新获取目标端包含目录对象的完整列表
            dest_all_objects = list_all_objects_with_dirs(client, dest_bucket, dest_prefix)
            for dest_key, obj_info in dest_all_objects.items():
                rel_key = dest_key[len(dest_prefix):].lstrip("/") if dest_prefix else dest_key
                src_key = build_cos_key(cos_prefix, rel_key)
                if obj_info.get("IsDir"):
                    # 目录对象：检查源端是否存在对应目录对象
                    src_dir_key = src_key if src_key.endswith("/") else src_key + "/"
                    if src_dir_key not in src_objects:
                        client.delete_object(Bucket=dest_bucket, Key=dest_key)
                        deleted += 1
                else:
                    if src_key not in src_objects:
                        client.delete_object(Bucket=dest_bucket, Key=dest_key)
                        deleted += 1

        monitor.stop(log_file=log_file)

        if deleted > 0:
            print("已删除目标端多余文件: %d" % deleted)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
