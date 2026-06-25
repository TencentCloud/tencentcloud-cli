# -*- coding: utf-8 -*-
"""
最终覆盖率补齐 —— 针对剩余 89-94% 覆盖率的命令文件：
move_object / sync_copy_object / sync_download_object / sync_upload_object /
delete_bucket / lsparts / abort_multipart / copy_object（剩余分支）等。
"""
import os

from conftest import MOCK_GLOBALS, make_cos_error


# =============================================================
# move_object —— single 分支补全
# =============================================================

class TestMoveObjectMoreBranches:

    def test_single_head_fails_file_size_zero(self, mock_client, patch_init_client):
        """Convey: 单文件 move 时 head_object 失败 → file_size=0，move 继续"""
        mod = patch_init_client("move_object", mock_client)
        mock_client.head_object.side_effect = RuntimeError("boom")

        mod.move_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_called_once()
        mock_client.delete_object.assert_called_once()

    def test_single_storage_class_passed(self, mock_client, patch_init_client):
        """Convey: 单文件 move 透传 storage_class"""
        mod = patch_init_client("move_object", mock_client)

        mod.move_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "b",
             "storage_class": "ARCHIVE"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["StorageClass"] == "ARCHIVE"

    def test_recursive_empty_dir_excluded(self, mock_client, patch_init_client):
        """Convey: recursive 空目录被 include/exclude 过滤"""
        mod = patch_init_client("move_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 空目录被跳过 → put_object 不被调用
        mock_client.put_object.assert_not_called()

    def test_recursive_retry_exhausted_logs_err(self, mock_client, patch_init_client):
        """Convey: recursive 子文件 move 重试耗尽 → 记录 err"""
        mod = patch_init_client("move_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.copy.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True, "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 → 2 次尝试；copy 全失败 → delete_object 不被调用
        assert mock_client.copy.call_count == 2


# =============================================================
# sync_copy_object 剩余分支
# =============================================================

class TestSyncCopyObjectMoreBranches:

    def test_dir_excluded_by_filter(self, mock_client, patch_init_client):
        """Convey: 源端空目录被 include/exclude 过滤跳过"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            # 源端
            {"Contents": [
                {"Key": "p/keep_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "p/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "p/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "p/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ], "IsTruncated": "false"},
            # 目标端
            {"Contents": [], "IsTruncated": "false"},
        ]

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/",
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # include=*.txt → 只有 a.txt 被复制；
        # excluded_dir 和 b.log 都被 include 过滤
        assert mock_client.copy.call_count == 1
        assert mock_client.copy.call_args.kwargs["Key"] == "d/a.txt"

    def test_retry_exhausted_logs_err(self, mock_client, patch_init_client):
        """Convey: copy 失败 —— 记录 err，顶层不抛异常"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "p/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
            {"Contents": [], "IsTruncated": "false"},
        ]
        mock_client.copy.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/", "retry": 0},
            MOCK_GLOBALS,
        )

        # retry=0 → 1 次尝试
        assert mock_client.copy.call_count == 1

    def test_delete_extra_dir(self, mock_client, patch_init_client):
        """Convey: --delete 删除目标端多余的目录对象"""
        mod = patch_init_client("sync_copy_object", mock_client)

        src_listing = {
            "Contents": [{"Key": "p/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        dest_listing_no_dir = {
            "Contents": [
                {"Key": "d/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        # list_all_objects_with_dirs(目标-for delete) 包含多余目录
        dest_with_dirs = {
            "Contents": [
                {"Key": "d/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "d/orphan_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        mock_client.list_objects.side_effect = [
            src_listing, dest_listing_no_dir, dest_with_dirs,
        ]
        # 源目标 CRC 不同 → 仍会复制 a.txt
        mock_client.head_object.return_value = {"x-cos-hash-crc64ecma": "0"}

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/", "delete": True},
            MOCK_GLOBALS,
        )

        delete_keys = [c.kwargs["Key"] for c in mock_client.delete_object.call_args_list]
        assert "d/orphan_dir/" in delete_keys


# =============================================================
# sync_download_object 剩余分支
# =============================================================

class TestSyncDownloadObjectMoreBranches:

    def test_local_path_auto_created(self, mock_client, patch_init_client, tmp_path):
        """Convey: local_path 不存在时自动 makedirs"""
        mod = patch_init_client("sync_download_object", mock_client)
        target = tmp_path / "new_root" / "subdir"   # 不存在
        assert not target.exists()

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(target)},
            MOCK_GLOBALS,
        )

        # 目录被创建
        assert target.is_dir()

    def test_ensure_dir_creates_parent(self, mock_client, patch_init_client, tmp_path):
        """Convey: _ensure_dir 分支 —— 下载文件的父目录不存在时自动创建"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/sub1/sub2/deep.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        # sub1/sub2 会在 _ensure_dir 中被创建
        assert (tmp_path / "sub1" / "sub2").is_dir()

    def test_retry_exhausted_logs_err(self, mock_client, patch_init_client, tmp_path):
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.download_file.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "GET", 500,
        )

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "retry": 0},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 1


# =============================================================
# sync_upload_object 剩余分支（39, 59, 63, 79-80, 136-137, 157）
# =============================================================

class TestSyncUploadObjectMoreBranches:

    def test_local_path_not_dir_returns_early(self, mock_client, patch_init_client, capsys):
        """Convey: local_path 是文件而非目录 → 立即 return（已在 test_sync_objects.py 覆盖）"""
        # 此处仅走顶层 retry=None 分支：设置 retry=None 走默认 3
        mod = patch_init_client("sync_upload_object", mock_client)

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": "/tmp/tccli-cos-sync-upload-not-exist",
             "retry": None},
            MOCK_GLOBALS,
        )

        assert "本地路径不是目录" in capsys.readouterr().out

    def test_local_dir_empty_dir_key_exists_skip(self, mock_client, patch_init_client, tmp_path):
        """Convey: 根目录恰为空（rel_dir == "."）—— 走 cos_prefix 尾带 / 的分支"""
        mod = patch_init_client("sync_upload_object", mock_client)
        # tmp_path 本身是个空目录（rel_dir == "."）
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        # 会尝试创建 pre/ 这个空目录标记（因为根目录是空的）
        mock_client.put_object.assert_called()
        kwargs = mock_client.put_object.call_args.kwargs
        assert kwargs["Key"] == "pre/"

    def test_file_excluded_by_filter(self, mock_client, patch_init_client, tmp_path):
        """Convey: 本地文件被 include/exclude 过滤跳过"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.log").write_text("b")
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        keys = [c.kwargs["Key"] for c in mock_client.upload_file.call_args_list]
        assert keys == ["pre/a.txt"]

    def test_retry_exhausted_logs_err(self, mock_client, patch_init_client, tmp_path):
        """Convey: sync_upload 单文件重试耗尽 → 记录 err"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }
        mock_client.upload_file.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 → 2 次尝试
        assert mock_client.upload_file.call_count == 2


# =============================================================
# delete_bucket 剩余分支（59, 80, 87, 99-100, 123, 127, 139）
# =============================================================

class TestDeleteBucketMoreBranches:

    def test_force_versions_single_version_dict(self, mock_client, patch_init_client):
        """Convey: list_objects_versions 返回单个 Version dict（非 list），需要 wrap 成 list"""
        mod = patch_init_client("delete_bucket", mock_client)

        mock_client.list_objects.return_value = {"Contents": [], "IsTruncated": "false"}
        mock_client.list_objects_versions.return_value = {
            "Version": {"Key": "a", "VersionId": "v1"},          # 单对象，非 list
            "DeleteMarker": {"Key": "b", "VersionId": "v2"},     # 单对象，非 list
            "IsTruncated": "false",
        }
        mock_client.list_multipart_uploads.return_value = {
            "Upload": {"Key": "u1", "UploadId": "up1"},          # 单对象，非 list
            "IsTruncated": "false",
        }

        mod.delete_bucket({"bucket": "b", "force": True}, MOCK_GLOBALS)

        # 版本 + 删除标记 → 1 次 delete_objects
        mock_client.delete_objects.assert_called_once()
        # 分片 abort 1 次
        mock_client.abort_multipart_upload.assert_called_once()


# =============================================================
# abort_multipart / lsparts 剩余分支
# =============================================================

class TestAbortMultipartMoreBranches:

    def test_uploads_as_dict(self, mock_client, patch_init_client):
        """Convey: list_multipart_uploads 返回单个 Upload dict"""
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": {"Key": "a", "UploadId": "u1", "Initiated": "t"},
            "IsTruncated": "false",
        }

        mod.abort_multipart({"bucket": "b"}, MOCK_GLOBALS)

        mock_client.abort_multipart_upload.assert_called_once()


class TestLspartsMoreBranches:

    def test_uploads_as_dict(self, mock_client, patch_init_client, capsys):
        """Convey: list_multipart_uploads 返回单个 Upload dict"""
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": {"Key": "a", "UploadId": "u1", "Initiated": "t"},
            "IsTruncated": "false",
        }

        mod.lsparts_object({"bucket": "b"}, MOCK_GLOBALS)

        assert "u1" in capsys.readouterr().out


# =============================================================
# copy_object 剩余分支（30, 58-59, 138, 155, 178, 180-181）
# =============================================================

class TestCopyObjectRemaining:

    def test_single_dest_bucket_defaults_when_none(self, mock_client, patch_init_client):
        """Convey: dest_bucket = None 时，回落为 src bucket（覆盖 or 分支）"""
        mod = patch_init_client("copy_object", mock_client)

        # dest_bucket 显式传 None，走 `or bucket` 分支
        mod.copy_object(
            {"bucket": "b-125", "cos_key": "a", "dest_bucket": None, "dest_key": "d"},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_args.kwargs["Bucket"] == "b-125"

    def test_single_head_fails_file_size_zero(self, mock_client, patch_init_client):
        """Convey: 单文件 copy 时 head_object 失败 → file_size=0"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.head_object.side_effect = RuntimeError("boom")

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "d"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_called_once()

    def test_recursive_storage_class_and_metadata_combined(self, mock_client, patch_init_client):
        """Convey: recursive + storage_class + metadata （走到 MetadataDirective 分支）"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True,
             "storage_class": "ARCHIVE", "meta": "a=1"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["StorageClass"] == "ARCHIVE"
        assert kwargs["Metadata"] == {"x-cos-meta-a": "1"}
        assert kwargs["MetadataDirective"] == "Replaced"


# =============================================================
# head_object / list_object / list_buckets / du / restore / acl 剩余一点点分支
# =============================================================

class TestHeadMoreBranches:

    def test_restore_header(self, mock_client, patch_init_client, capsys):
        """Convey: head_object 返回 x-cos-restore 时输出"""
        mod = patch_init_client("head_object", mock_client)
        mock_client.head_object.return_value = {
            "Content-Length": "10",
            "x-cos-restore": 'ongoing-request="true"',
        }

        mod.head_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "Restore:" in capsys.readouterr().out


class TestTaggingMoreBranches:

    def test_put_returns_early_on_invalid_format(self, mock_client, patch_init_client, capsys):
        """put_object_tagging：tags 只含 `invalid-without-equal` —— 打印 Error 并 return（tagging_object.py 第 25 行）"""
        mod = patch_init_client("tagging_object", mock_client)

        mod.put_object_tagging(
            {"bucket": "b", "cos_key": "k", "tags": "only-one"},
            MOCK_GLOBALS,
        )

        # 标签格式错误 → 立即 return，不调用 put_object_tagging
        mock_client.put_object_tagging.assert_not_called()
        assert "Error:" in capsys.readouterr().out


class TestRestoreMoreBranches:

    def test_recursive_no_match(self, mock_client, patch_init_client, capsys):
        """Convey: 递归只有非归档对象 —— 全部 skip，统计数为 0"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a", "Size": "1", "StorageClass": "STANDARD"},
            ],
            "IsTruncated": "false",
        }

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        mock_client.restore_object.assert_not_called()
        out = capsys.readouterr().out
        assert "跳过 1" in out


class TestDuMoreBranches:

    def test_pagination_next_marker(self, mock_client, patch_init_client, capsys):
        """分页 NextMarker 分支"""
        mod = patch_init_client("du_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "a", "Size": "10", "StorageClass": "STANDARD"}],
             "IsTruncated": "true", "NextMarker": "a"},
            {"Contents": [], "IsTruncated": "false"},
        ]

        mod.du_object({"bucket": "b"}, MOCK_GLOBALS)

        assert mock_client.list_objects.call_count == 2


class TestAclMoreBranches:

    def test_get_bucket_acl_grant_is_single_dict(self, mock_client, patch_init_client, capsys):
        """Convey: Grant 为单个 dict（非 list）"""
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_bucket_acl.return_value = {
            "Owner": {"ID": "o", "DisplayName": "d"},
            "AccessControlList": {"Grant": {
                "Grantee": {"ID": "u1", "type": "CanonicalUser"},
                "Permission": "READ",
            }},
        }

        mod.get_bucket_acl({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "u1" in out and "READ" in out
