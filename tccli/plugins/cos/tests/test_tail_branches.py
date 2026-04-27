# -*- coding: utf-8 -*-
"""
收尾覆盖 —— 拉到 ≥98% 所需的最后几个分支。
"""
import os

from conftest import MOCK_GLOBALS, make_cos_error


# =============================================================
# upload_object 的空 cos_prefix 分支
# =============================================================

class TestUploadObjectEmptyCosPrefix:

    def test_recursive_empty_cos_prefix_file(self, mock_client, patch_init_client, tmp_path):
        """Convey: cos_key 为空字符串 + recursive —— 普通文件 key 直接为 rel_path"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")

        mod.upload_object(
            {"bucket": "b", "cos_key": "",
             "local_path": str(tmp_path) + "/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        keys = [c.kwargs["Key"] for c in mock_client.upload_file.call_args_list]
        assert keys == ["a.txt"]

    def test_recursive_empty_cos_prefix_empty_dir(self, mock_client, patch_init_client, tmp_path):
        """Convey: cos_key 为空字符串 + recursive —— 空目录 key = rel_dir + '/'"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "empty_dir").mkdir()

        mod.upload_object(
            {"bucket": "b", "cos_key": "",
             "local_path": str(tmp_path) + "/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        keys = [c.kwargs["Key"] for c in mock_client.put_object.call_args_list]
        assert keys == ["empty_dir/"]


# =============================================================
# sync_download_object 的 include/exclude 过滤 + 创建空目录
# =============================================================

class TestSyncDownloadFilterAndCreate:

    def test_include_filter_for_file(self, mock_client, patch_init_client, tmp_path):
        """Convey: COS 普通文件被 include 过滤掉"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 只 a.txt 被下载
        assert mock_client.download_file.call_count == 1

    def test_creates_cos_empty_dir_locally(self, mock_client, patch_init_client, tmp_path):
        """Convey: COS 上有 / 结尾空目录 + 本地不存在 → 本地创建"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/empty_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        # 空目录被创建到本地
        assert (tmp_path / "empty_dir").is_dir()


# =============================================================
# sync_copy_object 剩余：ignore_existing 为 True 但 dest 不存在（dest_head=None）
# =============================================================

class TestSyncCopyTopLevelExceptionOther:

    def test_generic_exception_not_captured_by_cos_error(self, mock_client, patch_init_client):
        """Convey: 顶层非 CosServiceError 异常会让函数直接抛出（顶层只捕获 CosServiceError）"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = RuntimeError("boom")

        # 不捕获 RuntimeError，函数会直接抛异常
        try:
            mod.sync_copy_object(
                {"bucket": "src", "cos_key": "p/",
                 "dest_bucket": "dst", "dest_key": "d/"},
                MOCK_GLOBALS,
            )
            assert False, "expected exception"
        except RuntimeError:
            pass


# =============================================================
# delete_bucket 剩余：多页 objects_versions 分页
# =============================================================

class TestDeleteBucketVersionPagination:

    def test_version_pagination(self, mock_client, patch_init_client):
        """Convey: list_objects_versions 分页（IsTruncated=true → false）"""
        mod = patch_init_client("delete_bucket", mock_client)

        mock_client.list_objects.return_value = {"Contents": [], "IsTruncated": "false"}
        mock_client.list_objects_versions.side_effect = [
            {"Version": [{"Key": "a", "VersionId": "v1"}],
             "DeleteMarker": [], "IsTruncated": "true",
             "NextKeyMarker": "a", "NextVersionIdMarker": "v1"},
            {"Version": [{"Key": "b", "VersionId": "v2"}],
             "DeleteMarker": [], "IsTruncated": "false"},
        ]
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [], "IsTruncated": "false",
        }

        mod.delete_bucket({"bucket": "b", "force": True}, MOCK_GLOBALS)

        # 两次 delete_objects（两页版本）
        assert mock_client.delete_objects.call_count == 2


# =============================================================
# lsparts 剩余：empty upload item 被跳过
# =============================================================

class TestLspartsEmptyItem:

    def test_empty_upload_item_skipped(self, mock_client, patch_init_client, capsys):
        """Convey: Upload 列表含空 item —— 代码用 `if not upload: continue` 防御，被跳过"""
        mod = patch_init_client("lsparts_object", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [
                None,
                {"Key": "a", "UploadId": "u1", "Initiated": "t1"},
            ],
            "IsTruncated": "false",
        }

        mod.lsparts_object({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "u1" in out
        # 只展示 1 条
        assert "共 1 个" in out


# =============================================================
# list_buckets 单桶 dict 分支
# =============================================================

class TestListBucketsSingleDict:

    def test_single_bucket_as_dict(self, mock_client, patch_init_client, capsys):
        """Convey: Bucket 为单 dict（非 list）"""
        mod = patch_init_client("list_buckets", mock_client)
        mock_client.list_buckets.return_value = {
            "Buckets": {"Bucket": {
                "Name": "only-125", "Location": "ap-guangzhou",
                "CreationDate": "2026-04-01T00:00:00Z",
            }},
        }

        mod.list_buckets({}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "only-125" in out
        assert "共 1 个存储桶" in out


# =============================================================
# list_object non-recursive pagination break 之后的统计行
# =============================================================

class TestListObjectTotalCount:

    def test_total_count_zero_no_output(self, mock_client, patch_init_client, capsys):
        """Convey: 非 recursive 且无 Contents —— 不输出统计行"""
        mod = patch_init_client("list_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

        mod.list_object({"bucket": "b"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "共 " not in out   # 不输出统计行（total_count 为 0 且非 recursive）


# =============================================================
# du_object：子目录标记（以 / 结尾、Size=0）被单独计数
# =============================================================

class TestDuObjectDirMarker:

    def test_dir_marker_counted(self, mock_client, patch_init_client, capsys):
        """Convey: / 结尾的目录对象被统计为文件夹数（不计入总大小）"""
        mod = patch_init_client("du_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/dir/", "Size": "0", "StorageClass": "STANDARD"},
                {"Key": "pre/dir/a.txt", "Size": "100", "StorageClass": "STANDARD"},
            ],
            "IsTruncated": "false",
        }

        mod.du_object({"bucket": "b", "prefix": "pre/"}, MOCK_GLOBALS)

        out = capsys.readouterr().out
        assert "总文件数: 1" in out
        assert "总文件夹数: 1" in out


# =============================================================
# abort_multipart 剩余：upload 中出现空条目被 continue
# =============================================================

class TestAbortMultipartEmptyItem:

    def test_empty_upload_item_continue(self, mock_client, patch_init_client):
        """Convey: Upload 中含空条目 → continue，不调用 abort"""
        mod = patch_init_client("abort_multipart", mock_client)
        mock_client.list_multipart_uploads.return_value = {
            "Upload": [None, {"Key": "a", "UploadId": "u1", "Initiated": "t"}],
            "IsTruncated": "false",
        }

        mod.abort_multipart({"bucket": "b"}, MOCK_GLOBALS)

        # 只 abort 非空条目
        assert mock_client.abort_multipart_upload.call_count == 1


# =============================================================
# acl_object：Grant list 中 grantee 含 ID 和 type 的两种分支
# =============================================================

class TestAclTypeBranches:

    def test_put_object_acl_with_grant_read(self, mock_client, patch_init_client):
        """Convey: put_object_acl 传 grant_read（显式走该分支）"""
        mod = patch_init_client("acl_object", mock_client)

        mod.put_object_acl(
            {"bucket": "b", "cos_key": "k",
             "grant_read": 'id="u1"',
             "grant_full_control": 'id="u2"'},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.put_object_acl.call_args.kwargs
        assert kwargs["GrantRead"] == 'id="u1"'
        assert kwargs["GrantFullControl"] == 'id="u2"'


# =============================================================
# copy_object 最后几行：dest_region 默认值
# =============================================================

class TestCopyDestRegionDefault:

    def test_dest_region_falls_back_to_src(self, mock_client, patch_init_client):
        """Convey: dest_region=None → 走 `or region` 回落到 src region"""
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "d",
             "dest_region": None},
            MOCK_GLOBALS,
        )

        # CopySource 的 Region 来自 src 的 ap-guangzhou
        source = mock_client.copy.call_args.kwargs["CopySource"]
        assert source["Region"] == "ap-guangzhou"


# =============================================================
# hash_object 剩余 17 行：crcmod 未安装时返回错误信息
# =============================================================

class TestHashObjectNoCrcmod:

    def test_crc64_without_crcmod(self, mock_client, patch_init_client, monkeypatch, capsys, tmp_path):
        """Convey: 本地 crc64 但 crcmod 未安装 —— 打印错误提示"""
        mod = patch_init_client("hash_object", mock_client)
        f = tmp_path / "a.txt"
        f.write_text("x")

        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **kw):
            if name == "crcmod":
                raise ImportError("no crcmod")
            return real_import(name, *a, **kw)

        monkeypatch.setattr(builtins, "__import__", fake_import)

        mod.hash_object(
            {"local_path": str(f), "hash_type": "crc64"},
            MOCK_GLOBALS,
        )

        assert "crcmod" in capsys.readouterr().out
