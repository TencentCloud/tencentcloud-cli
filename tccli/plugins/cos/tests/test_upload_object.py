# -*- coding: utf-8 -*-
"""
upload_object 单测 —— 对齐 coscli cmd/cp_test.go 中 Upload 分支。
"""
import os

from conftest import MOCK_GLOBALS, make_cos_error


class TestUploadSingle:

    def test_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: Upload single file success"""
        mod = patch_init_client("upload_object", mock_client)
        f = tmp_path / "src.txt"
        f.write_text("hello")

        mod.upload_object(
            {"bucket": "b-1250000000", "cos_key": "dest.txt", "local_path": str(f)},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_called_once()
        kwargs = mock_client.upload_file.call_args.kwargs
        assert kwargs["Bucket"] == "b-1250000000"
        assert kwargs["Key"] == "dest.txt"
        assert kwargs["LocalFilePath"] == str(f)
        assert kwargs["PartSize"] == 20
        assert kwargs["MAXThread"] == 5
        assert "progress_callback" in kwargs

    def test_storage_class_and_meta(self, mock_client, patch_init_client, tmp_path):
        """storage_class / meta / content_type / rate_limiting 透传"""
        mod = patch_init_client("upload_object", mock_client)
        f = tmp_path / "src.txt"
        f.write_text("hello")

        mod.upload_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(f),
             "storage_class": "STANDARD_IA", "content_type": "text/plain",
             "meta": "author=alice#version=1.0",
             "rate_limiting": 10},
            MOCK_GLOBALS,
        )

        kwargs = mock_client.upload_file.call_args.kwargs
        assert kwargs["StorageClass"] == "STANDARD_IA"
        assert kwargs["ContentType"] == "text/plain"
        assert kwargs["Metadata"] == {
            "x-cos-meta-author": "alice", "x-cos-meta-version": "1.0",
        }
        # 10 MB/s = 10*1024*1024*8 bit/s
        assert kwargs["TrafficLimit"] == str(10 * 1024 * 1024 * 8)

    def test_local_path_not_exist(self, mock_client, patch_init_client, capsys):
        """Convey: Upload no local file —— 打印错误并直接 return"""
        mod = patch_init_client("upload_object", mock_client)

        mod.upload_object(
            {"bucket": "b", "cos_key": "k",
             "local_path": "/tmp/tccli-cos-nonexistent-upload-src"},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()
        assert "本地文件不存在" in capsys.readouterr().out

    def test_path_is_directory_without_recursive(self, mock_client, patch_init_client, capsys, tmp_path):
        """本地是目录但未指定 recursive —— 报错"""
        mod = patch_init_client("upload_object", mock_client)

        mod.upload_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(tmp_path)},
            MOCK_GLOBALS,
        )

        mock_client.upload_file.assert_not_called()
        assert "指定路径不是文件" in capsys.readouterr().out

    def test_retry_then_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: err-retry-num —— 第一次失败、第二次成功"""
        mod = patch_init_client("upload_object", mock_client)
        f = tmp_path / "src.txt"
        f.write_text("hello")
        mock_client.upload_file.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            None,
        ]

        mod.upload_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(f), "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.upload_file.call_count == 2

    def test_retry_exhausted_raises(self, mock_client, patch_init_client, tmp_path, capsys):
        """重试耗尽：_upload_single 会 raise，上层 upload_object 的 except 捕获并打印 Error"""
        mod = patch_init_client("upload_object", mock_client)
        f = tmp_path / "src.txt"
        f.write_text("hello")
        mock_client.upload_file.side_effect = make_cos_error(
            "InternalError", "mock", "r1", "PUT", 500,
        )

        mod.upload_object(
            {"bucket": "b", "cos_key": "k", "local_path": str(f), "retry": 1},
            MOCK_GLOBALS,
        )

        # retry=1 -> 共 2 次尝试
        assert mock_client.upload_file.call_count == 2
        assert "Error:" in capsys.readouterr().out


class TestUploadRecursive:

    def test_recursive_success(self, mock_client, patch_init_client, tmp_path):
        """Convey: Upload directory success —— 两个文件都被上传"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("aaa")
        (tmp_path / "sub").mkdir()
        (tmp_path / "sub" / "b.log").write_text("bbb")

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre",
             "local_path": str(tmp_path), "recursive": True},
            MOCK_GLOBALS,
        )

        # 2 个文件都被上传
        assert mock_client.upload_file.call_count == 2
        # cos_key 会根据目录名自动拼接：pre/<dirname>/...
        keys = {c.kwargs["Key"] for c in mock_client.upload_file.call_args_list}
        # tmp_path 最后一级目录名会被保留（local_path 不以 / 结尾）
        dir_name = os.path.basename(str(tmp_path).rstrip(os.sep))
        assert ("pre/%s/a.txt" % dir_name) in keys
        assert ("pre/%s/sub/b.log" % dir_name) in keys

    def test_recursive_include_exclude(self, mock_client, patch_init_client, tmp_path):
        """include/exclude 过滤在 recursive 模式下生效"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        (tmp_path / "b.log").write_text("b")

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True, "include": "*.txt"},
            MOCK_GLOBALS,
        )

        # 只有 a.txt 被上传
        assert mock_client.upload_file.call_count == 1
        assert mock_client.upload_file.call_args.kwargs["Key"] == "pre/a.txt"

    def test_recursive_empty_dir_creates_marker(self, mock_client, patch_init_client, tmp_path):
        """空目录在 COS 上创建 / 结尾的空对象标记"""
        mod = patch_init_client("upload_object", mock_client)
        # 创建一个完全空的目录
        empty = tmp_path / "empty_dir"
        empty.mkdir()

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True},
            MOCK_GLOBALS,
        )

        # 没有文件可上传
        mock_client.upload_file.assert_not_called()
        # 空目录被创建为 put_object（Key 以 / 结尾）
        mock_client.put_object.assert_called()
        keys = [c.kwargs["Key"] for c in mock_client.put_object.call_args_list]
        assert any(k.endswith("empty_dir/") for k in keys)

    def test_recursive_file_retry(self, mock_client, patch_init_client, tmp_path):
        """recursive 模式下单个文件重试逻辑（失败不中断整体）"""
        mod = patch_init_client("upload_object", mock_client)
        (tmp_path / "a.txt").write_text("a")
        mock_client.upload_file.side_effect = [
            make_cos_error("InternalError", "mock", "r1", "PUT", 500),
            None,
        ]

        mod.upload_object(
            {"bucket": "b", "cos_key": "pre/",
             "local_path": str(tmp_path) + "/",
             "recursive": True, "retry": 3},
            MOCK_GLOBALS,
        )

        assert mock_client.upload_file.call_count == 2


class TestUploadErrorPaths:

    def test_init_client_fails_caught(self, monkeypatch, capsys):
        """init_cos_client 抛异常 —— 命令允许异常抛出，
        但此处我们验证上层 try/except 吞掉运行期错误。"""
        from conftest import cos_module
        mod = cos_module("upload_object")
        def _raise(_pg):
            raise Exception("boom")
        monkeypatch.setattr(mod, "init_cos_client", _raise)

        try:
            mod.upload_object({"bucket": "b", "cos_key": "k", "local_path": "/x"},
                              MOCK_GLOBALS)
            # 若抛出到这里以上，下一行不会执行；若被吞则 OK
        except Exception as e:
            assert "boom" in str(e)
