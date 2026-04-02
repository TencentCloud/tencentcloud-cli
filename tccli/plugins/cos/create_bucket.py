# -*- coding: utf-8 -*-
"""
create_bucket 操作：创建存储桶
对齐 coscli mb 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def create_bucket(args, parsed_globals):
    """创建存储桶"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    acl = args.get("acl", "private") or "private"

    try:
        client.create_bucket(
            Bucket=bucket,
            ACL=acl,
        )
        print("存储桶创建成功: %s (Region: %s, ACL: %s)" % (bucket, region, acl))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))