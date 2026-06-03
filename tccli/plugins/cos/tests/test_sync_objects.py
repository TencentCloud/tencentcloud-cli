# -*- coding: utf-8 -*-
"""
sync_upload / sync_download / sync_copy 单测
—— 对齐 coscli cmd/sync_test.go 的 Upload / Download / CosCopy 分支。

重点覆盖跳过逻辑（对齐 coscli sync）：
  1) 默认：CRC64（x-cos-hash-crc64ecma）相等则跳过
  2) --ignore-existing：目标存在即跳过
  3) --update：Last-Modified 时间比较

以及 --delete（删除目标端多余）。
"""
import os

from tccli.plugins.cos.utils import calculate_local_crc64

from conftest import MOCK_GLOBALS, make_cos_error


# ========================================================
# sync_upload
# ========================================================

class TestSyncUpload:

    def _setup_empty_cos(self, mock_client):
        mock_client.list_objects.return_value = {
            "Contents": [], "IsTruncated": "false",
        }

    def test_local_path_not_directory(self, mock_client, patch_init_client, capsys):
        """本地路径必须是目录"""
        mod = patch_init_client("sync_upload_object", mock_client)

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": "/tmp/tccli-cos-sync-upload-not-exist"},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()
        assert "本地路径不是目录" in capsys.readouterr().out

    def test_sync_empty_target_uploads_all(self, mock_client, patch_init_client, tmp_path):
        """COS 端为空 —— 全部上传"""
        mod = patch_init_client("sync_upload_object", mock_client)
        self._setup_empty_cos(mock_client)
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.txt").write_text("bb")

        mod.sync_upload_object(
            {"bucket": "b-1250000000", "cos_key": "pre/",
             "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        assert mock_client.upload_file.call_count == 2

    def test_skip_by_crc64(self, mock_client, patch_init_client, tmp_path):
        """Convey: 默认跳过规则 —— 本地 CRC64 与 COS x-cos-hash-crc64ecma 相等则跳过"""
        mod = patch_init_client("sync_upload_object", mock_client)
        local = tmp_path / "a.txt"
        local.write_text("hello")

        local_crc = calculate_local_crc64(str(local))
        # 必须有 CRC64 环境（crcmod 可用），否则跳过逻辑会 fallback 为"不跳过"
        assert local_crc is not None, "单测环境缺少 crcmod，请先安装"

        # list_objects 列出对应 key
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "5",
                          "LastModified": "Mon, 07 Apr 2026 06:00:00 GMT",
                          "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        # should_skip_sync_upload 内部会 head_object
        mock_client.head_object.return_value = {
            "Content-Length": "5",
            "x-cos-hash-crc64ecma": local_crc,
            "Last-Modified": "Mon, 07 Apr 2026 06:00:00 GMT",
        }

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()

    def test_skip_by_ignore_existing(self, mock_client, patch_init_client, tmp_path):
        """Convey: --ignore-existing 目标存在即跳过"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("x")

        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.head_object.return_value = {"Content-Length": "1"}

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "ignore_existing": True},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()

    def test_skip_by_update(self, mock_client, patch_init_client, tmp_path):
        """Convey: --update 目标比本地新则跳过"""
        mod = patch_init_client("sync_upload_object", mock_client)
        local = tmp_path / "a.txt"
        local.write_text("x")
        # 把本地 mtime 设为一个很早的时间戳（2020 年）
        old_ts = 1577836800.0   # 2020-01-01 00:00:00 UTC
        os.utime(str(local), (old_ts, old_ts))

        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "Sun, 07 Apr 2030 06:00:00 GMT",
                          "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.head_object.return_value = {
            "Content-Length": "1",
            "Last-Modified": "Sun, 07 Apr 2030 06:00:00 GMT",  # 远比本地新
        }

        mod.sync_upload_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "update": True},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()

    def test_delete_extra(self, mock_client, patch_init_client, tmp_path):
        """Convey: --delete 删除 COS 上多余的对象"""
        mod = patch_init_client("sync_upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")

        # 第一次 list_objects（list_all_objects，不含目录）返回 orphan + a.txt
        # 第二次 list_objects（list_all_objects_with_dirs，含目录）同样返回这两个
        listing = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/orphan.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        mock_client.list_objects.return_value = listing
        # 目标存在 + CRC 不同 → 不跳过，仍需上传
        mock_client.head_object.return_value = {
            "Content-Length": "1", "x-cos-hash-crc64ecma": "0",
        }

        mod.sync_upload_object(
            {"bucket": "b-1250000000", "cos_key": "pre/",
             "local_path": str(tmp_path), "delete": True},
            MOCK_GLOBALS,
        )

        # orphan.log 应被删除
        delete_keys = [c.kwargs["Key"] for c in mock_client.delete_object.call_args_list]
        assert "pre/orphan.log" in delete_keys


# ========================================================
# sync_download
# ========================================================

class TestSyncDownload:

    def test_sync_download_all(self, mock_client, patch_init_client, tmp_path):
        """COS 有文件，本地为空 —— 全部下载"""
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "Mon, 07 Apr 2026 06:00:00 GMT",
                 "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "Mon, 07 Apr 2026 06:00:01 GMT",
                 "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 2

    def test_skip_by_ignore_existing(self, mock_client, patch_init_client, tmp_path):
        """--ignore-existing：本地存在即跳过"""
        mod = patch_init_client("sync_download_object", mock_client)
        (tmp_path / "a.txt").write_text("x")   # 本地已存在

        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "Mon, 07 Apr 2026 06:00:00 GMT",
                          "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "ignore_existing": True},
            MOCK_GLOBALS,
        )

        mock_client.download_file.assert_not_called()

    def test_skip_by_crc64(self, mock_client, patch_init_client, tmp_path):
        """默认：本地 CRC64 == COS x-cos-hash-crc64ecma → 跳过"""
        mod = patch_init_client("sync_download_object", mock_client)
        local = tmp_path / "a.txt"
        local.write_text("hello")
        local_crc = calculate_local_crc64(str(local))
        assert local_crc is not None

        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "5",
                          "LastModified": "Mon, 07 Apr 2026 06:00:00 GMT",
                          "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.head_object.return_value = {
            "x-cos-hash-crc64ecma": local_crc,
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        mock_client.download_file.assert_not_called()

    def test_delete_extra_local(self, mock_client, patch_init_client, tmp_path):
        """--delete：删除本地多余文件"""
        mod = patch_init_client("sync_download_object", mock_client)
        # 本地 orphan 存在但 COS 没有
        (tmp_path / "orphan.txt").write_text("x")

        mock_client.list_objects.return_value = {
            "Contents": [],
            "IsTruncated": "false",
        }

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path),
             "delete": True},
            MOCK_GLOBALS,
        )

        assert not os.path.exists(tmp_path / "orphan.txt")

    def test_sdk_error(self, mock_client, patch_init_client, tmp_path, capsys):
        mod = patch_init_client("sync_download_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )

        mod.sync_download_object(
            {"bucket": "b", "cos_key": "pre/", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


# ========================================================
# sync_copy
# ========================================================

class TestSyncCopy:

    def test_empty_src(self, mock_client, patch_init_client):
        """源端为空 —— 什么也不做"""
        mod = patch_init_client("sync_copy_object", mock_client)

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_not_called()

    def test_copy_all(self, mock_client, patch_init_client):
        """源端有文件 → 目标端全复制"""
        mod = patch_init_client("sync_copy_object", mock_client)
        # list_all_objects_with_dirs（源） + list_all_objects（目标，空）
        # 两次调用返回不同数据，用 side_effect 模拟
        mock_client.list_objects.side_effect = [
            # 源：含一个文件 + 一个目录
            {"Contents": [
                {"Key": "p/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "p/sub/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ], "IsTruncated": "false"},
            # 目标：空
            {"Contents": [], "IsTruncated": "false"},
        ]

        mod.sync_copy_object(
            {"bucket": "src-125", "cos_key": "p/",
             "dest_bucket": "dst-125", "dest_key": "d/"},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_called_once()
        copy_kwargs = mock_client.copy.call_args.kwargs
        assert copy_kwargs["Bucket"] == "dst-125"
        assert copy_kwargs["Key"] == "d/a.txt"
        # 空目录在目标端 put_object 创建
        mock_client.put_object.assert_called()

    def test_skip_by_ignore_existing(self, mock_client, patch_init_client):
        """目标存在 + --ignore-existing → 跳过"""
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            # 源
            {"Contents": [{"Key": "p/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
            # 目标（已有 d/a.txt）
            {"Contents": [{"Key": "d/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
        ]
        # should_skip_sync_copy 会 head_object 目标
        mock_client.head_object.return_value = {"Content-Length": "1"}

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/",
             "ignore_existing": True},
            MOCK_GLOBALS,
        )

        mock_client.copy.assert_not_called()

    def test_delete_extra(self, mock_client, patch_init_client):
        """--delete：删除目标端多余对象"""
        mod = patch_init_client("sync_copy_object", mock_client)

        # list_all_objects_with_dirs(源) / list_all_objects(目标) / list_all_objects_with_dirs(目标 - for delete)
        src = {"Contents": [
            {"Key": "p/a.txt", "Size": "1",
             "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false"}
        dest = {"Contents": [
            {"Key": "d/orphan.log", "Size": "2",
             "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            {"Key": "d/a.txt", "Size": "1",
             "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false"}
        mock_client.list_objects.side_effect = [src, dest, dest]
        # 目标 a.txt 与源 CRC 对不上 → 仍需复制；但 orphan 会被删
        mock_client.head_object.return_value = {
            "Content-Length": "1", "x-cos-hash-crc64ecma": "0",
        }

        mod.sync_copy_object(
            {"bucket": "src", "cos_key": "p/",
             "dest_bucket": "dst", "dest_key": "d/", "delete": True},
            MOCK_GLOBALS,
        )

        delete_keys = [c.kwargs["Key"] for c in mock_client.delete_object.call_args_list]
        assert "d/orphan.log" in delete_keys

    def test_sdk_error(self, mock_client, patch_init_client, capsys):
        mod = patch_init_client("sync_copy_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "AccessDenied", "denied", "req-1", "GET", 403,
        )

        mod.sync_copy_object(
            {"bucket": "b", "cos_key": "p/",
             "dest_bucket": "d", "dest_key": "d/"},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out
