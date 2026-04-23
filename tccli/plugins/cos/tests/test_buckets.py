# -*- coding: utf-8 -*-
"""
list_buckets / create_bucket / delete_bucket 单测
—— 对齐 coscli cmd/ls_test.go（list buckets 分支）/ mb_test.go / rb_test.go。
"""
from conftest import MOCK_GLOBALS, make_cos_error


# ========== list_buckets ==========

class TestListBuckets:

    def test_success(self, mock_client, patch_init_client, capsys):
        """Convey: list buckets success"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.return_value = {
            "Buckets": {"Bucket": [
                {"Name": "b1-125000", "Location": "ap-guangzhou",
                 "CreationDate": "2026-04-01T00:00:00Z"},
                {"Name": "b2-125000", "Location": "ap-beijing",
                 "CreationDate": "2026-04-02T00:00:00Z"},
            ]},
        }

        mod.list_buckets({}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "b1-125000" in out and "b2-125000" in out
        assert "共 2 个存储桶" in out

    def test_filter_region(self, mock_client, patch_init_client, capsys):
        """Convey: filter_region 过滤"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.return_value = {
            "Buckets": {"Bucket": [
                {"Name": "b1-125000", "Location": "ap-guangzhou",
                 "CreationDate": "2026-04-01T00:00:00Z"},
                {"Name": "b2-125000", "Location": "ap-beijing",
                 "CreationDate": "2026-04-02T00:00:00Z"},
            ]},
        }

        mod.list_buckets({"filter_region": "ap-beijing"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "b2-125000" in out
        assert "b1-125000" not in out

    def test_empty(self, mock_client, patch_init_client, capsys):
        """空存储桶列表"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.return_value = {"Buckets": {"Bucket": []}}

        mod.list_buckets({}, MOCK_GLOBALS)

        assert "当前账号下没有存储桶" in capsys.readouterr().out

    def test_filter_region_no_match(self, mock_client, patch_init_client, capsys):
        """filter_region 无匹配"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.return_value = {
            "Buckets": {"Bucket": [
                {"Name": "b1-125000", "Location": "ap-guangzhou",
                 "CreationDate": ""},
            ]},
        }

        mod.list_buckets({"filter_region": "ap-shanghai"}, MOCK_GLOBALS)

        assert "在 ap-shanghai 地域下没有存储桶" in capsys.readouterr().out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: list buckets error"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )

        mod.list_buckets({}, MOCK_GLOBALS)

        assert "Error:" in capsys.readouterr().out


# ========== create_bucket ==========

class TestCreateBucket:

    def test_success_default_acl(self, mock_client, patch_init_client, capsys):
        """Convey: create bucket success"""
        mod = patch_init_client("create_bucket", mock_client)

        mod.create_bucket({"bucket": "test-bucket-1250000000"}, MOCK_GLOBALS)

        kwargs = mock_client.create_bucket.call_args.kwargs
        assert kwargs["Bucket"] == "test-bucket-1250000000"
        assert kwargs["ACL"] == "private"   # 默认

        out = capsys.readouterr().out
        assert "存储桶创建成功" in out
        assert "ap-guangzhou" in out

    def test_success_custom_acl(self, mock_client, patch_init_client):
        """Convey: 指定 acl"""
        mod = patch_init_client("create_bucket", mock_client)

        mod.create_bucket(
            {"bucket": "b-1250000000", "acl": "public-read"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.create_bucket.call_args.kwargs
        assert kwargs["ACL"] == "public-read"

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: create bucket error"""
        mod = patch_init_client("create_bucket", mock_client)
        mock_client.create_bucket.side_effect = make_cos_error(
            "BucketAlreadyExists", "exists", "req-1", "PUT", 409,
        )

        mod.create_bucket({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "Error:" in out
        assert "BucketAlreadyExists" in out


# ========== delete_bucket ==========

class TestDeleteBucket:

    def test_success(self, mock_client, patch_init_client, capsys):
        """Convey: delete bucket success"""
        mod = patch_init_client("delete_bucket", mock_client)

        mod.delete_bucket({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        mock_client.delete_bucket.assert_called_once()
        assert "存储桶删除成功" in capsys.readouterr().out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        """Convey: delete bucket error"""
        mod = patch_init_client("delete_bucket", mock_client)
        mock_client.delete_bucket.side_effect = make_cos_error(
            "BucketNotEmpty", "not empty", "req-1", "DELETE", 409,
        )

        mod.delete_bucket({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "Error:" in out
        assert "BucketNotEmpty" in out

    def test_force_clear_and_delete(self, mock_client, patch_init_client, capsys):
        """Convey: force delete success —— 清空对象、版本、分片后删桶"""
        mod = patch_init_client("delete_bucket", mock_client)
        # 1. 普通对象（一页就结束）
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "a"}, {"Key": "b"}],
            "IsTruncated": "false",
        }
        # 2. 版本对象
        mock_client.list_objects_versions.return_value = {
            "Version": [{"Key": "a", "VersionId": "v1"}],
            "DeleteMarker": [{"Key": "b", "VersionId": "v2"}],
            "IsTruncated": "false",
        }
        # 3. 分片上传
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [{"Key": "u1", "UploadId": "up1"}],
            "IsTruncated": "false",
        }

        mod.delete_bucket({"bucket": "b-1250000000", "force": True}, MOCK_GLOBALS)

        # 普通对象 + 版本对象各调用一次 delete_objects
        assert mock_client.delete_objects.call_count == 2
        # 分片 abort
        mock_client.abort_multipart_upload.assert_called_once()
        mock_client.delete_bucket.assert_called_once()

        out = capsys.readouterr().out
        assert "存储桶删除成功" in out
        assert "已删除 2 个对象" in out
        assert "已删除 2 个版本对象" in out
        assert "已清理 1 个未完成的分片上传" in out
