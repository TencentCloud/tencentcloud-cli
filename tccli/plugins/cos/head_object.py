# -*- coding: utf-8 -*-
"""
head 操作：查询 COS 对象的元信息
对齐 coscli head 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client


def head_object(args, parsed_globals):
    """查询 COS 对象的元信息"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    version_id = args.get("version_id", "") or ""

    try:
        kwargs = {
            "Bucket": bucket,
            "Key": cos_key,
        }
        if version_id:
            kwargs["VersionId"] = version_id

        response = client.head_object(**kwargs)

        print("对象元信息: cos://%s/%s" % (bucket, cos_key))
        print("-" * 50)
        print("Content-Length:  %s" % response.get("Content-Length", ""))
        print("Content-Type:    %s" % response.get("Content-Type", ""))
        print("ETag:            %s" % response.get("ETag", ""))
        print("Last-Modified:   %s" % response.get("Last-Modified", ""))
        print("Storage-Class:   %s" % response.get("x-cos-storage-class", "STANDARD"))

        # CRC64
        crc64 = response.get("x-cos-hash-crc64ecma", "")
        if crc64:
            print("CRC64:           %s" % crc64)

        # 版本 ID
        vid = response.get("x-cos-version-id", "")
        if vid:
            print("Version-Id:      %s" % vid)

        # 恢复状态
        restore = response.get("x-cos-restore", "")
        if restore:
            print("Restore:         %s" % restore)

        # 输出自定义元数据
        for key, value in response.items():
            if key.startswith("x-cos-meta-"):
                print("%-16s %s" % (key + ":", value))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
