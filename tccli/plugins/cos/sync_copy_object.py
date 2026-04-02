# -*- coding: utf-8 -*-
"""
sync_copy 操作：COS -> COS 同步复制
对齐 coscli sync (COS->COS) 命令
- routines: 文件间并发数（同时复制的文件数）
"""
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from qcloud_cos import CosServiceError
from .utils import (init_cos_client, match_filters, build_cos_key, parse_meta,
                    list_all_objects, TransferProgressMonitor)


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

    # 解析自定义元数据
    metadata = parse_meta(meta)

    try:
        src_objects = list_all_objects(client, bucket, cos_prefix)
        dest_objects = list_all_objects(client, dest_bucket, dest_prefix)

        monitor = TransferProgressMonitor("copy")
        monitor.start()

        # 收集待复制的文件任务
        tasks = []
        total_size = 0
        skip_count = 0
        skip_size = 0
        for src_key, obj_info in src_objects.items():
            rel_key = src_key[len(cos_prefix):].lstrip("/") if cos_prefix else src_key

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

        # 设置扫描结果
        monitor.set_scan_info(len(tasks) + skip_count, total_size + skip_size)
        for i in range(skip_count):
            monitor.update_skip(skip_size // skip_count if skip_count > 0 else 0)

        def _do_copy(src_key, dest_key, file_size):
            """单个文件复制任务"""
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
            except CosServiceError as e:
                monitor.update_err()

        # 使用线程池并发复制多个文件，routines 控制文件间并发
        if tasks:
            max_workers = min(routines, len(tasks))
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for src_key, dest_key, file_size in tasks:
                    futures.append(executor.submit(_do_copy, src_key, dest_key, file_size))
                for future in as_completed(futures):
                    future.result()

        # 删除目标多余的文件
        deleted = 0
        if delete_extra:
            for dest_key in dest_objects:
                rel_key = dest_key[len(dest_prefix):].lstrip("/") if dest_prefix else dest_key
                src_key = build_cos_key(cos_prefix, rel_key)
                if src_key not in src_objects:
                    client.delete_object(Bucket=dest_bucket, Key=dest_key)
                    deleted += 1

        monitor.stop()

        if deleted > 0:
            print("已删除目标端多余文件: %d" % deleted)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
