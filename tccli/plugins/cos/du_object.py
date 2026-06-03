# -*- coding: utf-8 -*-
"""
du 操作：统计存储桶或目录的大小
对齐 coscli du 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, format_size


def du_object(args, parsed_globals):
    """统计存储桶或指定前缀下的对象总大小和数量"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    prefix = args.get("prefix", "") or ""

    try:
        total_size = 0
        total_count = 0
        total_dir_count = 0
        storage_stats = {}
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
                    # 目录标记单独统计
                    if key.endswith("/"):
                        total_dir_count += 1
                        continue
                    size = int(content.get("Size", 0))
                    storage_class = content.get("StorageClass", "STANDARD")

                    total_size += size
                    total_count += 1

                    if storage_class not in storage_stats:
                        storage_stats[storage_class] = {"count": 0, "size": 0}
                    storage_stats[storage_class]["count"] += 1
                    storage_stats[storage_class]["size"] += size

            if response.get("IsTruncated") == "true":
                marker = response.get("NextMarker", "")
            else:
                break

        # 输出统计结果
        target = "cos://%s/%s" % (bucket, prefix) if prefix else "cos://%s" % bucket
        print("统计: %s" % target)
        print("-" * 60)
        print("总文件数: %d" % total_count)
        print("总文件夹数: %d" % total_dir_count)
        print("总大小:   %s (%d 字节)" % (format_size(total_size), total_size))

        if storage_stats:
            print("\n按存储类型统计:")
            for sc, stats in sorted(storage_stats.items()):
                print("  %-20s  %d 个对象, %s" % (sc, stats["count"], format_size(stats["size"])))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))