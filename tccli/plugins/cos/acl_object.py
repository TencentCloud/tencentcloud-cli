# -*- coding: utf-8 -*-
"""
ACL 操作：获取和设置存储桶/对象的访问控制
对齐 coscli 的 ACL 管理能力
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def get_bucket_acl(args, parsed_globals):
    """获取存储桶的访问控制列表"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]

    try:
        response = client.get_bucket_acl(Bucket=bucket)

        owner = response.get("Owner", {})
        print("存储桶 ACL: %s" % bucket)
        print("-" * 60)
        print("Owner ID:          %s" % owner.get("ID", ""))
        print("Owner DisplayName: %s" % owner.get("DisplayName", ""))

        grants = response.get("AccessControlList", {}).get("Grant", [])
        if not isinstance(grants, list):
            grants = [grants]

        print("\n授权列表:")
        for grant in grants:
            grantee = grant.get("Grantee", {})
            permission = grant.get("Permission", "")
            grantee_id = grantee.get("ID", "")
            grantee_type = grantee.get("type", "")
            grantee_uri = grantee.get("URI", "")
            if grantee_uri:
                print("  - URI: %-40s  Permission: %s" % (grantee_uri, permission))
            else:
                print("  - ID: %-40s  Type: %-15s  Permission: %s" % (grantee_id, grantee_type, permission))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def put_bucket_acl(args, parsed_globals):
    """设置存储桶的访问控制"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    acl = args.get("acl", "") or ""
    grant_read = args.get("grant_read", "") or ""
    grant_write = args.get("grant_write", "") or ""
    grant_full_control = args.get("grant_full_control", "") or ""

    try:
        kwargs = {"Bucket": bucket}
        if acl:
            kwargs["ACL"] = acl
        if grant_read:
            kwargs["GrantRead"] = grant_read
        if grant_write:
            kwargs["GrantWrite"] = grant_write
        if grant_full_control:
            kwargs["GrantFullControl"] = grant_full_control

        client.put_bucket_acl(**kwargs)
        print("存储桶 ACL 设置成功: %s" % bucket)
        if acl:
            print("ACL: %s" % acl)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def get_object_acl(args, parsed_globals):
    """获取对象的访问控制列表"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]

    try:
        response = client.get_object_acl(Bucket=bucket, Key=cos_key)

        owner = response.get("Owner", {})
        print("对象 ACL: cos://%s/%s" % (bucket, cos_key))
        print("-" * 60)
        print("Owner ID:          %s" % owner.get("ID", ""))
        print("Owner DisplayName: %s" % owner.get("DisplayName", ""))

        grants = response.get("AccessControlList", {}).get("Grant", [])
        if not isinstance(grants, list):
            grants = [grants]

        print("\n授权列表:")
        for grant in grants:
            grantee = grant.get("Grantee", {})
            permission = grant.get("Permission", "")
            grantee_id = grantee.get("ID", "")
            grantee_type = grantee.get("type", "")
            grantee_uri = grantee.get("URI", "")
            if grantee_uri:
                print("  - URI: %-40s  Permission: %s" % (grantee_uri, permission))
            else:
                print("  - ID: %-40s  Type: %-15s  Permission: %s" % (grantee_id, grantee_type, permission))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))


def put_object_acl(args, parsed_globals):
    """设置对象的访问控制"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    acl = args.get("acl", "") or ""
    grant_read = args.get("grant_read", "") or ""
    grant_full_control = args.get("grant_full_control", "") or ""

    try:
        kwargs = {"Bucket": bucket, "Key": cos_key}
        if acl:
            kwargs["ACL"] = acl
        if grant_read:
            kwargs["GrantRead"] = grant_read
        if grant_full_control:
            kwargs["GrantFullControl"] = grant_full_control

        client.put_object_acl(**kwargs)
        print("对象 ACL 设置成功: cos://%s/%s" % (bucket, cos_key))
        if acl:
            print("ACL: %s" % acl)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
