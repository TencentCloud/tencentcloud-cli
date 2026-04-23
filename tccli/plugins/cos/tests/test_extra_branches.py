# -*- coding: utf-8 -*-
"""
进一步补齐覆盖率：copy / download / delete_object / upload 的 recursive 分支、
空目录过滤、重试错误记录、顶层 CosServiceError、progress bar tick 打印等。
"""
import time

from conftest import MOCK_GLOBALS, make_cos_error
from tccli.plugins.cos import utils as _utils


# =============================================================
# copy_object 补充分支
# =============================================================

class TestCopyObjectMoreBranches:

    def test_single_storage_class_only(self, mock_client, patch_init_client):
        """Convey: 单文件 copy + 指定 storage_class（只进 storage_class 分支，不进 metadata 分支）"""
        mod = patch_init_client("copy_object", mock_client)

        mod.copy_object(
            {"bucket": "b", "cos_key": "a", "dest_key": "d",
             "storage_class": "ARCHIVE"},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.copy.call_args.kwargs
        assert kwargs["StorageClass"] == "ARCHIVE"
        assert "Metadata" not in kwargs

    def test_recursive_pagination(self, mock_client, patch_init_client):
        """Convey: recursive 分页（IsTruncated=true → false）"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "pre/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "true", "NextMarker": "pre/a.txt"},
            {"Contents": [{"Key": "pre/b.txt", "Size": "2",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
        ]

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/", "recursive": True},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2

    def test_recursive_empty_dir_excluded(self, mock_client, patch_init_client):
        """Convey: recursive 空目录被 include/exclude 过滤掉"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/", "recursive": True,
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # a.txt 被复制；excluded_dir/ 被 include 过滤，put_object 不被调用
        assert mock_client.copy.call_count == 1
        mock_client.put_object.assert_not_called()

    def test_recursive_retry_then_success(self, mock_client, patch_init_client):
        """Convey: recursive copy 重试 —— 子文件首次失败、第二次成功"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.copy.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            {},
        ]

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True, "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.copy.call_count == 2

    def test_recursive_retry_exhausted_logs_err(self, mock_client, patch_init_client):
        """Convey: recursive copy 重试耗尽 —— 子文件失败记录 err，整体不抛异常"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.copy.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/",
             "recursive": True, "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 -> 共 2 次尝试
        assert mock_client.copy.call_count == 2

    def test_recursive_empty_dir_put_fails(self, mock_client, patch_init_client):
        """Convey: recursive 空目录 put_object 失败 —— 记录 err 不中断"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/sub/", "Size": "0",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.put_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "PUT", 403,
        )

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/", "recursive": True},
            MOCK_GLOBALS,
        )

        mock_client.put_object.assert_called_once()

    def test_top_level_cos_error(self, mock_client, patch_init_client, capsys):
        """Convey: recursive 顶层 list_objects 抛 CosServiceError"""
        mod = patch_init_client("copy_object", mock_client)
        mock_client.list_objects.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "GET", 403,
        )

        mod.copy_object(
            {"bucket": "src", "cos_key": "pre/",
             "dest_bucket": "dst", "dest_key": "d/", "recursive": True},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


# =============================================================
# download_object 补充分支
# =============================================================

class TestDownloadObjectMoreBranches:

    def test_recursive_include_filters_file_and_dir(self, mock_client, patch_init_client, tmp_path):
        """Convey: include 同时过滤普通文件和 COS 上的空目录标记"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/b.log", "Size": "2",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True,
             "include": "*.txt"},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 1
        # excluded_dir 被过滤 → 不创建本地目录
        assert not (tmp_path / "excluded_dir").exists()

    def test_recursive_pagination(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive 分页"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.side_effect = [
            {"Contents": [{"Key": "pre/a.txt", "Size": "1",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "true", "NextMarker": "pre/a.txt"},
            {"Contents": [{"Key": "pre/b.txt", "Size": "2",
                           "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
             "IsTruncated": "false"},
        ]

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True},
            MOCK_GLOBALS,
        )

        assert mock_client.download_file.call_count == 2

    def test_recursive_retry_exhausted_logs_err(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive 单文件重试耗尽 → 记录 err，整体继续"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }
        mock_client.download_file.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "GET", 500,
        )

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True, "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 -> 共 2 次尝试
        assert mock_client.download_file.call_count == 2

    def test_single_head_fails_file_size_zero(self, mock_client, patch_init_client, tmp_path):
        """Convey: 单文件下载 head_object 失败 —— file_size 回退为 0，下载仍成功"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.head_object.side_effect = RuntimeError("boom")

        mod.download_object(
            {"bucket": "b", "cos_key": "k",
             "local_path": str(tmp_path / "dst.txt")},
            MOCK_GLOBALS,
        )

        mock_client.download_file.assert_called_once()

    def test_top_level_generic_exception(self, mock_client, patch_init_client, tmp_path, capsys):
        """Convey: 顶层非 CosServiceError 异常 —— Error: 打印"""
        mod = patch_init_client("download_object", mock_client)
        mock_client.list_objects.side_effect = RuntimeError("boom")

        mod.download_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path), "recursive": True},
            MOCK_GLOBALS,
        )

        assert "Error:" in capsys.readouterr().out


# =============================================================
# delete_object 补充分支
# =============================================================

class TestDeleteObjectMoreBranches:

    def test_recursive_dir_excluded_by_include(self, mock_client, patch_init_client):
        """Convey: 目录对象被 include 过滤 → skip"""
        mod = patch_init_client("delete_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/a.txt", "Size": "1",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
                {"Key": "pre/excluded_dir/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/",
             "recursive": True, "force": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 文件 a.txt 通过 delete_objects；目录 excluded_dir 被过滤 → delete_object 不调用
        mock_client.delete_object.assert_not_called()

    def test_recursive_dir_delete_retry(self, mock_client, patch_init_client):
        """Convey: 目录逐个 delete 的重试后成功"""
        mod = patch_init_client("delete_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/sub/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        mock_client.delete_object.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "DELETE", 500),
            {},
        ]

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/",
             "recursive": True, "force": True, "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.delete_object.call_count == 2

    def test_recursive_dir_delete_retry_exhausted(self, mock_client, patch_init_client):
        """Convey: 目录 delete 重试耗尽 → 记录 err，不抛异常"""
        mod = patch_init_client("delete_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/sub/", "Size": "0",
                 "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'},
            ],
            "IsTruncated": "false",
        }
        mock_client.delete_object.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "DELETE", 500,
        )

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/",
             "recursive": True, "force": True, "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 -> 共 2 次尝试
        assert mock_client.delete_object.call_count == 2

    def test_recursive_confirm_eof(self, mock_client, patch_init_client, monkeypatch, capsys):
        """Convey: input 抛 EOFError —— 取消删除"""
        mod = patch_init_client("delete_object", mock_client)
        mock_client.list_objects.return_value = {
            "Contents": [{"Key": "pre/a.txt", "Size": "1",
                          "LastModified": "", "StorageClass": "STANDARD", "ETag": '"e"'}],
            "IsTruncated": "false",
        }

        def _raise_eof(*_a, **_k):
            raise EOFError()

        monkeypatch.setattr("builtins.input", _raise_eof)

        mod.delete_object(
            {"bucket": "b", "cos_key": "pre/", "recursive": True, "force": False},
            MOCK_GLOBALS,
        )

        mock_client.delete_objects.assert_not_called()
        assert "已取消删除" in capsys.readouterr().out


# =============================================================
# upload_object 补充分支
# =============================================================

class TestUploadObjectMoreBranches:

    def test_recursive_empty_dir_put_fails(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive 空目录 put_object 失败 —— 记录 err"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "empty").mkdir()
        mock_client.put_object.side_effect = make_cos_error(
            "AccessDenied", "denied", "r1", "PUT", 403,
        )

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/", "recursive": True},
            MOCK_GLOBALS,
        )

        mock_client.put_object.assert_called()

    def test_recursive_include_filter_skips_file(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive include 过滤跳过文件"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.log").write_text("b")

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        assert mock_client.upload_file.call_count == 1
        assert mock_client.upload_file.call_args.kwargs["Key"] == "pre/a.txt"

    def test_recursive_empty_dir_match_filter(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive 空目录被 exclude 过滤跳过"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "keep_dir").mkdir()
        (tmp_path / "excluded_dir").mkdir()

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True, "exclude": "excluded_dir"},
            MOCK_GLOBALS,
        )

        # keep_dir 对应 put_object 被调用，excluded_dir 不被调用
        keys = [c.kwargs["Key"] for c in mock_client.put_object.call_args_list]
        assert any("keep_dir" in k for k in keys)
        assert not any("excluded_dir" in k for k in keys)

    def test_recursive_retry_exhausted(self, mock_client, patch_init_client, tmp_path):
        """Convey: recursive 重试耗尽 —— 记录 err，整体不抛异常"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        mock_client.upload_file.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True, "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 -> 2 次尝试
        assert mock_client.upload_file.call_count == 2

    def test_cos_prefix_without_trailing_slash(self, mock_client, patch_init_client, tmp_path):
        """Convey: cos_prefix 不以 / 结尾时的 key 拼接分支"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")

        mod.upload_object(
            {"bucket": "b", "cos_key": "prefix",   # 不以 / 结尾
             "local_path": str(tmp_path) + "/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # 因为 local_path 以 / 结尾，所以不保留顶层目录名；cos_key "prefix" 内部会按
        # 分支 "cos_prefix + '/' + rel_path" 拼接
        keys = [c.kwargs["Key"] for c in mock_client.upload_file.call_args_list]
        assert keys == ["prefix/a.txt"]


# =============================================================
# utils.TransferProgressMonitor —— 进度条 tick 打印
# =============================================================

class TestProgressBarTick:

    def test_progress_bar_triggers_tick_print(self, tmp_path):
        """走一下 _progress_loop 让 _print_progress_bar 实际被触发打印（不只默认构造）。"""
        m = _utils.TransferProgressMonitor("upload")
        # 缩短 tick 间隔，确保 _print_progress_bar 能被调用到打印分支
        m._tick_duration = 0.01
        m.set_scan_info(1, 100)
        m.start()
        # 模拟进度前进
        cb, fid = m.create_progress_callback(100)
        cb(50, 100)
        # 稍微等待 tick
        time.sleep(0.05)
        cb(100, 100)
        m.update_ok(100, fid)
        m.stop()

    def test_progress_bar_scan_not_finished(self, tmp_path):
        """scan_end=False 时（未调用 set_scan_info）会走另一个分支"""
        m = _utils.TransferProgressMonitor("copy")
        m._tick_duration = 0.01
        m.start()
        m.update_ok(10)   # 不设置 scan_info
        time.sleep(0.05)
        m.stop()

    def test_finish_bar_with_total_size_but_err(self):
        """_print_finish_bar：有 total_size 且存在 err_num → 走 percent 分支"""
        m = _utils.TransferProgressMonitor("download")
        m.set_scan_info(2, 200)
        m.update_ok(100)
        m.update_err(path="/x", reason="fail")
        m._print_finish_bar()   # 直接调用确保覆盖分支
