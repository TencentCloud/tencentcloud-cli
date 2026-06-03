# -*- coding: utf-8 -*-
"""
list_buckets 操作：列出所有存储桶
对齐 coscli ls（无参数）命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def list_buckets(args, parsed_globals):
    """列出所有存储桶"""
    client, region = init_cos_client(parsed_globals)

    filter_region = args.get("filter_region", "") or ""

    try:
        response = client.list_buckets()

        buckets = response.get("Buckets", {}).get("Bucket", [])
        if not isinstance(buckets, list):
            buckets = [buckets]

        if not buckets:
            print("当前账号下没有存储桶")
            return

        # 按 region 过滤
        if filter_region:
            buckets = [b for b in buckets if b.get("Location", "") == filter_region]
            if not buckets:
                print("在 %s 地域下没有存储桶" % filter_region)
                return

        # 表头
        print("%-50s  %-15s  %-25s" % ("BucketName", "Region", "CreationDate"))
        print("-" * 95)

        for bucket in buckets:
            name = bucket.get("Name", "")
            location = bucket.get("Location", "")
            creation_date = bucket.get("CreationDate", "")
            print("%-50s  %-15s  %-25s" % (name, location, creation_date))

        print("\n共 %d 个存储桶" % len(buckets))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
