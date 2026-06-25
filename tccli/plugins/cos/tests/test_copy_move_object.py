# -*- coding: utf-8 -*-
"""
copy_object / move_object 单测 —— 对齐 coscli cmd/cp_test.go CosCopy 分支 + move 行为。
"""
from conftest import MOCK_GLOBALS, make_cos_error


# ========== copy ==========

class TestCopySingle:

    def test_success(self, mock_client, patch_init_client, capsys):
        """Convey: CosCopy single object success"""
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "src-b-1250000000", "cos_key": "a.txt",
             "dest_bucket": "dst-b-1250000000", "dest_key": "b.txt"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_called_once()
        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["Bucket"] == "dst-b-1250000000"
        assert kwargs["Key"] == "b.txt"
        assert kwargs["CopySource"] == {
            "Bucket": "src-b-1250000000",
            "Key": "a.txt",
            "Region": "ap-guangzhou",
        }

    def test_storage_class_and_meta(self, mock_client, patch_init_client):
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b",
             "storage_class": "ARCHIVE",
             "meta": "env=prod"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["StorageClass"] == "ARCHIVE"
        assert kwargs["Metadata"] == {"x-cos-meta-env": "prod"}
        assert kwargs["CopyStatus"] == "Replaced"   # 单文件复制用 CopyStatus

    def test_dest_bucket_defaults_to_src(self, mock_client, patch_init_client):
        """未指定 dest_bucket 时默认与 src 相同"""
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "same-b-125", "cos_key": "a", "dest_key": "b"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["Bucket"] == "same-b-125"
        assert kwargs["CopySource"]["Bucket"] == "same-b-125"

    def test_retry_then_success(self, mock_client, patch_init_client):
        mod = patch_init_client("copy_object", mock_client)
        mock_client.copy.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            {},
        ]

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b", "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: CosCopy error"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.copy.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "PUT", 404,
        )

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b", "retry": 0},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


class TestCopyRecursive:

    def test_recursive_empty(self, mock_client, patch_init_client):
        """Convey: CosCopy recursive (no objects)"""
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_key": "dst/", "recursive": True},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_not_called()

    def test_recursive_with_files(self, mock_client, patch_init_client):
        """Convey: CosCopy recursive success with files"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/empty/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.copy_object(
            {"bucket": "src-b-1250000000", "cos_key": "pre/",
             "dest_bucket": "dst-b-1250000000", "dest_key": "dst/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # 无 include → a.txt / b.log 都复制
        assert mock_client.copy.call_count == 2
        # 空目录通过 put_object 在目标桶创建
        mock_client.put_object.assert_called()
        put_kwargs = mock_client.put_object.call_args.kwargs
        assert put_kwargs["Bucket"] == "dst-b-1250000000"
        assert put_kwargs["Key"].endswith("empty/")

    def test_recursive_include_filter(self, mock_client, patch_init_client):
        """include 过滤只保留 a.txt"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.copy_object(
            {"bucket": "src-b-1250000000", "cos_key": "pre/",
             "dest_bucket": "dst-b-1250000000", "dest_key": "dst/",
             "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 1
        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["Bucket"] == "dst-b-1250000000"
        assert kwargs["Key"] == "dst/a.txt"


# ========== move ==========

class TestMoveSingle:

    def test_success(self, mock_client, patch_init_client):
        """单文件移动 = copy + delete 源"""
        mod = patch_init_client("move_object", mock_client)

        mod.move_object(
            {"bucket": "b-125", "cos_key": "a.txt",
             "dest_bucket": "b-125", "dest_key": "b.txt"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_called_once()
        mock_client.delete_object.assert_called_once()
        del_kwargs = mock_client.delete_object.call_args.kwargs
        assert del_kwargs["Bucket"] == "b-125"
        assert del_kwargs["Key"] == "a.txt"

    def test_retry_then_success(self, mock_client, patch_init_client):
        mod = patch_init_client("move_object", mock_client)
        mock_client.copy.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            {},
        ]

        mod.move_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b", "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2
        # 成功后才调用 delete_object（1 次）
        assert mock_client.delete_object.call_count == 1

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("move_object", mock_client)
        mock_client.copy.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "PUT", 404,
        )

        mod.move_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b", "retry": 0},
            MOCK_GLOBALS,
        )

        # copy 失败后 delete 不应被调用
        mock_client.delete_object.assert_not_called()
        assert "Error:" in capsys.readouterr().out


class TestMoveRecursive:

    def test_recursive_with_files(self, mock_client, patch_init_client):
        """Convey: move recursive —— 每个文件 copy + delete"""
        mod = patch_init_client("move_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.txt", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "dst/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2
        assert mock_client.delete_object.call_count == 2
