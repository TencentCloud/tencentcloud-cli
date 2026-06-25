# -*- coding: utf-8 -*-
"""
signurl 操作：生成预签名 URL
对齐 coscli signurl 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def signurl_object(args, parsed_globals):
    """生成 COS 对象的预签名 URL"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    expired = args.get("expired", 3600) or 3600
    method = (args.get("method", "GET") or "GET").upper()

    try:
        if method == "GET":
            url = client.get_presigned_download_url(
                Bucket=bucket,
                Key=cos_key,
                Expired=expired,
            )
        elif method == "PUT":
            url = client.get_presigned_url(
                Method="PUT",
                Bucket=bucket,
                Key=cos_key,
                Expired=expired,
            )
        else:
            url = client.get_presigned_url(
                Method=method,
                Bucket=bucket,
                Key=cos_key,
                Expired=expired,
            )

        print("预签名 URL (有效期 %d 秒):" % expired)
        print(url)

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))
