# -*- coding: utf-8 -*-
"""
download_object 单测 —— 对齐 coscli cmd/cp_test.go 中 Download 分支。
"""
import os

from conftest import MOCK_GLOBALS, make_cos_error


class TestDownloadSingle:

    def test_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: Download single file success"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.head_object.return_value = {"Content-Length": "100"}
        local = tmp_path / "dst.txt"

        mod.download_object(
            {"bucket": "b-1250000000", "cos_key": "k", "local_path": str(local)},
            MOCK_GLOBALS,
        )

        mock_client.download_file.assert_called_once()
        kwargs = mock_client.download_file.call_args.kwargs
        assert kwargs["Bucket"] == "b-1250000000"
        assert kwargs["Key"] == "k"
        assert kwargs["DestFilePath"] == str(local)
        assert "progress_callback" in kwargs

    def test_with_version_and_rate_limiting(self, mock_client, patch_init_client, tmp_path):
        mod = patch_init_client("download_object", mock_client)
        local = tmp_path / "dst.txt"

        mod.download_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(local),
             "version_id": "v-1", "rate_limiting": 5},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.download_file.call_args.kwargs
        assert kwargs["VersionId"] == "v-1"
        assert kwargs["TrafficLimit"] == str(5 * 1024 * 1024 * 8)

    def test_creates_parent_dir(self, mock_client, patch_init_client, tmp_path):
        """本地目标目录不存在时自动创建"""
        mod = patch_init_client("download_object", mock_client)
        local = tmp_path / "new_dir" / "sub" / "dst.txt"

        mod.download_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(local)},
            MOCK_GLOBALS,
        )

        assert os.path.isdir(os.path.dirname(str(local)))

    def test_retry_then_success(self, mock_client, patch_init_client, tmp_path):
        mod = patch_init_client("download_object", mock_client)
        mock_client.download_file.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "GET", 500),
            None,
        ]

        mod.download_object(
            {"bucket": "b", "cos_key": "k",
             "local_path": str(tmp_path / "dst.txt"), "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 2

    def test_sdk_error(self, mock_client, patch_init_client, tmp_path, capsys):
        """Convey: Download error —— 最终失败被上层 except 捕获"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.download_file.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "GET", 404,
        )

        mod.download_object(
            {"bucket": "b", "cos_key": "k",
             "local_path": str(tmp_path / "dst.txt"), "retry": 0},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


class TestDownloadRecursive:

    def test_recursive_empty(self, mock_client, patch_init_client, tmp_path):
        """Convey: Download directory success (no objects)"""
        mod = patch_init_client("download_object", mock_client)

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True},
            MOCK_GLOBALS,
        )

        mock_client.download_file.assert_not_called()

    def test_recursive_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: Download directory success with files"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "10",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/sub/b.log", "Size": "20",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/empty_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True},
            MOCK_GLOBALS,
        )

        # 两个文件都下载
        assert mock_client.download_file.call_count == 2
        # 空目录在本地被创建
        assert os.path.isdir(str(tmp_path / "empty_dir"))

    def test_recursive_include_filter(self, mock_client, patch_init_client, tmp_path):
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 1
        assert mock_client.download_file.call_args.kwargs["Key"] == "pre/a.txt"
