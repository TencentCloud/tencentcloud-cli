# -*- coding: utf-8 -*-
"""
补充覆盖率测试 —— 针对各命令文件中覆盖率偏低的分支。

按命令分组组织；用例命名对齐 coscli Convey 子场景。
"""
import os

from conftest import MOCK_GLOBALS, make_cos_error


# =============================================================
# move_object 递归空目录
# =============================================================

class TestMoveRecursiveEmptyDir:

    def _setup(self, mock_client, patch_init_client, include="", exclude=""):
        mod = patch_init_client("move_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/sub/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/excluded/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        return mod

    def test_success_move_dir_markers(self, mock_client, patch_init_client):
        """Convey: move 空目录对象 —— 创建目标 + 删除源"""
        mod = self._setup(mock_client, patch_init_client)

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # a.txt 的 copy + delete
        # sub/、excluded/ 两个空目录各一次 put_object
        # 源文件 + 两个源目录共 3 次 delete_object
        assert mock_client.put_object.call_count == 2
        assert mock_client.delete_object.call_count == 3

    def test_put_object_fails(self, mock_client, patch_init_client):
        """Convey: 创建目标文件夹失败 —— 不继续 delete 源"""
        mod = self._setup(mock_client, patch_init_client)
        mock_client.put_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "PUT", 403,
        )

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # 2 次尝试创建目录都失败 → 不应调用源目录 delete
        # 只有 a.txt 的 delete_object（由 _do_move 内部发起）
        assert mock_client.put_object.call_count == 2
        assert mock_client.delete_object.call_count == 1

    def test_delete_src_dir_fails(self, mock_client, patch_init_client):
        """Convey: 删除源文件夹失败 —— 记录 err 但继续"""
        mod = self._setup(mock_client, patch_init_client)

        # delete_object 在处理 pre/sub/ 时抛 CosServiceError
        def _delete_side(**kwargs):
            if kwargs.get("Key", "").endswith("sub/"):
                raise make_cos_error("AccessDenied", "denied", "r1", "DELETE", 403)
            return {}

        mock_client.delete_object.side_effect = _delete_side

        mod.move_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # put_object 成功 2 次（sub、excluded 两个空目录）
        assert mock_client.put_object.call_count == 2

    def test_recursive_include_filter(self, mock_client, patch_init_client):
        """include 过滤 —— 只移动 *.txt，目录 skip"""
        mod = patch_init_client("move_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
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

        # 只有 a.txt 被复制/删除
        assert mock_client.copy.call_count == 1
        assert mock_client.copy.call_args.kwargs["Key"] == "d/a.txt"


# =============================================================
# sync_upload_object 补充分支
# =============================================================

class TestSyncUploadExtraBranches:

    def test_storage_class_meta_content_type_rate_limiting(self, mock_client, patch_init_client, tmp_path):
        """Convey: 透传 storage_class/meta/content_type/rate_limiting"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "storage_class": "STANDARD_IA", "content_type": "text/plain",
             "meta": "env=prod", "rate_limiting": 2},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_called_once()
        kwargs = mock_client.upload_file.call_args.kwargs
        assert kwargs["StorageClass"] == "STANDARD_IA"
        assert kwargs["ContentType"] == "text/plain"
        assert kwargs["Metadata"] == {"x-cos-meta-env": "prod"}
        assert kwargs["TrafficLimit"] == str(2 * 1024 * 1024 * 8)

    def test_retry_resets_progress_callback(self, mock_client, patch_init_client, tmp_path):
        """Convey: retry 后必须重置 progress_callback 并成功"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }
        mock_client.upload_file.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            None,
        ]

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path), "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.upload_file.call_count == 2

    def test_empty_dir_upload_error_recorded(self, mock_client, patch_init_client, tmp_path):
        """Convey: 空目录标记创建失败时记录 err，不中断流程"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "empty_dir").mkdir()
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }
        mock_client.put_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "PUT", 403,
        )

        # 不应抛异常
        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        mock_client.put_object.assert_called()

    def test_delete_extra_dir_and_file(self, mock_client, patch_init_client, tmp_path, capsys):
        """Convey: --delete 删除 COS 上的多余文件 + 多余目录"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")

        # list_all_objects（不含目录）→ 用于扫描+跳过判断
        # list_all_objects_with_dirs（含目录）→ 用于 delete 多余扫描
        listing_no_dirs = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/orphan.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        listing_with_dirs = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/orphan.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/orphan_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        # list_objects 依次用于 list_all_objects(含跳过)、list_all_objects_with_dirs(delete)
        mock_client.list_objects.side_effect = [listing_no_dirs, listing_with_dirs]
        # head_object 不返回 CRC —— 本地 a.txt 与 COS 一致性判断返回"不跳过"
        mock_client.head_object.return_value = {"x-cos-hash-crc64ecma": ""}

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "delete": True},
            MOCK_GLOBALS,
        )

        delete_keys = [c.kwargs["Key"] for c in mock_client.delete_object.call_args_list]
        # orphan.txt 与 orphan_dir/ 都应被删除
        assert "pre/orphan.txt" in delete_keys
        assert "pre/orphan_dir/" in delete_keys
        assert "已删除 COS 上多余文件" in capsys.readouterr().out

    def test_top_level_cos_error_captured(self, mock_client, patch_init_client, tmp_path, capsys):
        """Convey: list_all_objects 抛 CosServiceError —— 顶层 except 捕获并打印"""
        mod = patch_init_client("sync_upload_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "GET", 403,
        )

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


# =============================================================
# sync_download_object 补充分支
# =============================================================

class TestSyncDownloadExtraBranches:

    def test_cos_empty_dir_include_filter(self, mock_client, patch_init_client, tmp_path):
        """Convey: COS 空目录被 include/exclude 过滤掉"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                # 空目录标记 —— 不匹配 include *.txt 被跳过
                {"Key": "pre/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                # 正常文件
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 仅 a.txt 被下载
        assert mock_client.download_file.call_count == 1
        # excluded_dir 被跳过 → 本地不会出现
        assert not (tmp_path / "excluded_dir").exists()

    def test_retry_then_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: download 重试后成功"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.download_file.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "GET", 500),
            None,
        ]

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path), "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 2

    def test_rate_limiting_passed(self, mock_client, patch_init_client, tmp_path):
        """Convey: rate_limiting 参数被透传为 TrafficLimit (bit/s)"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "rate_limiting": 3},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.download_file.call_args.kwargs
        assert kwargs["TrafficLimit"] == str(3 * 1024 * 1024 * 8)

    def test_delete_extra_removes_empty_local_dirs(self, mock_client, patch_init_client, tmp_path):
        """Convey: --delete 删除本地多余文件后，空目录也被清理"""
        mod = patch_init_client("sync_download_object", mock_client)
        # 本地有 orphan 子目录 + 孤儿文件；COS 上全无
        orphan_dir = tmp_path / "orphan_dir"
        orphan_dir.mkdir()
        (orphan_dir / "x.txt").write_text("x")
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "delete": True},
            MOCK_GLOBALS,
        )

        # 孤儿文件已删除，空目录也被 rmdir
        assert not orphan_dir.exists()


# =============================================================
# sync_copy_object 补充分支
# =============================================================

class TestSyncCopyExtraBranches:

    def test_storage_class_and_meta(self, mock_client, patch_init_client):
        """Convey: storage_class + meta 透传（使用 CopyStatus=Replaced）"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "p/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
            {"Contents": [], "IsTruncated": "false"},
        ]

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/",
             "storage_class": "ARCHIVE",
             "meta": "env=prod"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["StorageClass"] == "ARCHIVE"
        assert kwargs["Metadata"] == {"x-cos-meta-env": "prod"}
        assert kwargs["CopyStatus"] == "Replaced"

    def test_empty_dir_put_object_fails(self, mock_client, patch_init_client):
        """Convey: 空目录 put_object 失败 —— 记录 err 不中断"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "p/sub/", "Size": "0",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
            {"Contents": [], "IsTruncated": "false"},
        ]
        mock_client.put_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "PUT", 403,
        )

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/"},
            MOCK_GLOBALS,
        )

        mock_client.put_object.assert_called_once()

    def test_retry_copy_success(self, mock_client, patch_init_client):
        """Convey: copy 重试后成功"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "p/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
            {"Contents": [], "IsTruncated": "false"},
        ]
        mock_client.copy.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            {},
        ]

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/", "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2


# =============================================================
# cat_object 非文本分支
# =============================================================

class TestCatObjectBinary:

    def test_non_utf8_content(self, mock_client, patch_init_client, capsys):
        """Convey: 非 UTF-8 编码 —— 以十六进制显示"""
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.return_value = {"Content-Length": "4"}

        body_stream = mock_client.get_object.return_value["Body"]
        # 非 UTF-8 字节
        body_stream.get_raw_stream.return_value.read.return_value = b"\xff\xfe\xfd\xfc"

        mod.cat_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "十六进制" in out
        assert "fffefdfc" in out

    def test_binary_long_content(self, mock_client, patch_init_client, capsys):
        """Convey: >1024 字节的二进制文件，尾部显示剩余字节数"""
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.return_value = {"Content-Length": "2000"}

        body_stream = mock_client.get_object.return_value["Body"]
        body_stream.get_raw_stream.return_value.read.return_value = b"\xff" * 2000

        mod.cat_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "共 2000 字节" in out

    def test_generic_exception(self, mock_client, patch_init_client, capsys):
        """Convey: 其他 Exception 被 Error: 打印（比如 head_object 返回无效 Content-Length）"""
        mod = patch_init_client("cat_object", mock_client)
        mock_client.head_object.side_effect = RuntimeError("boom")

        mod.cat_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "Error:" in capsys.readouterr().out


# =============================================================
# restore_object 补充分支
# =============================================================

class TestRestoreObjectExtraBranches:

    def test_recursive_already_in_progress(self, mock_client, patch_init_client, capsys):
        """Convey: 递归 —— 子对象已在进行中"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a", "Size": "1", "StorageClass": "ARCHIVE"},
            ],
            "IsTruncated": "false",
        }
        mock_client.restore_object.side_effect = make_cos_error(
            "RestoreAlreadyInProgress", "in progress", "r1", "POST", 409,
        )

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        out = capsys.readouterr().out
        assert "恢复进行中" in out

    def test_recursive_other_error(self, mock_client, patch_init_client, capsys):
        """Convey: 递归 —— 普通失败计数"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a", "Size": "1", "StorageClass": "ARCHIVE"},
            ],
            "IsTruncated": "false",
        }
        mock_client.restore_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "POST", 403,
        )

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        assert "恢复失败" in capsys.readouterr().out

    def test_recursive_skip_by_include(self, mock_client, patch_init_client, capsys):
        """Convey: include 过滤不匹配的归档对象被跳过"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.log", "Size": "1", "StorageClass": "ARCHIVE"},
                {"Key": "pre/b.txt", "Size": "2", "StorageClass": "ARCHIVE"},
            ],
            "IsTruncated": "false",
        }

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 只 b.txt 触发 restore_object
        assert mock_client.restore_object.call_count == 1

    def test_recursive_pagination(self, mock_client, patch_init_client):
        """Convey: 递归分页"""
        mod = patch_init_client("restore_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "pre/a", "Size": "1", "StorageClass": "ARCHIVE"}],
             "IsTruncated": "true", "NextMarker": "pre/a"},
            {"Contents": [{"Key": "pre/b", "Size": "1", "StorageClass": "ARCHIVE"}],
             "IsTruncated": "false"},
        ]

        mod.restore_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True},
            MOCK_GLOBALS,
        )

        assert mock_client.restore_object.call_count == 2


# =============================================================
# delete_bucket 补充分支
# =============================================================

class TestDeleteBucketExtraBranches:

    def test_force_versions_list_error_is_ignored(self, mock_client, patch_init_client, capsys):
        """Convey: list_objects_versions 抛 CosServiceError —— 忽略，继续清理分片"""
        mod = patch_init_client("delete_bucket", mock_client)

        mock_client.list_objects.return_value = {"Contents": [], "IsTruncated": "false"}
        mock_client.list_objects_versions.side_effect = make_cos_error(
            "VersioningNotEnabled", "n/a", "r1", "GET", 400,
        )
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [], "IsTruncated": "false",
        }

        mod.delete_bucket({"bucket": "b", "force": True}, MOCK_GLOBALS)

        mock_client.delete_bucket.assert_called_once()
        assert "存储桶删除成功" in capsys.readouterr().out

    def test_force_multi_page(self, mock_client, patch_init_client):
        """Convey: force 清理分页场景（IsTruncated=true → false）"""
        mod = patch_init_client("delete_bucket", mock_client)

        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "a"}], "IsTruncated": "true", "NextMarker": "a"},
            {"Contents": [{"Key": "b"}], "IsTruncated": "false"},
        ]
        mock_client.list_objects_versions.return_value = {
            "Version": [], "DeleteMarker": [], "IsTruncated": "false",
        }
        mock_client.list_multipart_uploads.side_effect = [
            {"Upload": [{"Key": "u1", "UploadId": "up1"}],
             "IsTruncated": "true", "NextKeyMarker": "u1", "NextUploadIdMarker": "up1"},
            {"Upload": [{"Key": "u2", "UploadId": "up2"}],
             "IsTruncated": "false"},
        ]

        mod.delete_bucket({"bucket": "b", "force": True}, MOCK_GLOBALS)

        # 两批对象各一次 delete_objects
        assert mock_client.delete_objects.call_count == 2
        # 两次 abort
        assert mock_client.abort_multipart_upload.call_count == 2


# =============================================================
# hash_object 补充分支
# =============================================================

class TestHashObjectExtraBranches:

    def test_local_crc64(self, mock_client, patch_init_client, capsys, tmp_path):
        """Convey: 计算本地 crc64"""
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_text("hello")

        mod.hash_object(
            {"local_path": str(f), "hash_type": "crc64"},
            MOCK_GLOBALS,
        )

        out = capsys.readouterr().out
        assert "CRC64" in out

    def test_local_sha1(self, mock_client, patch_init_client, capsys, tmp_path):
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_bytes(b"")  # 空文件的 sha1

        mod.hash_object(
            {"local_path": str(f), "hash_type": "sha1"},
            MOCK_GLOBALS,
        )
        # 空文件 sha1 = da39a3ee5e6b4b0d3255bfef95601890afd80709
        assert "da39a3ee5e6b4b0d3255bfef95601890afd80709" in capsys.readouterr().out

    def test_local_unsupported_hash_type(self, mock_client, patch_init_client, capsys, tmp_path):
        """Convey: 不支持的哈希类型"""
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_text("hi")

        mod.hash_object(
            {"local_path": str(f), "hash_type": "sha512"},
            MOCK_GLOBALS,
        )

        assert "不支持的哈希类型" in capsys.readouterr().out

    def test_local_path_is_dir(self, mock_client, patch_init_client, capsys, tmp_path):
        mod = patch_init_client("hash_object", mock_client)

        mod.hash_object({"local_path": str(tmp_path)}, MOCK_GLOBALS)

        assert "指定路径不是文件" in capsys.readouterr().out


# =============================================================
# acl_object 补充分支
# =============================================================

class TestAclObjectExtraBranches:

    def test_get_bucket_acl_uri_grantee(self, mock_client, patch_init_client, capsys):
        """Convey: URI grantee 输出分支"""
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_bucket_acl.return_value = {
            "Owner": {"ID": "o", "DisplayName": "d"},
            "AccessControlList": {"Grant": {
                "Grantee": {"URI": "http://cam.qcloud.com/groups/global/AllUsers"},
                "Permission": "READ",
            }},
        }

        mod.get_bucket_acl({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "URI" in out
        assert "AllUsers" in out

    def test_get_object_acl_uri_grantee(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("acl_object", mock_client)
        mock_client.get_object_acl.return_value = {
            "Owner": {"ID": "o", "DisplayName": "d"},
            "AccessControlList": {"Grant": {
                "Grantee": {"URI": "http://cam.qcloud.com/groups/global/AllUsers"},
                "Permission": "READ",
            }},
        }

        mod.get_object_acl({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "URI" in capsys.readouterr().out


# =============================================================
# abort_multipart 补充：abort_multipart_upload 指定单个 upload_id 时出错
# =============================================================

class TestAbortMultipartExtraBranches:

    def test_abort_single_upload_id_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.abort_multipart_upload.side_effect = make_cos_error(
            "NoSuchUpload", "no upload", "r1", "DELETE", 404,
        )

        mod.abort_multipart(
            {"bucket": "b", "cos_key": "k", "upload_id": "up1"},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out

    def test_abort_pagination(self, mock_client, patch_init_client, capsys):
        """Convey: abort 分页列举"""
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.side_effect = [
            {"Upload": [{"Key": "a", "UploadId": "u1", "Initiated": "t1"}],
             "IsTruncated": "true", "NextKeyMarker": "a", "NextUploadIdMarker": "u1"},
            {"Upload": [{"Key": "b", "UploadId": "u2", "Initiated": "t2"}],
             "IsTruncated": "false"},
        ]

        mod.abort_multipart({"bucket": "b"}, MOCK_GLOBALS)

        assert mock_client.abort_multipart_upload.call_count == 2


# =============================================================
# list_object / list_buckets 补充
# =============================================================

class TestListExtraBranches:

    def test_list_non_recursive_pagination(self, mock_client, patch_init_client, capsys):
        """Convey: 非递归模式下分页被截断提示"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "a", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "true",
            "NextMarker": "a",
        }

        mod.list_object({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "结果已截断" in out

    def test_list_buckets_sdk_error(self, mock_client, patch_init_client, capsys):
        """list_buckets SDK 错误分支（再次覆盖通用 except 路径）"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "GET", 500,
        )
        mod.list_buckets({}, MOCK_GLOBALS)
        assert "Error:" in capsys.readouterr().out


# =============================================================
# signurl 其它 HTTP 方法分支
# =============================================================

class TestSignurlExtraBranches:

    def test_other_method(self, mock_client, patch_init_client, capsys):
        """Convey: 除 GET/PUT 外的其他 method（如 HEAD/DELETE）"""
        mod = patch_init_client("signurl_object", mock_client)
        mock_client.get_presigned_url.return_value = "https://signed-delete"

        mod.signurl_object(
            {"bucket": "b", "cos_key": "k", "method": "DELETE", "expired": 60},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.get_presigned_url.call_args.kwargs
        assert kwargs["Method"] == "DELETE"
        assert "https://signed-delete" in capsys.readouterr().out

    def test_generic_exception(self, mock_client, patch_init_client, capsys):
        """Convey: 非 CosServiceError 异常（Exception 分支）"""
        mod = patch_init_client("signurl_object", mock_client)
        mock_client.get_presigned_download_url.side_effect = RuntimeError("boom")

        mod.signurl_object({"bucket": "b", "cos_key": "k"}, MOCK_GLOBALS)

        assert "Error: boom" in capsys.readouterr().out


# =============================================================
# du_object 分页
# =============================================================

class TestDuObjectExtraBranches:

    def test_pagination(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("du_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "a", "Size": "100", "StorageClass": "STANDARD"}],
             "IsTruncated": "true", "NextMarker": "a"},
            {"Contents": [{"Key": "b", "Size": "200", "StorageClass": "STANDARD"}],
             "IsTruncated": "false"},
        ]

        mod.du_object({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "总文件数: 2" in out
        assert "300 字节" in out


# =============================================================
# lsparts 分页
# =============================================================

class TestLspartsExtraBranches:

    def test_pagination(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.side_effect = [
            {"Upload": [{"Key": "a", "UploadId": "u1", "Initiated": "t1"}],
             "IsTruncated": "true", "NextKeyMarker": "a", "NextUploadIdMarker": "u1"},
            {"Upload": [{"Key": "b", "UploadId": "u2", "Initiated": "t2"}],
             "IsTruncated": "false"},
        ]

        mod.lsparts_object({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "u1" in out and "u2" in out
        assert "共 2 个" in out
