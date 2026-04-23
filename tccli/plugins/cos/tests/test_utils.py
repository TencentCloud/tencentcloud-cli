# -*- coding: utf-8 -*-
"""
tccli.plugins.cos.utils 工具函数单测。

覆盖目标：
- parse_global_arg：凭据优先级（命令行 > 环境变量 > 配置文件）+ 校验失败
- init_cos_client：成功构造 CosS3Client（mock qcloud_cos 类）
- format_size / match_filters / parse_meta / build_cos_key：全部分支
- calculate_local_crc64 / parse_http_time / get_object_head
- should_skip_sync_upload / should_skip_sync_download / should_skip_sync_copy
- list_all_objects / list_all_objects_with_dirs / list_local_files
- TransferProgressMonitor：start / stop / update_ok / update_skip / update_err / callback / log_file
"""
import os
import json

import pytest
from unittest.mock import MagicMock, patch

from tccli.plugins.cos import utils as _utils

from conftest import make_cos_error


# =============================================================
# _load_json_file
# =============================================================

class TestLoadJsonFile:

    def test_ok(self, tmp_path):
        f = tmp_path / "a.json"
        f.write_text('{"k": 1}')
        assert _utils._load_json_file(str(f)) == {"k": 1}

    def test_missing_file_returns_empty(self, tmp_path):
        assert _utils._load_json_file(str(tmp_path / "not-exist.json")) == {}

    def test_invalid_json_returns_empty(self, tmp_path):
        f = tmp_path / "a.json"
        f.write_text("not-json")
        assert _utils._load_json_file(str(f)) == {}


# =============================================================
# parse_global_arg 凭据优先级
# =============================================================

class TestParseGlobalArg:

    def _isolate_env(self, monkeypatch):
        """隔离掉所有腾讯云相关环境变量，避免宿主机污染测试。"""
        for k in ("TENCENTCLOUD_SECRET_ID", "TENCENTCLOUD_SECRET_KEY",
                  "TENCENTCLOUD_TOKEN", "TENCENTCLOUD_REGION", "TCCLI_PROFILE"):
            monkeypatch.delenv(k, raising=False)

    def _isolate_home(self, monkeypatch, tmp_path):
        """把 HOME 指到 tmp_path，确保 ~/.tccli/*.configure/credential 读不到真实文件。"""
        monkeypatch.setenv("HOME", str(tmp_path))

    def test_cli_arg_highest_priority(self, monkeypatch, tmp_path):
        """命令行参数优先于环境变量与配置文件"""
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)
        monkeypatch.setenv("TENCENTCLOUD_SECRET_ID", "env-sid")
        monkeypatch.setenv("TENCENTCLOUD_SECRET_KEY", "env-sk")

        pg = {"secretId": "cli-sid", "secretKey": "cli-sk",
              "token": None, "region": None, "endpoint": None, "profile": None}
        out = _utils.parse_global_arg(pg)
        assert out["secretId"] == "cli-sid"
        assert out["secretKey"] == "cli-sk"
        assert out["profile"] == "default"

    def test_env_var_fallback(self, monkeypatch, tmp_path):
        """未指定命令行参数时，使用环境变量"""
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)
        monkeypatch.setenv("TENCENTCLOUD_SECRET_ID", "env-sid")
        monkeypatch.setenv("TENCENTCLOUD_SECRET_KEY", "env-sk")
        monkeypatch.setenv("TENCENTCLOUD_TOKEN", "env-tk")
        monkeypatch.setenv("TENCENTCLOUD_REGION", "ap-beijing")

        pg = {"secretId": None, "secretKey": None,
              "token": None, "region": None, "endpoint": None, "profile": None}
        out = _utils.parse_global_arg(pg)
        assert out["secretId"] == "env-sid"
        assert out["secretKey"] == "env-sk"
        assert out["token"] == "env-tk"
        assert out["region"] == "ap-beijing"

    def test_credential_file_fallback(self, monkeypatch, tmp_path):
        """命令行 + 环境变量都没给时，读 ~/.tccli/<profile>.credential"""
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)
        tccli_dir = tmp_path / ".tccli"
        tccli_dir.mkdir()
        (tccli_dir / "default.credential").write_text(json.dumps({
            "secretId": "cred-sid",
            "secretKey": "cred-sk",
            "token": "cred-tk",
        }))
        (tccli_dir / "default.configure").write_text(json.dumps({
            "_sys_param": {"region": "ap-chengdu"},
        }))

        pg = {"secretId": None, "secretKey": None,
              "token": None, "region": None, "endpoint": None, "profile": None}
        out = _utils.parse_global_arg(pg)
        assert out["secretId"] == "cred-sid"
        assert out["secretKey"] == "cred-sk"
        assert out["token"] == "cred-tk"
        assert out["region"] == "ap-chengdu"
        assert out["endpoint"] is None

    def test_profile_env_override(self, monkeypatch, tmp_path):
        """TCCLI_PROFILE 环境变量能影响读取的配置文件"""
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)
        monkeypatch.setenv("TCCLI_PROFILE", "prod")
        tccli_dir = tmp_path / ".tccli"
        tccli_dir.mkdir()
        (tccli_dir / "prod.credential").write_text(json.dumps({
            "secretId": "prod-sid", "secretKey": "prod-sk",
        }))

        pg = {"secretId": None, "secretKey": None,
              "token": None, "region": None, "endpoint": None, "profile": None}
        out = _utils.parse_global_arg(pg)
        assert out["profile"] == "prod"
        assert out["secretId"] == "prod-sid"

    def test_missing_secret_id_raises(self, monkeypatch, tmp_path):
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)

        with pytest.raises(Exception) as exc:
            _utils.parse_global_arg({"secretId": None, "secretKey": None,
                                     "token": None, "region": None,
                                     "endpoint": None, "profile": None})
        assert "secretId 未配置" in str(exc.value)

    def test_missing_secret_key_raises(self, monkeypatch, tmp_path):
        self._isolate_env(monkeypatch)
        self._isolate_home(monkeypatch, tmp_path)

        with pytest.raises(Exception) as exc:
            _utils.parse_global_arg({"secretId": "x", "secretKey": None,
                                     "token": None, "region": None,
                                     "endpoint": None, "profile": None})
        assert "secretKey 未配置" in str(exc.value)


# =============================================================
# init_cos_client
# =============================================================

class TestInitCosClient:

    def test_success(self, monkeypatch):
        """mock qcloud_cos.CosConfig + CosS3Client，验证 init_cos_client 的装配逻辑"""
        fake_config_cls = MagicMock(return_value="fake-config-obj")
        fake_client_cls = MagicMock(return_value="fake-client-obj")
        monkeypatch.setattr("qcloud_cos.CosConfig", fake_config_cls)
        monkeypatch.setattr("qcloud_cos.CosS3Client", fake_client_cls)

        pg = {"secretId": "sid", "secretKey": "sk", "token": "tk",
              "region": None, "endpoint": None, "profile": "default"}
        client, region = _utils.init_cos_client(pg)

        assert client == "fake-client-obj"
        # region 为空时默认 ap-guangzhou
        assert region == "ap-guangzhou"
        fake_config_cls.assert_called_once_with(
            Region="ap-guangzhou", SecretId="sid", SecretKey="sk",
            Token="tk", Endpoint=None,
        )
        fake_client_cls.assert_called_once_with("fake-config-obj")


# =============================================================
# format_size 各阈值
# =============================================================

class TestFormatSize:
    @pytest.mark.parametrize("size,expected_substr", [
        (0, "0 B"),
        (1023, "1023 B"),
        (1024, "1.00 KB"),
        (1024 * 1024, "1.00 MB"),
        (1024 * 1024 * 1024, "1.00 GB"),
        (1024 * 1024 * 1024 * 1024, "1.00 TB"),
    ])
    def test_boundaries(self, size, expected_substr):
        assert _utils.format_size(size) == expected_substr


# =============================================================
# match_filters
# =============================================================

class TestMatchFilters:
    @pytest.mark.parametrize("name,inc,exc,expected", [
        ("a.txt", "", "", True),
        ("a.txt", "*.txt", "", True),
        ("a.log", "*.txt", "", False),
        ("a.txt", "", "*.log", True),
        ("a.log", "", "*.log", False),
        ("a.txt", "*.txt", "*.log", True),   # include 过，且 exclude 不匹配
        ("a.log", "*.txt", "*.log", False),   # include 不过
    ])
    def test_all_cases(self, name, inc, exc, expected):
        assert _utils.match_filters(name, inc, exc) is expected


# =============================================================
# parse_meta
# =============================================================

class TestParseMeta:

    def test_normal(self):
        assert _utils.parse_meta("a=1#b=2") == {
            "x-cos-meta-a": "1", "x-cos-meta-b": "2",
        }

    def test_strip_spaces(self):
        assert _utils.parse_meta(" a = 1 # b = 2 ") == {
            "x-cos-meta-a": "1", "x-cos-meta-b": "2",
        }

    def test_empty_and_invalid(self):
        assert _utils.parse_meta("") == {}
        # 不含 "="，会被忽略
        assert _utils.parse_meta("invalid#a=1") == {"x-cos-meta-a": "1"}


# =============================================================
# build_cos_key
# =============================================================

class TestBuildCosKey:
    @pytest.mark.parametrize("prefix,rel,expected", [
        ("", "dir/file.txt", "dir/file.txt"),
        ("backup", "dir/file.txt", "backup/dir/file.txt"),
        ("backup/", "dir/file.txt", "backup/dir/file.txt"),
    ])
    def test_cases(self, prefix, rel, expected):
        assert _utils.build_cos_key(prefix, rel) == expected


# =============================================================
# calculate_local_crc64
# =============================================================

class TestCalcLocalCrc64:

    def test_normal_file(self, tmp_path):
        f = tmp_path / "a.txt"
        f.write_text("hello")
        crc = _utils.calculate_local_crc64(str(f))
        assert crc is not None
        # 稳定值断言
        assert _utils.calculate_local_crc64(str(f)) == crc

    def test_missing_file_returns_none(self, tmp_path):
        assert _utils.calculate_local_crc64(str(tmp_path / "nonexistent.bin")) is None

    def test_crcmod_not_installed(self, monkeypatch, tmp_path):
        """模拟 crcmod 未安装 —— 导入失败时返回 None"""
        import builtins
        real_import = builtins.__import__

        def fake_import(name, *a, **kw):
            if name == "crcmod":
                raise ImportError("no crcmod")
            return real_import(name, *a, **kw)

        monkeypatch.setattr(builtins, "__import__", fake_import)
        f = tmp_path / "a.txt"
        f.write_text("x")
        assert _utils.calculate_local_crc64(str(f)) is None


# =============================================================
# get_object_head
# =============================================================

class TestGetObjectHead:

    def test_ok(self):
        cli = MagicMock()
        cli.head_object.return_value = {"Content-Length": "1"}
        assert _utils.get_object_head(cli, "b", "k") == {"Content-Length": "1"}

    def test_cos_service_error_returns_none(self):
        cli = MagicMock()
        cli.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no key", "req-1", "HEAD", 404,
        )
        assert _utils.get_object_head(cli, "b", "k") is None

    def test_generic_exception_returns_none(self):
        cli = MagicMock()
        cli.head_object.side_effect = RuntimeError("boom")
        assert _utils.get_object_head(cli, "b", "k") is None


# =============================================================
# parse_http_time
# =============================================================

class TestParseHttpTime:

    def test_empty(self):
        assert _utils.parse_http_time("") is None
        assert _utils.parse_http_time(None) is None

    def test_rfc1123(self):
        ts = _utils.parse_http_time("Mon, 02 Jan 2006 15:04:05 GMT")
        # 2006-01-02T15:04:05Z = 1136214245
        assert ts == 1136214245.0

    def test_rfc3339(self):
        ts = _utils.parse_http_time("2006-01-02T15:04:05Z")
        assert ts == 1136214245.0

    def test_invalid(self):
        assert _utils.parse_http_time("not a time") is None


# =============================================================
# should_skip_sync_upload / download / copy 全分支
# =============================================================

class TestShouldSkipSyncUpload:

    def test_target_missing_no_skip(self):
        cli = MagicMock()
        cli.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no key", "r", "HEAD", 404,
        )
        assert _utils.should_skip_sync_upload(cli, "b", "k", "/tmp/x", 0) is False

    def test_ignore_existing(self):
        cli = MagicMock()
        cli.head_object.return_value = {"Content-Length": "1"}
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", "/tmp/x", 0, ignore_existing=True
        ) is True

    def test_update_remote_newer(self):
        cli = MagicMock()
        cli.head_object.return_value = {
            "Last-Modified": "Sun, 07 Apr 2030 06:00:00 GMT",
        }
        # local mtime = 2020-01-01
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", "/tmp/x", 1577836800.0, update=True,
        ) is True

    def test_update_remote_older(self):
        cli = MagicMock()
        cli.head_object.return_value = {
            "Last-Modified": "Sun, 07 Apr 2000 06:00:00 GMT",
        }
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", "/tmp/x", 1577836800.0, update=True,
        ) is False

    def test_default_crc_match(self, tmp_path):
        cli = MagicMock()
        local = tmp_path / "a.txt"
        local.write_text("hello")
        crc = _utils.calculate_local_crc64(str(local))
        assert crc is not None
        cli.head_object.return_value = {"x-cos-hash-crc64ecma": crc}
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", str(local), 0,
        ) is True

    def test_default_crc_mismatch(self, tmp_path):
        cli = MagicMock()
        local = tmp_path / "a.txt"
        local.write_text("hello")
        cli.head_object.return_value = {"x-cos-hash-crc64ecma": "999"}
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", str(local), 0,
        ) is False

    def test_default_remote_crc_empty(self, tmp_path):
        cli = MagicMock()
        local = tmp_path / "a.txt"
        local.write_text("hello")
        cli.head_object.return_value = {"x-cos-hash-crc64ecma": ""}
        assert _utils.should_skip_sync_upload(
            cli, "b", "k", str(local), 0,
        ) is False


class TestShouldSkipSyncDownload:

    def test_local_missing_no_skip(self, tmp_path):
        cli = MagicMock()
        assert _utils.should_skip_sync_download(
            cli, "b", "k", {"LastModified": ""},
            str(tmp_path / "missing.bin"),
        ) is False

    def test_ignore_existing(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("x")
        assert _utils.should_skip_sync_download(
            cli, "b", "k", {"LastModified": ""}, str(f), ignore_existing=True,
        ) is True

    def test_update_local_newer(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("x")
        # 给个很新的本地 mtime
        future = 4102444800.0  # 2100-01-01
        os.utime(str(f), (future, future))
        assert _utils.should_skip_sync_download(
            cli, "b", "k",
            {"LastModified": "Sun, 07 Apr 2000 06:00:00 GMT"},
            str(f), update=True,
        ) is True

    def test_update_remote_newer(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("x")
        old = 946684800.0  # 2000-01-01
        os.utime(str(f), (old, old))
        assert _utils.should_skip_sync_download(
            cli, "b", "k",
            {"LastModified": "Sun, 07 Apr 2030 06:00:00 GMT"},
            str(f), update=True,
        ) is False

    def test_default_crc_match(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("hello")
        crc = _utils.calculate_local_crc64(str(f))
        cli.head_object.return_value = {"x-cos-hash-crc64ecma": crc}
        assert _utils.should_skip_sync_download(
            cli, "b", "k", {}, str(f),
        ) is True

    def test_default_remote_head_missing(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("hello")
        # head_object 抛错 → get_object_head 返回 None → 不跳过
        cli.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no", "r", "HEAD", 404,
        )
        assert _utils.should_skip_sync_download(
            cli, "b", "k", {}, str(f),
        ) is False

    def test_default_remote_crc_empty(self, tmp_path):
        cli = MagicMock()
        f = tmp_path / "a.txt"
        f.write_text("hello")
        cli.head_object.return_value = {"x-cos-hash-crc64ecma": ""}
        assert _utils.should_skip_sync_download(
            cli, "b", "k", {}, str(f),
        ) is False


class TestShouldSkipSyncCopy:

    def test_dest_missing_no_skip(self):
        cli = MagicMock()
        cli.head_object.side_effect = make_cos_error(
            "NoSuchKey", "no", "r", "HEAD", 404,
        )
        assert _utils.should_skip_sync_copy(cli, "sb", "sk", "db", "dk") is False

    def test_ignore_existing(self):
        cli = MagicMock()
        cli.head_object.return_value = {"Content-Length": "1"}
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk", ignore_existing=True,
        ) is True

    def test_update_dest_newer(self):
        cli = MagicMock()
        # 先 dest_head，再 src_head
        cli.head_object.side_effect = [
            {"Last-Modified": "Sun, 07 Apr 2030 06:00:00 GMT"},  # dest 新
            {"Last-Modified": "Sun, 07 Apr 2000 06:00:00 GMT"},  # src 旧
        ]
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk", update=True,
        ) is True

    def test_update_src_newer(self):
        cli = MagicMock()
        cli.head_object.side_effect = [
            {"Last-Modified": "Sun, 07 Apr 2000 06:00:00 GMT"},  # dest 旧
            {"Last-Modified": "Sun, 07 Apr 2030 06:00:00 GMT"},  # src 新
        ]
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk", update=True,
        ) is False

    def test_default_crc_match(self):
        cli = MagicMock()
        cli.head_object.side_effect = [
            {"x-cos-hash-crc64ecma": "12345"},  # dest
            {"x-cos-hash-crc64ecma": "12345"},  # src
        ]
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk",
        ) is True

    def test_default_crc_missing_on_either_side(self):
        cli = MagicMock()
        cli.head_object.side_effect = [
            {"x-cos-hash-crc64ecma": ""},
            {"x-cos-hash-crc64ecma": "12345"},
        ]
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk",
        ) is False

    def test_src_missing(self):
        cli = MagicMock()
        cli.head_object.side_effect = [
            {"x-cos-hash-crc64ecma": "1"},  # dest ok
            make_cos_error("NoSuchKey", "no", "r", "HEAD", 404),  # src missing
        ]
        assert _utils.should_skip_sync_copy(
            cli, "sb", "sk", "db", "dk",
        ) is False


# =============================================================
# list_all_objects / list_all_objects_with_dirs / list_local_files
# =============================================================

class TestListAllObjects:

    def test_pagination_and_skip_dir_markers(self):
        cli = MagicMock()
        cli.list_objects.side_effect = [
            # 第一页：含目录标记 + 普通文件 + 截断
            {"Contents": [
                {"Key": "pre/dir/", "Size": "0"},   # 目录标记会被跳过
                {"Key": "pre/a.txt", "Size": "10",
                 "ETag": '"1"', "LastModified": "t1",
                 "StorageClass": "STANDARD"},
            ], "IsTruncated": "true", "NextMarker": "pre/a.txt"},
            # 第二页
            {"Contents": [
                {"Key": "pre/b.txt", "Size": "20",
                 "ETag": '"2"', "LastModified": "t2",
                 "StorageClass": "STANDARD_IA"},
            ], "IsTruncated": "false"},
        ]

        result = _utils.list_all_objects(cli, "b", "pre/")
        assert set(result.keys()) == {"pre/a.txt", "pre/b.txt"}
        assert result["pre/a.txt"]["Size"] == 10
        assert result["pre/b.txt"]["StorageClass"] == "STANDARD_IA"
        assert cli.list_objects.call_count == 2

    def test_with_dirs_keeps_markers(self):
        cli = MagicMock()
        cli.list_objects.return_value = {
            "Contents": [
                {"Key": "pre/dir/", "Size": "0",
                 "ETag": '"0"', "LastModified": "t",
                 "StorageClass": "STANDARD"},
                {"Key": "pre/a.txt", "Size": "5",
                 "ETag": '"1"', "LastModified": "t",
                 "StorageClass": "STANDARD"},
            ],
            "IsTruncated": "false",
        }
        result = _utils.list_all_objects_with_dirs(cli, "b", "pre/")
        assert set(result.keys()) == {"pre/dir/", "pre/a.txt"}
        assert result["pre/dir/"]["IsDir"] is True
        assert result["pre/a.txt"]["IsDir"] is False


class TestListLocalFiles:

    def test_recursive_and_mtime(self, tmp_path):
        (tmp_path / "a.txt").write_text("aaa")
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "b.log").write_text("bb")

        result = _utils.list_local_files(str(tmp_path))
        assert set(result.keys()) == {"a.txt", "sub/b.log"}
        assert result["a.txt"]["Size"] == 3
        assert "FullPath" in result["a.txt"]
        assert "MTime" in result["a.txt"]

    def test_empty_dir(self, tmp_path):
        assert _utils.list_local_files(str(tmp_path)) == {}


# =============================================================
# TransferProgressMonitor
# =============================================================

class TestTransferProgressMonitor:

    def test_happy_path_with_callback_and_log(self, tmp_path):
        """完整走一遍：start → set_scan_info → ok + skip + err → stop → 写 log"""
        m = _utils.TransferProgressMonitor("upload")
        m.set_scan_info(3, 300)
        m.start()

        # 成功（通过 callback 模拟进度更新）
        cb, fid = m.create_progress_callback(100)
        cb(50, 100)   # 进行中
        cb(100, 100)  # 完成
        m.update_ok(100, fid)

        # 跳过
        m.update_skip(100)

        # 失败
        fail_cb, fail_fid = m.create_progress_callback(100)
        m.update_err(
            fail_fid,
            src_path="/local/a.txt",
            dest_path="cos://b/a.txt",
            reason="mock",
            request_id="req-1",
        )

        log_path = tmp_path / "logs" / "fail.log"
        m.stop(log_file=str(log_path))

        # 失败日志被写出（目录会自动创建）
        assert log_path.exists()
        body = log_path.read_text(encoding="utf-8")
        assert "Source    : /local/a.txt" in body
        assert "Dest      : cos://b/a.txt" in body
        assert "Reason    : mock" in body
        assert "RequestId : req-1" in body

    def test_update_ok_without_callback(self):
        """不使用 progress_callback 时，update_ok 直接累加 transfer_size"""
        m = _utils.TransferProgressMonitor("copy")
        m.set_scan_info(1, 10)
        m.update_ok(10)  # 无 file_id
        assert m.transfer_size == 10
        assert m.ok_num == 1

    def test_update_err_legacy_path_kw(self):
        """update_err 通过旧的 path= 兼容参数工作"""
        m = _utils.TransferProgressMonitor("download")
        m.update_err(path="/a", reason="x")
        assert m.err_num == 1
        assert m._fail_records[0]["src_path"] == "/a"

    def test_write_log_file_err_path(self, monkeypatch, tmp_path):
        """写日志失败（open 异常）时，应打印错误到 stderr，但不抛异常"""
        m = _utils.TransferProgressMonitor("upload")
        m.update_err(path="/a", reason="x")

        real_open = open

        def fake_open(path, *a, **kw):
            if str(path).endswith("fail.log"):
                raise IOError("disk full")
            return real_open(path, *a, **kw)

        monkeypatch.setattr("builtins.open", fake_open)

        # 不应抛异常
        m._write_log_file(str(tmp_path / "fail.log"))

    def test_start_stop_without_callbacks(self):
        """空 monitor 也能正常 start/stop"""
        m = _utils.TransferProgressMonitor("delete")
        m.set_scan_info(0, 0)
        m.start()
        m.stop()  # log_file 为空 → 不写文件

    def test_stop_empty_log_file_no_write(self, tmp_path):
        """stop(log_file="") 时即使有失败记录也不写文件"""
        m = _utils.TransferProgressMonitor("upload")
        m.update_err(path="/a", reason="x")
        m.stop(log_file="")
        assert not (tmp_path / "any.log").exists()
