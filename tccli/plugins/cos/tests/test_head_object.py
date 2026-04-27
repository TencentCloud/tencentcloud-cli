# -*- coding: utf-8 -*-
"""
head_object 单测 —— 对齐 coscli cmd/stat_test.go 的打桩风格。
"""
from conftest import MOCK_GLOBALS, cos_module, make_cos_error


class TestHeadObject:

    def test_success(self, mock_client, patch_init_client, capsys):
        """Convey: stat success"""
        mod = patch_init_client("head_object", mock_client)
        mock_client.head_object.return_value = {
            "Content-Length": "2048",
            "Content-Type": "application/octet-stream",
            "ETag": '"etag-xyz"',
            "Last-Modified": "Mon, 07 Apr 2026 06:00:00 GMT",
            "x-cos-storage-class": "STANDARD_IA",
            "x-cos-hash-crc64ecma": "1234567890",
            "x-cos-version-id": "v-001",
            "x-cos-meta-author": "alice",
        }

        mod.head_object(
            {"bucket": "test-bucket-1250000000", "cos_key": "path/to/file.txt"},
            MOCK_GLOBALS,
        )

        mock_client.head_object.assert_called_once()
        kwargs = mock_client.head_object.call_args.kwargs
        assert kwargs["Bucket"] == "test-bucket-1250000000"
        assert kwargs["Key"] == "path/to/file.txt"
        assert "VersionId" not in kwargs

        out = capsys.readouterr().out
        assert "Content-Length" in out
        assert "2048" in out
        assert "STANDARD_IA" in out
        assert "CRC64" in out
        assert "1234567890" in out
        assert "v-001" in out
        assert "x-cos-meta-author" in out
        assert "alice" in out

    def test_with_version_id(self, mock_client, patch_init_client):
        """Convey: version-id 参数透传"""
        mod = patch_init_client("head_object", mock_client)

        mod.head_object(
            {"bucket": "b-1250000000", "cos_key": "k", "version_id": "v-abc"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.head_object.call_args.kwargs
        assert kwargs["VersionId"] == "v-abc"

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: stat NoSuchKey error —— 命令吞掉异常并打印 Error"""
        mod = patch_init_client("head_object", mock_client)
        mock_client.head_object.side_effect = make_cos_error(
            code="NoSuchKey", msg="Object not found", req_id="req-123",
            method="GET", status_code=404,
        )

        mod.head_object(
            {"bucket": "b-1250000000", "cos_key": "not-exist.txt"},
            MOCK_GLOBALS,
        )

        out = capsys.readouterr().out
        assert "Error:" in out
        assert "NoSuchKey" in out
        assert "Code:" in out
        assert "RequestId" in out
        assert "req-123" in out

    def test_init_client_error(self, monkeypatch):
        """Convey: CreateClient error —— init_cos_client 异常被允许抛出到上层框架处理。"""
        mod = cos_module("head_object")
        def _raise(_pg):
            raise Exception("mock CreateClient error")
        monkeypatch.setattr(mod, "init_cos_client", _raise)

        # head_object 未显式捕获 init 异常，允许其抛出（等价于 coscli 的 error 返回）
        try:
            mod.head_object({"bucket": "b-1250000000", "cos_key": "k"}, MOCK_GLOBALS)
            assert False, "expect exception"
        except Exception as e:
            assert "mock CreateClient error" in str(e)