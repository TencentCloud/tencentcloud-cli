# -*- coding: utf-8 -*-
"""
hash 操作：计算本地文件或 COS 对象的哈希值
对齐 coscli hash 命令
"""
import os
import hashlib
from qcloud_cos import CosServiceError
from .utils import init_cos_client, calculate_local_crc64


def _calculate_local_hash(file_path, hash_type="md5"):
    """计算本地文件的哈希值"""
    if hash_type == "crc64":
        result = calculate_local_crc64(file_path)
        if result is None:
            return "Error: 计算 CRC64 需要安装 crcmod 库: pip install crcmod"
        return result

    if hash_type == "md5":
        h = hashlib.md5()
    elif hash_type == "sha1":
        h = hashlib.sha1()
    elif hash_type == "sha256":
        h = hashlib.sha256()
    else:
        return "Error: 不支持的哈希类型: %s (可选: md5, sha1, sha256, crc64)" % hash_type

    with open(file_path, "rb") as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


def hash_object(args, parsed_globals):
    """计算本地文件或 COS 对象的哈希值"""
    client, region = init_cos_client(parsed_globals)

    hash_type = (args.get("hash_type", "md5") or "md5").lower()
    local_path = args.get("local_path", "") or ""
    bucket = args.get("bucket", "") or ""
    cos_key = args.get("cos_key", "") or ""

    if not local_path and not (bucket and cos_key):
        print("Error: 请指定 --local_path 或 --bucket + --cos_key")
        return

    # 计算本地文件哈希
    if local_path:
        if not os.path.exists(local_path):
            print("Error: 本地文件不存在: %s" % local_path)
            return
        if not os.path.isfile(local_path):
            print("Error: 指定路径不是文件: %s" % local_path)
            return

        result = _calculate_local_hash(local_path, hash_type)
        print("本地文件: %s" % local_path)
        print("%s: %s" % (hash_type.upper(), result))

    # 获取 COS 对象哈希信息
    if bucket and cos_key:
        try:
            response = client.head_object(
                Bucket=bucket,
                Key=cos_key,
            )
            etag = response.get("ETag", "").strip('"')
            crc64 = response.get("x-cos-hash-crc64ecma", "")
            content_length = response.get("Content-Length", "")

            print("COS 对象: cos://%s/%s" % (bucket, cos_key))
            print("大小: %s 字节" % content_length)
            print("ETag (MD5): %s" % etag)
            if crc64:
                print("CRC64: %s" % crc64)

        except CosServiceError as e:
            print("Error: %s (Code: %s, RequestId: %s)" % (
                e.get_error_msg(), e.get_error_code(), e.get_request_id()))