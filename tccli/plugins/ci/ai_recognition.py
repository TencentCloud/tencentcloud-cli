# -*- coding: utf-8 -*-
"""
内容识别（AI）模块

提供数据万象 AI 内容识别功能的 CLI 命令，包括：
- 图片上色（ai_image_coloring）
- 图片增强（ai_enhance_image）
- 智能裁剪（ai_image_crop）
- 图片修复（ai_image_repair）
- 人脸检测（ai_detect_face）
- 人脸特效（ai_face_effect）
- 人体识别（ai_body_recognition）
- 身份证识别（ai_id_card_ocr）
- 行驶证识别（ai_license_rec）
- 游戏场景识别（ai_game_rec）
- 商品抠图（goods_matting）
- 图片标签（detect_label）
- OCR 通用文字识别（ocr_process）
- 车辆识别（detect_car）
- 图片质量评估（assess_quality）
- 二维码识别（qrcode_detect）
- 二维码生成（qrcode_generate）
- 图片超分辨率（super_resolution）
- 通用抠图（pic_matting）
- 人像抠图（portrait_matting）

使用 ci_process 通用方法调用 AI 功能，通过 CiProcess 参数区分不同处理类型。
"""
import json
import os

from .ci_helpers import init_cos_client, handle_cos_error, print_result, save_response_to_file


def _ci_process_stream(client, bucket, key, ci_process, params=None, local_path=None):
    """通用的 ci_process 调用（返回图片流的场景）

    Args:
        client: CosS3Client 实例
        bucket: 存储桶名称
        key: COS 对象键
        ci_process: CI 处理类型名称
        params: (可选) 额外 query 参数
        local_path: (可选) 本地保存路径

    Returns:
        tuple: (dict 结果信息, dict response headers)
    """
    resp_headers, response = client.ci_process(
        Bucket=bucket,
        Key=key,
        CiProcess=ci_process,
        Params=params or {},
        Stream=True,
        NeedHeader=True,
    )

    # 某些 CI 方法（如 face-effect）在错误时返回 dict 而非 StreamBody
    if isinstance(response, dict):
        # 如果是错误响应，直接返回
        return response, resp_headers

    if local_path:
        total_bytes = save_response_to_file(response, local_path)
        return {
            "Status": "Success",
            "Output": os.path.abspath(local_path),
            "ContentLength": str(total_bytes),
        }, resp_headers
    else:
        return {
            "Status": "Success",
            "Message": "Stream response received but no local_path specified",
        }, resp_headers


def _ci_process_json(client, bucket, key, ci_process, params=None):
    """通用的 ci_process 调用（返回 JSON 的场景）

    Args:
        client: CosS3Client 实例
        bucket: 存储桶名称
        key: COS 对象键
        ci_process: CI 处理类型名称
        params: (可选) 额外 query 参数

    Returns:
        tuple: (dict API 返回的 JSON 数据, dict response headers)
    """
    resp_headers, response = client.ci_process(
        Bucket=bucket,
        Key=key,
        CiProcess=ci_process,
        Params=params or {},
        NeedHeader=True,
    )
    return response, resp_headers


# ---------------------------------------------------------------------------
# AI 图像处理（返回图片流）
# ---------------------------------------------------------------------------

def ai_image_coloring(args, parsed_globals):
    """AI 图片上色"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "AIImageColoring", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_enhance_image(args, parsed_globals):
    """AI 图片增强"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("denoise"):
            params["denoise"] = args["denoise"]
        if args.get("sharpen"):
            params["sharpen"] = args["sharpen"]
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "AIEnhanceImage", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_image_crop(args, parsed_globals):
    """AI 智能裁剪"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {
            "width": args["width"],
            "height": args["height"],
        }
        if args.get("fixed"):
            params["fixed"] = args["fixed"]
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "AIImageCrop", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_image_repair(args, parsed_globals):
    """AI 图片修复"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("mask_key"):
            params["MaskPic"] = args["mask_key"]
        elif args.get("mask_url"):
            params["MaskPic"] = args["mask_url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "ImageRepair", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 人脸与人体
# ---------------------------------------------------------------------------

def ai_detect_face(args, parsed_globals):
    """AI 人脸检测"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("max_face_num"):
            params["max-face-num"] = args["max_face_num"]
        response, resp_headers = _ci_process_json(
            client, args["bucket"], key,
            "DetectFace", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_face_effect(args, parsed_globals):
    """AI 人脸特效"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {"type": args["effect_type"]}
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "face-effect", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_body_recognition(args, parsed_globals):
    """AI 人体识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        response, resp_headers = _ci_process_json(
            client, args["bucket"], key,
            "AIBodyRecognition", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# OCR 识别
# ---------------------------------------------------------------------------

def ai_id_card_ocr(args, parsed_globals):
    """身份证 OCR 识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("card_side"):
            params["CardSide"] = args["card_side"]
        if args.get("url"):
            params["detect-url"] = args["url"]
        response, resp_headers = _ci_process_json(
            client, args["bucket"], key,
            "IDCardOCR", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_license_rec(args, parsed_globals):
    """行驶证/驾驶证 OCR 识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("card_type"):
            params["CardType"] = args["card_type"]
        if args.get("url"):
            params["detect-url"] = args["url"]
        response, resp_headers = _ci_process_json(
            client, args["bucket"], key,
            "LicenseRec", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ai_game_rec(args, parsed_globals):
    """游戏场景识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        response, resp_headers = _ci_process_json(
            client, args["bucket"], key,
            "GameRec", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def ocr_process(args, parsed_globals):
    """通用 OCR 文字识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key and not args.get("url"):
            raise ValueError("必须指定 key 或 url 参数")

        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        if args.get("language_type"):
            params["language-type"] = args["language_type"]
        if args.get("ispdf"):
            params["ispdf"] = args["ispdf"]
        if args.get("pdf_pagenumber"):
            params["pdf-pagenumber"] = args["pdf_pagenumber"]

        response, resp_headers = _ci_process_json(
            client, args["bucket"], key or "",
            "OCR", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 图片识别（SDK 已内置的方法）
# ---------------------------------------------------------------------------

def detect_label(args, parsed_globals):
    """图片标签识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key and not args.get("url"):
            raise ValueError("必须指定 key 或 url 参数")

        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]

        response, resp_headers = _ci_process_json(
            client, args["bucket"], key or "",
            "detect-label", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def detect_car(args, parsed_globals):
    """车辆识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key and not args.get("url"):
            raise ValueError("必须指定 key 或 url 参数")

        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]

        response, resp_headers = _ci_process_json(
            client, args["bucket"], key or "",
            "DetectCar", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def assess_quality(args, parsed_globals):
    """图片质量评估"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key and not args.get("url"):
            raise ValueError("必须指定 key 或 url 参数")

        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]

        response, resp_headers = _ci_process_json(
            client, args["bucket"], key or "",
            "AssessQuality", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 二维码
# ---------------------------------------------------------------------------

def qrcode_detect(args, parsed_globals):
    """二维码识别"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key and not args.get("url"):
            raise ValueError("必须指定 key 或 url 参数")

        cover = int(args["cover"]) if args.get("cover") else 0
        params = {"cover": str(cover)}
        if args.get("url"):
            params["detect-url"] = args["url"]

        response, resp_headers = _ci_process_json(
            client, args["bucket"], key or "",
            "QRcode", params,
        )
        print_result(response, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def qrcode_generate(args, parsed_globals):
    """二维码生成"""
    try:
        client = init_cos_client(parsed_globals)
        kwargs = {
            "Bucket": args["bucket"],
            "QrcodeContent": args["text"],
        }
        if args.get("width"):
            kwargs["Width"] = int(args["width"])
        if args.get("mode"):
            kwargs["Mode"] = int(args["mode"])
        response = client.ci_qrcode_generate(**kwargs)
        if args.get("local_path") and response.get("ResultImage"):
            import base64
            img_data = base64.b64decode(response["ResultImage"])
            output_dir = os.path.dirname(args["local_path"])
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            with open(args["local_path"], "wb") as f:
                f.write(img_data)
            response["Output"] = os.path.abspath(args["local_path"])
        print_result(response)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 图片增强处理（SDK 已内置的方法）
# ---------------------------------------------------------------------------

def super_resolution(args, parsed_globals):
    """图片超分辨率"""
    try:
        client = init_cos_client(parsed_globals)
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], args["key"],
            "AIImageSuperResolution", {},
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


# ---------------------------------------------------------------------------
# 抠图（使用 ci_process 通用方法）
# ---------------------------------------------------------------------------

def goods_matting(args, parsed_globals):
    """商品抠图"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "GoodsMatting", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def pic_matting(args, parsed_globals):
    """通用抠图"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "AIPicMatting", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)


def portrait_matting(args, parsed_globals):
    """人像抠图"""
    try:
        client = init_cos_client(parsed_globals)
        key = args.get("key")
        if not key:
            raise ValueError("必须指定 key 参数")
        params = {}
        if args.get("url"):
            params["detect-url"] = args["url"]
        result, resp_headers = _ci_process_stream(
            client, args["bucket"], key,
            "AIPortraitMatting", params,
            args.get("local_path"),
        )
        print_result(result, resp_headers)
    except Exception as e:
        handle_cos_error(e)
