# -*- coding: utf-8 -*-
"""
list 操作：列出 COS 存储桶中的文件
对齐 coscli ls 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, format_size, match_filters


def list_object(args, parsed_globals):
    """列出 COS 存储桶中的文件"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    prefix = args.get("prefix", "") or ""
    marker = args.get("marker", "") or ""
    max_keys = args.get("max_keys", 1000) or 1000
    delimiter = args.get("delimiter", "") or ""
    recursive = args.get("recursive", False)
    include = args.get("include", "") or ""
    exclude = args.get("exclude", "") or ""

    # 递归模式下不使用 delimiter，以列出所有层级的对象
    if recursive:
        delimiter = ""

    try:
        total_count = 0
        total_size = 0

        while True:
            response = client.list_objects(
                Bucket=bucket,
                Prefix=prefix,
                Marker=marker,
                MaxKeys=max_keys,
                Delimiter=delimiter,
            )

            # 输出公共前缀（目录）
            if "CommonPrefixes" in response:
                for common_prefix in response["CommonPrefixes"]:
                    print("DIR  %s" % common_prefix["Prefix"])

            # 输出文件列表
            if "Contents" in response:
                for content in response["Contents"]:
                    key = content["Key"]

                    # include/exclude 过滤
                    if not match_filters(key, include, exclude):
                        continue

                    size = int(content.get("Size", 0))
                    last_modified = content.get("LastModified", "")
                    storage_class = content.get("StorageClass", "STANDARD")
                    total_count += 1
                    total_size += size
                    print("%-12s  %-20s  %-25s  %s" % (
                        format_size(size), storage_class, last_modified, key))

            # 分页处理
            if response.get("IsTruncated") == "true":
                marker = response.get("NextMarker", "")
                if not recursive:
                    print("\n结果已截断，下一页 Marker: %s" % marker)
                    break
            else:
                break

        # 输出统计信息
        if recursive or total_count > 0:
            print("\n共 %d 个对象, 总大小: %s" % (total_count, format_size(total_size)))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))