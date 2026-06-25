# -*- coding: utf-8 -*-
"""
tccli cos 插件单元测试公共 fixture 与工具。

打桩风格对齐 coscli（Go + gomonkey）：
- coscli 用 gomonkey.ApplyMethodFunc 打桩 *cos.BucketService/ObjectService 方法；
- tccli 这边用 unittest.mock.MagicMock 对 CosS3Client 的方法做等价打桩；
- coscli 用 ApplyFunc(util.NewClient, ...) 打桩工厂函数；
- tccli 这边用 patch.object(<module>, "init_cos_client") 做等价打桩。

关键注意：`tccli.plugins.cos` 的 __init__ 中有
    from .head_object import head_object
这会让 `tccli.plugins.cos.head_object` 被解析为**函数**而不是模块，
所以 @patch("tccli.plugins.cos.head_object.init_cos_client") 会失败（属性不存在）。
统一使用 cos_module(name) 加载底层子模块，然后对模块对象打桩。
"""
import importlib

import pytest
from unittest.mock import MagicMock
from qcloud_cos import CosServiceError


# ========= 全局参数：对齐 coscli 的 setupTestConfig 中假 secret =========
MOCK_GLOBALS = {
    "secretId": "test-secret-id",
    "secretKey": "test-secret-key",
    "token": None,
    "region": "ap-guangzhou",
    "endpoint": None,
    "profile": "default",
}


def cos_module(name):
    """加载 tccli.plugins.cos 下的**子模块对象**（绕过 __init__ 的同名函数覆盖）。

    用法：
        mod = cos_module("head_object")
        with patch.object(mod, "init_cos_client", return_value=(mock_client, "ap-guangzhou")):
            mod.head_object(args, MOCK_GLOBALS)
    """
    return importlib.import_module("tccli.plugins.cos.%s" % name)


def make_cos_error(code="InternalError", msg="mock error", req_id="mock-req-id",
                   method="GET", status_code=500):
    """
    构造真实可用的 CosServiceError（满足 get_error_code/msg/request_id/status_code 断言）。
    CosServiceError 的真实签名为 __init__(method, message, status_code)，
    其中 message 必须是 COS 服务端返回的 XML 错误体。
    """
    xml = (
        "<?xml version='1.0' encoding='utf-8' ?>"
        "<Error>"
        "<Code>%s</Code>"
        "<Message>%s</Message>"
        "<Resource>bucket/key</Resource>"
        "<RequestId>%s</RequestId>"
        "<TraceId>mock-trace-id</TraceId>"
        "</Error>" % (code, msg, req_id)
    )
    return CosServiceError(method, xml, status_code)


def build_mock_client():
    """
    构造一个 qcloud_cos.CosS3Client 的 MagicMock，并为最常见的方法预设合理返回值。
    单测中可以进一步覆盖个别方法的 return_value/side_effect。
    """
    mc = MagicMock()

    # head_object —— 默认返回最小可用头
    mc.head_object.return_value = {
        "Content-Length": "1024",
        "Content-Type": "text/plain",
        "ETag": '"etag-abc"',
        "Last-Modified": "Mon, 07 Apr 2026 06:00:00 GMT",
        "x-cos-storage-class": "STANDARD",
        "x-cos-hash-crc64ecma": "",  # 默认留空以避开 CRC 校验分支
    }

    # list_objects（注意 IsTruncated 是字符串 "false"）
    mc.list_objects.return_value = {
        "Contents": [],
        "CommonPrefixes": [],
        "IsTruncated": "false",
    }

    # list_multipart_uploads
    mc.list_multipart_uploads.return_value = {"Upload": [], "IsTruncated": "false"}

    # list_buckets
    mc.list_buckets.return_value = {"Buckets": {"Bucket": []}}

    # list_objects_versions
    mc.list_objects_versions.return_value = {
        "Version": [], "DeleteMarker": [], "IsTruncated": "false",
    }

    # ACL 默认值
    mc.get_bucket_acl.return_value = {
        "Owner": {"ID": "owner-id", "DisplayName": "owner"},
        "AccessControlList": {"Grant": []},
    }
    mc.get_object_acl.return_value = {
        "Owner": {"ID": "owner-id", "DisplayName": "owner"},
        "AccessControlList": {"Grant": []},
    }

    # Tagging 默认值
    mc.get_object_tagging.return_value = {"TagSet": {"Tag": []}}

    # 预签名 URL
    mc.get_presigned_url.return_value = "https://example.com/signed-url"
    mc.get_presigned_download_url.return_value = "https://example.com/signed-download-url"

    # get_object（流式）
    body_stream = MagicMock()
    body_stream.get_raw_stream.return_value.read.return_value = b"hello world"
    mc.get_object.return_value = {"Body": body_stream, "Content-Length": "11"}

    # upload_file / download_file / copy / put_object / delete_object 等 —— 默认成功
    mc.upload_file.return_value = None
    mc.download_file.return_value = None
    mc.copy.return_value = {}
    mc.create_bucket.return_value = {}
    mc.delete_bucket.return_value = {}
    mc.put_object.return_value = {}
    mc.delete_object.return_value = {}
    mc.delete_objects.return_value = {"Deleted": []}
    mc.put_bucket_acl.return_value = {}
    mc.put_object_acl.return_value = {}
    mc.put_object_tagging.return_value = {}
    mc.delete_object_tagging.return_value = {}
    mc.abort_multipart_upload.return_value = {}
    mc.restore_object.return_value = {}

    return mc


# ========= pytest fixture =========

@pytest.fixture
def mock_client():
    """提供一个预设好的 CosS3Client MagicMock。"""
    return build_mock_client()


@pytest.fixture
def globals_param():
    """提供一份不可变的 MOCK_GLOBALS 副本（避免用例互相污染）。"""
    return dict(MOCK_GLOBALS)


@pytest.fixture
def patch_init_client(monkeypatch):
    """
    返回一个辅助函数：`patch_init_client(module_name, client, region="ap-guangzhou")`
    会在指定子模块上打桩 init_cos_client，使其返回 (client, region)。

    用法：
        def test_xxx(mock_client, patch_init_client):
            mod = patch_init_client("head_object", mock_client)
            mod.head_object(args, MOCK_GLOBALS)
    """
    def _do(module_name, client, region="ap-guangzhou"):
        mod = cos_module(module_name)
        monkeypatch.setattr(mod, "init_cos_client",
                            lambda _pg: (client, region))
        return mod
    return _do