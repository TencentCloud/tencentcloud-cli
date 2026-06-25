# -*- coding: utf-8 -*-
"""
图片处理模块

提供数据万象图片处理全部功能的 CLI 命令，包括：

基础处理：
- image_process:         图片下载时实时处理
- image_process_saveas:  图片云上处理另存
- image_upload_process:  图片上传时处理
- image_info:            获取图片基本信息

补充功能：
- image_exif_info:       获取图片 EXIF 信息
- image_ave_color:       获取图片主色调
- image_inspect:         异常图片检测
- image_style_add:       添加图片样式
- image_style_get:       查询图片样式
- image_style_delete:    删除图片样式
"""
import json
import os

from .ci_helpers import init_cos_client, handle_cos_error, print_result


# =====================================================================
# 基础处理
# =====================================================================

def image_process(args, parsed_globals):
    """下载时实时处理

    调用 SDK 的 ci_get_object 方法，对图片进行实时处理后下载到本地。
    原图不变。

    支持所有数据万象处理规则：缩放、裁剪、旋转、格式转换、水印、
    管道操作（多步处理用 | 连接）等。

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - key: 图片在 COS 上的对象键
            - rule: 数据万象处理规则（如 imageView2/2/w/800/h/600）
            - local_path: (可选) 本地保存路径，默认保存到当前目录
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]
        key = args["key"]
        rule = args["rule"]

        # 确定输出路径
        output = args.get("local_path") or os.path.basename(key)

        # 确保输出目录存在
        output_dir = os.path.dirname(output)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # 使用 SDK 原生的 ci_get_object 方法：下载时处理
        response = client.ci_get_object(
            Bucket=bucket,
            Key=key,
            DestImagePath=output,
            Rule=rule,
        )

        file_size = os.path.getsize(output) if os.path.exists(output) else 0

        # response 就是 headers dict
        print_result({
            "Status": "Success",
            "Output": os.path.abspath(output),
            "ContentType": response.get("Content-Type", ""),
            "ContentLength": str(file_size),
        }, response)
    except Exception as e:
        handle_cos_error(e)


def image_process_saveas(args, parsed_globals):
    """云上数据处理

    通过 POST 请求调用数据万象 ci_image_process 接口，
    对已存储在 COS 上的图片进行处理，结果另存为新的对象。
    原图保持不变。

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - key: 原图在 COS 上的对象键
            - rule: 数据万象处理规则
            - savekey: 处理后图片在 COS 上的存储路径
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]
        key = args["key"]
        rule = args["rule"]
        savekey = args["savekey"]

        pic_operations = json.dumps({
            "is_pic_info": 1,
            "rules": [{"fileid": savekey, "rule": rule}]
        })

        response, data = client.ci_image_process(
            Bucket=bucket,
            Key=key,
            PicOperations=pic_operations,
        )

        result = {
            "Status": "Success",
            "RequestId": response.get("x-cos-request-id", ""),
        }

        # 原图信息
        original = data.get("OriginalInfo", {}).get("ImageInfo", {})
        if original:
            result["OriginalImage"] = {
                "Format": original.get("Format", ""),
                "Width": original.get("Width", ""),
                "Height": original.get("Height", ""),
            }

        # 处理结果
        objects = data.get("ProcessResults", {}).get("Object", [])
        if isinstance(objects, dict):
            objects = [objects]
        result["ProcessedImages"] = [
            {
                "Key": obj.get("Key", ""),
                "ETag": obj.get("ETag", ""),
                "Format": obj.get("Format", ""),
                "Width": obj.get("Width", ""),
                "Height": obj.get("Height", ""),
                "Size": obj.get("Size", ""),
                "Quality": obj.get("Quality", ""),
            }
            for obj in objects
        ]

        print_result(result, response)
    except Exception as e:
        handle_cos_error(e)


def image_upload_process(args, parsed_globals):
    """上传时处理

    通过 PUT 请求调用数据万象 ci_put_object_from_local_file 接口，
    将本地图片上传到 COS，上传的同时进行图片处理并保存结果。

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - local: 本地图片文件路径
            - key: 上传到 COS 的对象键（原图存储路径）
            - rule: 数据万象处理规则
            - savekey: (可选) 处理后图片的存储路径，默认与 key 相同
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)
        bucket = args["bucket"]
        local = args["local"]
        key = args["key"]
        rule = args["rule"]
        savekey = args.get("savekey") or key

        # 校验本地文件存在
        if not os.path.isfile(local):
            raise FileNotFoundError(f"本地文件不存在: {local}")

        pic_operations = json.dumps({
            "is_pic_info": 1,
            "rules": [{"fileid": savekey, "rule": rule}]
        })

        response, data = client.ci_put_object_from_local_file(
            Bucket=bucket,
            LocalFilePath=local,
            Key=key,
            PicOperations=pic_operations,
        )

        result = {
            "Status": "Success",
            "RequestId": response.get("x-cos-request-id", ""),
        }

        # 原图信息
        original = data.get("OriginalInfo", {}).get("ImageInfo", {})
        if original:
            result["OriginalImage"] = {
                "Format": original.get("Format", ""),
                "Width": original.get("Width", ""),
                "Height": original.get("Height", ""),
            }

        # 处理结果
        objects = data.get("ProcessResults", {}).get("Object", [])
        if isinstance(objects, dict):
            objects = [objects]
        result["ProcessedImages"] = [
            {
                "Key": obj.get("Key", ""),
                "ETag": obj.get("ETag", ""),
                "Format": obj.get("Format", ""),
                "Width": obj.get("Width", ""),
                "Height": obj.get("Height", ""),
                "Size": obj.get("Size", ""),
                "Quality": obj.get("Quality", ""),
            }
            for obj in objects
        ]

        print_result(result, response)
    except Exception as e:
        handle_cos_error(e)


def image_info(args, parsed_globals):
    """获取图片基本信息

    调用 SDK 的 ci_get_image_info 方法获取图片的元数据。
    返回图片格式、尺寸、大小、MD5 等信息。

    Args:
        args: 命令参数字典
            - bucket: 存储桶名称
            - key: 图片在 COS 上的对象键
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        # 使用 SDK 原生的 ci_get_image_info 方法
        response, data = client.ci_get_image_info(
            Bucket=args["bucket"],
            Key=args["key"],
        )
        # SDK 返回的 data 是 rt.content (bytes)，需要先解码为 dict
        if isinstance(data, bytes):
            data = json.loads(data)
        print_result(data, response)
    except Exception as e:
        handle_cos_error(e)


# =====================================================================
# 补充功能：EXIF、主色调、异常图片检测、样式管理
# =====================================================================

def image_exif_info(args, parsed_globals):
    """获取图片 EXIF 信息

    Args:
        args:
            - bucket: 存储桶名称
            - key: 图片在 COS 上的对象键
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_get_image_exif_info(
            Bucket=args["bucket"],
            Key=args["key"],
        )

        resp_headers = None
        # 可能返回 bytes
        if isinstance(response, (bytes, bytearray)):
            response = json.loads(response)
        elif isinstance(response, tuple):
            resp_headers, data = response
            if isinstance(data, bytes):
                data = json.loads(data)
            response = data

        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def image_ave_color(args, parsed_globals):
    """获取图片主色调

    Args:
        args:
            - bucket: 存储桶名称
            - key: 图片在 COS 上的对象键
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_get_image_ave_info(
            Bucket=args["bucket"],
            Key=args["key"],
        )

        resp_headers = None
        # 可能返回 bytes
        if isinstance(response, (bytes, bytearray)):
            response = json.loads(response)
        elif isinstance(response, tuple):
            resp_headers, data = response
            if isinstance(data, bytes):
                data = json.loads(data)
            response = data

        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def image_inspect(args, parsed_globals):
    """异常图片检测

    检测图片中是否隐含其他类型的可疑文件（例如在图片格式中嵌入视频或其他文件）。
    API参考：https://cloud.tencent.com/document/product/460/75997

    Args:
        args:
            - bucket: 存储桶名称
            - key: 图片在 COS 上的对象键
        parsed_globals: TCCLI 全局参数

    Returns:
        JSON 结果包含：
            - picSize: 检测的原图大小（Bytes）
            - picType: 检测的原图类型（如 jpg、png）
            - suspicious: 是否检测到图片格式以外的文件（true/false）
            - suspiciousBeginByte: 可疑文件起始字节位置
            - suspiciousEndByte: 可疑文件末尾字节位置
            - suspiciousSize: 可疑文件大小
            - suspiciousType: 可疑文件类型（如 MPEG-TS）
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_image_inspect(
            Bucket=args["bucket"],
            Key=args["key"],
        )

        resp_headers = None
        if isinstance(response, (bytes, bytearray)):
            response = json.loads(response)
        elif isinstance(response, tuple):
            resp_headers, data = response
            if isinstance(data, bytes):
                data = json.loads(data)
            response = data

        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def image_style_add(args, parsed_globals):
    """添加图片样式

    Args:
        args:
            - bucket: 存储桶名称
            - style_name: 样式名称
            - style_body: 样式内容（处理规则）
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_put_image_style(
            Bucket=args["bucket"],
            Request={
                "StyleName": args["style_name"],
                "StyleBody": args["style_body"],
            },
        )
        # response 是 headers dict，从中提取 RequestId 并输出
        print_result(response, response)
    except Exception as e:
        handle_cos_error(e)


def image_style_get(args, parsed_globals):
    """查询图片样式

    Args:
        args:
            - bucket: 存储桶名称
            - style_name: (可选) 样式名称，不指定则列出所有
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        request = {}
        if args.get("style_name"):
            request["StyleName"] = args["style_name"]

        response = client.ci_get_image_style(
            Bucket=args["bucket"],
            Request=request,
        )
        # ci_get_image_style 返回 (response_headers, data) 元组
        resp_headers = None
        if isinstance(response, tuple):
            resp_headers, data = response
            response = data
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def image_style_delete(args, parsed_globals):
    """删除图片样式

    Args:
        args:
            - bucket: 存储桶名称
            - style_name: 样式名称
        parsed_globals: TCCLI 全局参数
    """
    try:
        client = init_cos_client(parsed_globals)

        response = client.ci_delete_image_style(
            Bucket=args["bucket"],
            Request={
                "StyleName": args["style_name"],
            },
        )
        # response 是 headers dict，从中提取 RequestId 并输出
        print_result(response, response)
    except Exception as e:
        handle_cos_error(e)
