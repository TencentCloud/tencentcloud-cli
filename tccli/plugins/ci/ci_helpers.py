# -*- coding: utf-8 -*-
"""
CI（数据万象）插件公共工具模块

提供以下功能：
- init_cos_client: COS 客户端初始化（数据万象复用 COS SDK 客户端）
- handle_cos_error: 统一错误处理
- print_result: JSON 格式化输出
- save_response_to_file: 流式写入本地文件
"""
import json
import os
import sys

from qcloud_cos import CosConfig, CosS3Client, CosServiceError


def _load_credential_from_profile(parsed_globals):
    """从 TCCLI 配置文件或环境变量中加载认证信息

    当 parsed_globals 中的 secretId/secretKey 为 None 时（即用户未通过命令行
    --secretId/--secretKey 传入），自动从以下来源按优先级读取：
      1. ~/.tccli/<profile>.credential 文件
      2. 环境变量 TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY

    同时加载 region 配置（如果命令行未指定）。

    Args:
        parsed_globals: TCCLI 传入的全局参数字典（会被就地修改）

    Returns:
        修改后的 parsed_globals
    """
    secret_id = parsed_globals.get("secretId")
    secret_key = parsed_globals.get("secretKey")

    # 如果命令行已经传入了密钥，直接返回
    if secret_id and secret_key:
        return parsed_globals

    # 确定 profile
    profile = parsed_globals.get("profile") or os.environ.get("TCCLI_PROFILE", "default")
    configure_path = os.path.join(os.path.expanduser("~"), ".tccli")

    # 尝试从 credential 文件加载
    cred_file = os.path.join(configure_path, profile + ".credential")
    cred = {}
    if os.path.isfile(cred_file):
        try:
            with open(cred_file, "r") as f:
                cred = json.load(f)
        except (json.JSONDecodeError, IOError):
            pass

    if not secret_id:
        parsed_globals["secretId"] = (
            cred.get("secretId")
            or os.environ.get("TENCENTCLOUD_SECRET_ID")
        )
    if not secret_key:
        parsed_globals["secretKey"] = (
            cred.get("secretKey")
            or os.environ.get("TENCENTCLOUD_SECRET_KEY")
        )
    if not parsed_globals.get("token"):
        parsed_globals["token"] = (
            cred.get("token")
            or os.environ.get("TENCENTCLOUD_TOKEN")
        )

    # 尝试从 configure 文件加载 region
    if not parsed_globals.get("region"):
        conf_file = os.path.join(configure_path, profile + ".configure")
        if os.path.isfile(conf_file):
            try:
                with open(conf_file, "r") as f:
                    conf = json.load(f)
                sys_param = conf.get("_sys_param", {})
                parsed_globals["region"] = (
                    sys_param.get("region")
                    or os.environ.get("TENCENTCLOUD_REGION")
                )
            except (json.JSONDecodeError, IOError):
                pass

    # 最终校验
    if not parsed_globals.get("secretId") or not parsed_globals.get("secretKey"):
        raise ValueError(
            "SecretId and SecretKey is Required! "
            "请通过 tccli configure 配置密钥，或通过 --secretId/--secretKey 参数传入，"
            "或设置环境变量 TENCENTCLOUD_SECRET_ID/TENCENTCLOUD_SECRET_KEY"
        )

    return parsed_globals


def init_cos_client(parsed_globals):
    """初始化 COS 客户端

    从 parsed_globals 中读取认证信息和区域配置，创建 CosS3Client 实例。
    如果命令行未传入密钥，会自动从 TCCLI 配置文件或环境变量中加载。
    数据万象 CI 的 API 底层复用 COS SDK 的客户端。

    Args:
        parsed_globals: TCCLI 传入的全局参数字典，包含:
            - secretId: 腾讯云 SecretId
            - secretKey: 腾讯云 SecretKey
            - token: 临时密钥 Token（可选）
            - region: 地域（可选，默认 ap-guangzhou）
            - endpoint: 自定义 Endpoint（可选）

    Returns:
        CosS3Client 实例
    """
    # 确保密钥已加载（从配置文件或环境变量）
    _load_credential_from_profile(parsed_globals)

    config = CosConfig(
        Region=parsed_globals.get("region") or "ap-guangzhou",
        SecretId=parsed_globals["secretId"],
        SecretKey=parsed_globals["secretKey"],
        Token=parsed_globals.get("token"),
        Endpoint=parsed_globals.get("endpoint"),
    )
    return CosS3Client(config)


def handle_cos_error(e):
    """统一错误处理

    将 COS SDK 异常和通用异常格式化为 JSON 输出到 stderr 并退出。

    Args:
        e: 捕获到的异常
    """
    if isinstance(e, CosServiceError):
        result = {
            "Error": {
                "Code": e.get_error_code(),
                "Message": e.get_error_msg(),
                "RequestId": e.get_request_id(),
                "StatusCode": e.get_status_code(),
            }
        }
    else:
        result = {"Error": {"Code": "ClientError", "Message": str(e)}}
    print(json.dumps(result, indent=2, ensure_ascii=False), file=sys.stderr)
    sys.exit(1)


def _extract_request_id(headers):
    """从 HTTP 响应头中提取 RequestId

    Args:
        headers: HTTP 响应头字典

    Returns:
        dict: 包含 RequestId 信息的字典（可能为空）
    """
    if not headers or not isinstance(headers, dict):
        return {}
    result = {}
    ci_req_id = headers.get("x-ci-request-id")
    cos_req_id = headers.get("x-cos-request-id")
    if ci_req_id:
        result["RequestId"] = ci_req_id
    if cos_req_id:
        result["CosRequestId"] = cos_req_id
    return result


def print_result(data, headers=None):
    """JSON 格式化输出，可选附带 RequestId

    Args:
        data: 要输出的字典或列表
        headers: (可选) HTTP 响应头字典，用于提取 RequestId
    """
    if isinstance(data, dict) and headers:
        req_ids = _extract_request_id(headers)
        if req_ids:
            # 将 RequestId 注入到输出中，放在最前面
            data = {**req_ids, **data}
    print(json.dumps(data, indent=2, ensure_ascii=False))


def save_response_to_file(response, output_path):
    """将 COS 响应体流式写入本地文件

    支持两种响应格式：
    1. dict: 标准 COS 响应，包含 Body 字段（如 get_snapshot）
    2. StreamBody: ci_process(Stream=True) 直接返回 StreamBody 对象

    Args:
        response: COS SDK 返回的 response 对象
        output_path: 本地保存路径

    Returns:
        写入的字节数
    """
    from qcloud_cos.cos_client import StreamBody

    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    total_bytes = 0
    with open(output_path, "wb") as f:
        if isinstance(response, StreamBody):
            # ci_process(Stream=True) 直接返回 StreamBody
            for chunk in response.get_stream(1024 * 1024):
                f.write(chunk)
                total_bytes += len(chunk)
        elif isinstance(response, dict) and "Body" in response:
            # 标准 COS 响应格式
            body = response["Body"]
            if isinstance(body, StreamBody):
                for chunk in body.get_stream(1024 * 1024):
                    f.write(chunk)
                    total_bytes += len(chunk)
            else:
                for chunk in body.get_raw_stream().stream(1024 * 1024):
                    f.write(chunk)
                    total_bytes += len(chunk)
        elif isinstance(response, bytes):
            f.write(response)
            total_bytes = len(response)
        else:
            raise ValueError(f"Unsupported response type: {type(response)}")
    return total_bytes
