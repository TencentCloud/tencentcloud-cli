# -*- coding: utf-8 -*-
"""
cat 操作：查看 COS 对象内容
对齐 coscli cat 命令
"""
from qcloud_cos import CosServiceError
from .utils import init_cos_client, format_size


def cat_object(args, parsed_globals):
    """查看 COS 对象的内容"""
    client, region = init_cos_client(parsed_globals)

    bucket = args["bucket"]
    cos_key = args["cos_key"]
    byte_range = args.get("range", "") or ""
    max_size = args.get("max_size", 10) or 10  # 默认最大 10MB

    try:
        # 先获取对象大小
        head_response = client.head_object(
            Bucket=bucket,
            Key=cos_key,
        )
        content_length = int(head_response.get("Content-Length", 0))

        # 检查文件大小限制
        max_bytes = int(max_size) * 1024 * 1024
        if content_length > max_bytes and not byte_range:
            print("Warning: 文件大小 %s 超过限制 (%dMB)，仅显示前 %dMB" % (
                format_size(content_length), max_size, max_size))
            byte_range = "bytes=0-%d" % (max_bytes - 1)

        # 获取对象内容
        kwargs = {
            "Bucket": bucket,
            "Key": cos_key,
        }
        if byte_range:
            kwargs["Range"] = byte_range

        response = client.get_object(**kwargs)
        body = response["Body"]

        # 读取并输出内容
        content = body.get_raw_stream().read()
        try:
            text = content.decode("utf-8")
            print(text)
        except UnicodeDecodeError:
            print("Warning: 文件内容不是 UTF-8 编码的文本，显示为十六进制")
            hex_str = content[:1024].hex()
            for i in range(0, len(hex_str), 64):
                print(hex_str[i:i + 64])
            if len(content) > 1024:
                print("... (共 %d 字节)" % len(content))

    except CosServiceError as e:
        print("Error: %s (Code: %s, RequestId: %s)" % (
            e.get_error_msg(), e.get_error_code(), e.get_request_id()))
    except Exception as e:
        print("Error: %s" % str(e))