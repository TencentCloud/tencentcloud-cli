# -*- coding: utf-8 -*-
"""
delete_object 单测 —— 对齐 coscli cmd/rm_test.go。
"""
from unittest.mock import patch

from conftest import MOCK_GLOBALS, make_cos_error


class TestDeleteObjectSingle:

    def test_success(self, mock_client, patch_init_client, capsys):
        """Convey: delete object success"""
        mod = patch_init_client("delete_object", mock_client)

        mod.delete_object(
            {"bucket": "b-1250000000", "cos_key": "k"},
            MOCK_GLOBALS,
        )

        mock_client.delete_object.assert_called_once()
        kwargs = mock_client.delete_object.call_args.kwargs
        assert kwargs["Bucket"] == "b-1250000000"
        assert kwargs["Key"] == "k"
        assert "删除成功" in capsys.readouterr().out

    def test_with_version_id(self, mock_client, patch_init_client):
        mod = patch_init_client("delete_object", mock_client)

        mod.delete_object(
            {"bucket": "b", "cos_key": "k", "version_id": "v1"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.delete_object.call_args.kwargs
        assert kwargs["VersionId"] == "v1"

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: delete object error"""
        mod = patch_init_client("delete_object", mock_client)
        mock_client.delete_object.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "DELETE", 404,
        )

        mod.delete_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "Error:" in capsys.readouterr().out


class TestDeleteObjectRecursive:

    def _setup_list(self, mock_client, files, dirs=None):
        """预设 list_objects 返回（list_all_objects_with_dirs 会用）"""
        contents = []
        for key, size in files:
            contents.append({
                "Key": key, "Size": str(size),
                "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"',
            })
        for d in dirs or []:
            contents.append({
                "Key": d, "Size": "0",
                "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"',
            })
        mock_client.list_objects.return_value = {
            "Contents": contents, "IsTruncated": "false",
        }

    def test_recursive_empty(self, mock_client, patch_init_client, capsys):
        """Convey: recursive 空前缀"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(mock_client, [])

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True, "force": True},
            MOCK_GLOBALS,
        )

        mock_client.delete_objects.assert_not_called()
        assert "没有匹配的对象需要删除" in capsys.readouterr().out

    def test_recursive_force_success(self, mock_client, patch_init_client):
        """Convey: recursive force 删除成功（文件 + 目录对象）"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(
            mock_client,
            files=[("pre/a.txt", 10), ("pre/b.txt", 20)],
            dirs=["pre/sub/"],
        )

        mod.delete_object(
            {"bucket": "b-1250000000", "cos_key": "pre/",
             "recursive": True, "force": True},
            MOCK_GLOBALS,
        )

        # 文件批量删除 1 次
        mock_client.delete_objects.assert_called_once()
        batch = mock_client.delete_objects.call_args.kwargs["Delete"]["Object"]
        assert {o["Key"] for o in batch} == {"pre/a.txt", "pre/b.txt"}
        # 目录对象逐个 delete_object
        mock_client.delete_object.assert_called_once()
        assert mock_client.delete_object.call_args.kwargs["Key"] == "pre/sub/"

    def test_recursive_include_filter(self, mock_client, patch_init_client):
        """include 过滤生效"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(
            mock_client,
            files=[("pre/a.txt", 1), ("pre/b.log", 2)],
        )

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True,
             "force": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        batch = mock_client.delete_objects.call_args.kwargs["Delete"]["Object"]
        assert [o["Key"] for o in batch] == ["pre/a.txt"]

    def test_recursive_confirm_cancel(self, mock_client, patch_init_client, capsys, monkeypatch):
        """非 force 模式下用户输入非 y —— 取消删除"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(mock_client, files=[("pre/a.txt", 1)])
        monkeypatch.setattr("builtins.input", lambda *_a, **_k: "n")

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True, "force": False},
            MOCK_GLOBALS,
        )

        mock_client.delete_objects.assert_not_called()
        assert "已取消删除" in capsys.readouterr().out

    def test_recursive_confirm_yes(self, mock_client, patch_init_client, monkeypatch):
        """非 force 模式下用户输入 y —— 继续删除"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(mock_client, files=[("pre/a.txt", 1)])
        monkeypatch.setattr("builtins.input", lambda *_a, **_k: "y")

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True, "force": False},
            MOCK_GLOBALS,
        )

        mock_client.delete_objects.assert_called_once()

    def test_recursive_retry_then_success(self, mock_client, patch_init_client):
        """Convey: err-retry-num 分支 —— 第一次失败，第二次成功"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(mock_client, files=[("pre/a.txt", 1), ("pre/b.txt", 2)])
        mock_client.delete_objects.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "POST", 500),
            {"Deleted": []},
        ]

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True,
             "force": True, "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.delete_objects.call_count == 2

    def test_recursive_retry_exhausted(self, mock_client, patch_init_client):
        """重试耗尽仍失败，不抛异常"""
        mod = patch_init_client("delete_object", mock_client)
        self._setup_list(mock_client, files=[("pre/a.txt", 1)])
        mock_client.delete_objects.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "POST", 500,
        )

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True,
             "force": True, "retry": 2},
            MOCK_GLOBALS,
        )

        # retry=2 -> 一共 3 次尝试
        assert mock_client.delete_objects.call_count == 3
