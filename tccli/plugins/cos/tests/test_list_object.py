# -*- coding: utf-8 -*-
"""
list_object 单测 —— 对齐 coscli cmd/ls_test.go。
"""
from conftest import MOCK_GLOBALS, make_cos_error


class TestListObject:

    def test_success_non_recursive(self, mock_client, patch_init_client, capsys):
        """Convey: list objects success（非递归，带 CommonPrefixes 目录）"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "a.txt", "Size": "100",
                 "LastModified": "Mon, 07 Apr 2026 06:00:00 GMT",
                 "StorageClass": "STANDARD", "ETag": '"e1"'},
                {"Key": "b.log", "Size": "200",
                 "LastModified": "Mon, 07 Apr 2026 06:00:01 GMT",
                 "StorageClass": "STANDARD_IA", "ETag": '"e2"'},
            ],
            "CommonPrefixes": [{"Prefix": "sub/"}],
            "IsTruncated": "false",
        }

        mod.list_object({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        kwargs = mock_client.list_objects.call_args.kwargs
        # 非递归且未指定 delimiter 时默认使用 /
        assert kwargs["Delimiter"] == "/"
        assert kwargs["Bucket"] == "b-1250000000"

        out = capsys.readouterr().out
        assert "DIR" in out and "sub/" in out
        assert "a.txt" in out and "b.log" in out
        assert "共 2 个对象" in out

    def test_recursive_disables_delimiter(self, mock_client, patch_init_client):
        """Convey: recursive 模式下 delimiter 被强制置空"""
        mod = patch_init_client("list_object", mock_client)

        mod.list_object(
            {"bucket": "b-1250000000", "prefix": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.list_objects.call_args.kwargs
        assert kwargs["Delimiter"] == ""
        assert kwargs["Prefix"] == "pre/"

    def test_include_exclude_filter(self, mock_client, patch_init_client, capsys):
        """Convey: include/exclude 过滤生效（纯逻辑 match_filters 不 mock）"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.list_object(
            {"bucket": "b-1250000000", "include": "*.txt", "recursive": True},
            MOCK_GLOBALS,
        )

        out = capsys.readouterr().out
        assert "a.txt" in out
        assert "b.log" not in out
        assert "共 1 个对象" in out

    def test_pagination_recursive(self, mock_client, patch_init_client):
        """Convey: 分页在 recursive 模式下自动翻页直到 IsTruncated=false"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "p1.txt", "Size": "1", "LastModified": "",
                           "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "true", "NextMarker": "p1.txt"},
            {"Contents": [{"Key": "p2.txt", "Size": "1", "LastModified": "",
                           "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
        ]

        mod.list_object(
            {"bucket": "b-1250000000", "recursive": True},
            MOCK_GLOBALS,
        )

        assert mock_client.list_objects.call_count == 2
        # 第二次请求的 Marker 应来自上一页的 NextMarker
        assert mock_client.list_objects.call_args_list[1].kwargs["Marker"] == "p1.txt"

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: list objects error"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "AccessDenied", "access denied", "req-1", "GET", 403,
        )

        mod.list_object({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "Error:" in out
        assert "AccessDenied" in out
        assert "req-1" in out
