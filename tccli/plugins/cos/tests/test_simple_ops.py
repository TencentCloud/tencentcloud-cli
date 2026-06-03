# -*- coding: utf-8 -*-
"""
signurl / acl / tagging / du / cat / hash / lsparts / abort / restore 单测
—— 对齐 coscli cmd/signurl_test.go / object_acl_test.go / bucket_acl_test.go
    / object_tagging_test.go / du_test.go / cat_test.go / hash_test.go
    / lsparts_test.go / abort_test.go / restore_test.go。

这些命令都是 "简单查询/操作" 类：直接调用 SDK 后同步输出，无并发。
"""
from conftest import MOCK_GLOBALS, make_cos_error


# ========== signurl ==========

class TestSignurl:

    def test_get_default(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("signurl_object", mock_client)
        mock_client.get_presigned_download_url.return_value = "https://signed-get"

        mod.signurl_object(
            {"bucket": "b-1250000000", "cos_key": "k.txt"},
            MOCK_GLOBALS,
        )

        mock_client.get_presigned_download_url.assert_called_once()
        kwargs = mock_client.get_presigned_download_url.call_args.kwargs
        assert kwargs["Bucket"] == "b-1250000000"
        assert kwargs["Key"] == "k.txt"
        assert kwargs["Expired"] == 3600   # 默认
        assert "https://signed-get" in capsys.readouterr().out

    def test_put_method(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("signurl_object", mock_client)
        mock_client.get_presigned_url.return_value = "https://signed-put"

        mod.signurl_object(
            {"bucket": "b-1250000000", "cos_key": "k",
             "method": "put", "expired": 60},
            MOCK_GLOBALS,
        )

        mock_client.get_presigned_url.assert_called_once()
        kwargs = mock_client.get_presigned_url.call_args.kwargs
        assert kwargs["Method"] == "PUT"
        assert kwargs["Expired"] == 60

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("signurl_object", mock_client)
        mock_client.get_presigned_download_url.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )

        mod.signurl_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "Error:" in capsys.readouterr().out


# ========== bucket_acl / object_acl ==========

class TestAclObject:

    def _acl_body(self):
        return {
            "Owner": {"ID": "owner-id", "DisplayName": "owner"},
            "AccessControlList": {"Grant": [
                {"Grantee": {"ID": "u1", "type": "CanonicalUser"},
                 "Permission": "FULL_CONTROL"},
            ]},
        }

    def test_get_bucket_acl_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_bucket_acl.return_value = self._acl_body()

        mod.get_bucket_acl({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "存储桶 ACL" in out and "owner-id" in out and "u1" in out

    def test_get_bucket_acl_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_bucket_acl.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )
        mod.get_bucket_acl({"bucket": "b-1250000000"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_put_bucket_acl_with_grants(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)

        mod.put_bucket_acl(
            {"bucket": "b-1250000000", "acl": "public-read",
             "grant_read": 'id="1001"', "grant_full_control": 'id="1002"'},
            MOCK_GLOBALS,
        )

        mock_client.put_bucket_acl.assert_called_once()
        kwargs = mock_client.put_bucket_acl.call_args.kwargs
        assert kwargs["ACL"] == "public-read"
        assert kwargs["GrantRead"] == 'id="1001"'
        assert kwargs["GrantFullControl"] == 'id="1002"'
        assert "存储桶 ACL 设置成功" in capsys.readouterr().out

    def test_put_bucket_acl_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.put_bucket_acl.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "PUT", 403,
        )
        mod.put_bucket_acl({"bucket": "b-1250000000"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_get_object_acl_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_object_acl.return_value = self._acl_body()

        mod.get_object_acl({"bucket": "b-1250000000", "cos_key": "k"}, MOCK_GLOBALS)

        assert "对象 ACL" in capsys.readouterr().out

    def test_get_object_acl_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_object_acl.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "GET", 404,
        )
        mod.get_object_acl({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_put_object_acl(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)

        mod.put_object_acl(
            {"bucket": "b-1250000000", "cos_key": "k", "acl": "private"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.put_object_acl.call_args.kwargs
        assert kwargs["Key"] == "k"
        assert kwargs["ACL"] == "private"
        assert "对象 ACL 设置成功" in capsys.readouterr().out

    def test_put_object_acl_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.put_object_acl.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "PUT", 403,
        )
        mod.put_object_acl({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== tagging 三元组 ==========

class TestObjectTagging:

    def test_get_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)
        mock_client.get_object_tagging.return_value = {
            "TagSet": {"Tag": [
                {"Key": "env", "Value": "prod"},
                {"Key": "team", "Value": "ops"},
            ]}
        }

        mod.get_object_tagging({"bucket": "b-1250000000", "cos_key": "k"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "env = prod" in out
        assert "team = ops" in out

    def test_get_empty(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)
        mock_client.get_object_tagging.return_value = {"TagSet": {"Tag": []}}

        mod.get_object_tagging({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "(无标签)" in capsys.readouterr().out

    def test_get_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)
        mock_client.get_object_tagging.side_effect = make_cos_error(
            "NoSuchTagSet", "no tag set", "req-1", "GET", 404,
        )
        mod.get_object_tagging({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_put_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)

        mod.put_object_tagging(
            {"bucket": "b-1250000000", "cos_key": "k", "tags": "env=prod,team=ops"},
            MOCK_GLOBALS,
        )

        mock_client.put_object_tagging.assert_called_once()
        kwargs = mock_client.put_object_tagging.call_args.kwargs
        assert kwargs["Tagging"] == {
            "TagSet": {"Tag": [
                {"Key": "env", "Value": "prod"},
                {"Key": "team", "Value": "ops"},
            ]}
        }
        assert "对象标签设置成功" in capsys.readouterr().out

    def test_put_invalid_format(self, mock_client, patch_init_client, capsys):
        """Convey: invalid tag 格式"""
        mod = patch_init_client("tagging_object", mock_client)

        mod.put_object_tagging(
            {"bucket": "b", "cos_key": "k", "tags": "invalid-without-equal"},
            MOCK_GLOBALS,
        )

        mock_client.put_object_tagging.assert_not_called()
        assert "Error" in capsys.readouterr().out

    def test_put_empty_tags(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)

        mod.put_object_tagging({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        mock_client.put_object_tagging.assert_not_called()
        assert "Error" in capsys.readouterr().out

    def test_put_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)
        mock_client.put_object_tagging.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "PUT", 403,
        )
        mod.put_object_tagging(
            {"bucket": "b", "cos_key": "k", "tags": "a=b"}, MOCK_GLOBALS,
        )
        assert "Error:" in capsys.readouterr().out

    def test_delete_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)

        mod.delete_object_tagging({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        mock_client.delete_object_tagging.assert_called_once()
        assert "对象标签删除成功" in capsys.readouterr().out

    def test_delete_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("tagging_object", mock_client)
        mock_client.delete_object_tagging.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "DELETE", 403,
        )
        mod.delete_object_tagging({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== du ==========

class TestDuObject:

    def test_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("du_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "a.txt", "Size": "100", "StorageClass": "STANDARD"},
                {"Key": "b.txt", "Size": "200", "StorageClass": "STANDARD_IA"},
                {"Key": "c.txt", "Size": "300", "StorageClass": "STANDARD"},
                {"Key": "dir/", "Size": "0", "StorageClass": "STANDARD"},
            ],
            "IsTruncated": "false",
        }

        mod.du_object({"bucket": "b-1250000000", "prefix": "p/"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "总文件数: 3" in out
        assert "总文件夹数: 1" in out
        # 100+200+300=600 字节
        assert "600 字节" in out
        assert "STANDARD" in out
        assert "STANDARD_IA" in out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("du_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "NoSuchBucket", "no such", "req-1", "GET", 404,
        )
        mod.du_object({"bucket": "b"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== cat ==========

class TestCatObject:

    def test_success_text(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.return_value = {"Content-Length": "5"}

        body_stream = mock_client.get_object.return_value["Body"]
        body_stream.get_raw_stream.return_value.read.return_value = b"hello"

        mod.cat_object({"bucket": "b-1250000000", "cos_key": "k"}, MOCK_GLOBALS)

        assert "hello" in capsys.readouterr().out
        # 小文件不带 Range
        assert "Range" not in mock_client.get_object.call_args.kwargs

    def test_big_file_truncated(self, mock_client, patch_init_client, capsys):
        """文件超过 max_size 时自动加 Range"""
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.return_value = {
            "Content-Length": str(20 * 1024 * 1024),  # 20 MB
        }

        mod.cat_object(
            {"bucket": "b", "cos_key": "k", "max_size": 10},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.get_object.call_args.kwargs
        assert kwargs["Range"].startswith("bytes=0-")
        out = capsys.readouterr().out
        assert "仅显示前 10MB" in out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "GET", 404,
        )
        mod.cat_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== hash ==========

class TestHashObject:

    def test_local_md5(self, mock_client, patch_init_client, capsys, tmp_path):
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_text("hello")
        # "hello" 的 MD5 = 5d41402abc4b2a76b9719d911017c592

        mod.hash_object({"local_path": str(f), "hash_type": "md5"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "MD5" in out
        assert "5d41402abc4b2a76b9719d911017c592" in out

    def test_local_sha256(self, patch_init_client, mock_client, capsys, tmp_path):
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_bytes(b"")  # 空文件

        mod.hash_object({"local_path": str(f), "hash_type": "sha256"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        # 空文件 sha256
        assert "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" in out

    def test_local_path_not_exist(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("hash_object", mock_client)

        mod.hash_object(
            {"local_path": "/tmp/tccli-cos-test-nonexistent.txt"},
            MOCK_GLOBALS,
        )

        assert "本地文件不存在" in capsys.readouterr().out

    def test_cos_object_hash(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("hash_object", mock_client)
        mock_client.head_object.return_value = {
            "ETag": '"md5-abc"',
            "x-cos-hash-crc64ecma": "123456",
            "Content-Length": "100",
        }

        mod.hash_object(
            {"bucket": "b-1250000000", "cos_key": "k"},
            MOCK_GLOBALS,
        )

        out = capsys.readouterr().out
        assert "md5-abc" in out
        assert "123456" in out

    def test_cos_hash_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("hash_object", mock_client)
        mock_client.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "GET", 404,
        )
        mod.hash_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_nothing_to_hash(self, mock_client, patch_init_client, capsys):
        """没有指定 local_path 也没指定 bucket+cos_key"""
        mod = patch_init_client("hash_object", mock_client)

        mod.hash_object({}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "Error" in out


# ========== lsparts ==========

class TestLsparts:

    def test_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [
                {"Key": "big.bin", "UploadId": "upid-1",
                 "Initiated": "Mon, 07 Apr 2026 06:00:00 GMT"},
                {"Key": "big2.bin", "UploadId": "upid-2",
                 "Initiated": "Mon, 07 Apr 2026 06:00:01 GMT"},
            ],
            "IsTruncated": "false",
        }

        mod.lsparts_object({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "upid-1" in out and "upid-2" in out
        assert "共 2 个未完成的分片上传" in out

    def test_empty(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [], "IsTruncated": "false",
        }
        mod.lsparts_object({"bucket": "b"}, MOCK_GLOBALS)
        assert "没有未完成的分片上传" in capsys.readouterr().out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )
        mod.lsparts_object({"bucket": "b"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== abort ==========

class TestAbortMultipart:

    def test_abort_with_upload_id(self, mock_client, patch_init_client, capsys):
        """指定 upload_id + cos_key"""
        mod = patch_init_client("abort_multipart", mock_client)

        mod.abort_multipart(
            {"bucket": "b-1250000000", "cos_key": "k", "upload_id": "upid-1"},
            MOCK_GLOBALS,
        )

        mock_client.abort_multipart_upload.assert_called_once()
        kwargs = mock_client.abort_multipart_upload.call_args.kwargs
        assert kwargs["UploadId"] == "upid-1"
        assert kwargs["Key"] == "k"
        assert "已取消分片上传" in capsys.readouterr().out

    def test_abort_upload_id_missing_cos_key(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("abort_multipart", mock_client)

        mod.abort_multipart(
            {"bucket": "b", "upload_id": "upid-1"}, MOCK_GLOBALS,
        )

        mock_client.abort_multipart_upload.assert_not_called()
        assert "必须同时指定 cos_key" in capsys.readouterr().out

    def test_abort_all(self, mock_client, patch_init_client, capsys):
        """无 upload_id —— 列出并全部清理"""
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [
                {"Key": "a", "UploadId": "up1", "Initiated": "t1"},
                {"Key": "b", "UploadId": "up2", "Initiated": "t2"},
            ],
            "IsTruncated": "false",
        }

        mod.abort_multipart({"bucket": "b-1250000000"}, MOCK_GLOBALS)

        assert mock_client.abort_multipart_upload.call_count == 2
        out = capsys.readouterr().out
        assert "共清理 2 个" in out

    def test_abort_none(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [], "IsTruncated": "false",
        }

        mod.abort_multipart({"bucket": "b"}, MOCK_GLOBALS)

        mock_client.abort_multipart_upload.assert_not_called()
        assert "没有未完成的分片上传" in capsys.readouterr().out

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )
        mod.abort_multipart({"bucket": "b"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# ========== restore ==========

class TestRestoreObject:

    def test_single_success(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("restore_object", mock_client)

        mod.restore_object(
            {"bucket": "b-1250000000", "cos_key": "k",
             "days": 5, "tier": "Expedited"},
            MOCK_GLOBALS,
        )

        mock_client.restore_object.assert_called_once()
        kwargs = mock_client.restore_object.call_args.kwargs
        assert kwargs["RestoreRequest"]["Days"] == 5
        assert kwargs["RestoreRequest"]["CASJobParameters"]["Tier"] == "Expedited"
        out = capsys.readouterr().out
        assert "恢复请求已提交" in out
        assert "恢复天数: 5" in out
        assert "Expedited" in out

    def test_single_already_in_progress(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("restore_object", mock_client)
        mock_client.restore_object.side_effect = make_cos_error(
            "RestoreAlreadyInProgress", "already in progress", "req-1", "POST", 409,
        )

        mod.restore_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "恢复进行中" in capsys.readouterr().out

    def test_single_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("restore_object", mock_client)
        mock_client.restore_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "POST", 403,
        )
        mod.restore_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out

    def test_recursive_only_archive(self, mock_client, patch_init_client, capsys):
        """递归恢复只处理 ARCHIVE / DEEP_ARCHIVE"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1", "StorageClass": "STANDARD"},
                {"Key": "pre/b.txt", "Size": "2", "StorageClass": "ARCHIVE"},
                {"Key": "pre/c.txt", "Size": "3", "StorageClass": "DEEP_ARCHIVE"},
                {"Key": "pre/dir/", "Size": "0", "StorageClass": "STANDARD"},
            ],
            "IsTruncated": "false",
        }

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        # 只有 b.txt / c.txt 调用了 restore_object
        assert mock_client.restore_object.call_count == 2
        out = capsys.readouterr().out
        assert "提交 2" in out
