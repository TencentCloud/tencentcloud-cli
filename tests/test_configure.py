# -*- coding: utf-8 -*-
import io
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tccli.configure import ConfigureGetCommand, ConfigureSetCommand, ConfigureListCommand
from tccli.exceptions import ConfigurationError, ParamError
from utils import shell, recover_profile


# ── ConfigureSetCommand：output / language 非法值回退 ─────────────────────────

def _make_set_cmd():
    return ConfigureSetCommand()


@pytest.mark.parametrize("bad_output", ["xml", "yaml", ""])
def test_configure_set_invalid_output_falls_back_to_json(tmp_path, monkeypatch, bad_output, capsys):
    monkeypatch.setattr("tccli.configure.BasicConfigure.cli_path", str(tmp_path), raising=False)
    cmd = _make_set_cmd()
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    class FakeArgs:
        varname = ["output", bad_output]

    class FakeGlobals:
        profile = "unit_test"

    cmd._run_main(FakeArgs(), FakeGlobals())
    _, conf_path = cmd._profile_existed("unit_test.configure")
    data = json.loads(open(conf_path).read())
    assert data["_sys_param"]["output"] == "json"


@pytest.mark.parametrize("bad_lang", ["fr-FR", "ja-JP", ""])
def test_configure_set_invalid_language_falls_back_to_zh_cn(tmp_path, monkeypatch, bad_lang):
    cmd = _make_set_cmd()
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    class FakeArgs:
        varname = ["language", bad_lang]

    class FakeGlobals:
        profile = "unit_test"

    cmd._run_main(FakeArgs(), FakeGlobals())
    _, conf_path = cmd._profile_existed("unit_test.configure")
    data = json.loads(open(conf_path).read())
    assert data["_sys_param"]["language"] == "zh-CN"


def test_configure_set_odd_varname_raises(tmp_path, monkeypatch):
    cmd = _make_set_cmd()
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    class FakeArgs:
        varname = ["region"]  # 奇数个参数

    class FakeGlobals:
        profile = "unit_test"

    with pytest.raises(ParamError):
        cmd._run_main(FakeArgs(), FakeGlobals())


# ── ConfigureGetCommand：字段不存在时抛 ConfigurationError ────────────────────

def test_configure_get_nonexistent_key_raises(tmp_path, monkeypatch):
    cmd = ConfigureGetCommand()
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    conf_path = tmp_path / "unit_test.configure"
    conf_path.write_text(json.dumps({"_sys_param": {"region": "ap-guangzhou"}}))
    cred_path = tmp_path / "unit_test.credential"
    cred_path.write_text(json.dumps({}))

    class FakeArgs:
        varname = ["nonexistent_key"]

    class FakeGlobals:
        profile = "unit_test"

    with pytest.raises(ConfigurationError):
        cmd._run_main(FakeArgs(), FakeGlobals())


def test_configure_get_existing_key_outputs_value(tmp_path, monkeypatch):
    stream = io.StringIO()
    cmd = ConfigureGetCommand(stream=stream)
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    conf_path = tmp_path / "unit_test.configure"
    conf_path.write_text(json.dumps({"_sys_param": {"region": "ap-beijing"}}))
    cred_path = tmp_path / "unit_test.credential"
    cred_path.write_text(json.dumps({}))

    class FakeArgs:
        varname = ["region"]

    class FakeGlobals:
        profile = "unit_test"

    cmd._run_main(FakeArgs(), FakeGlobals())
    assert "region = ap-beijing" in stream.getvalue()


# ── 集成测试（依赖已安装的 tccli，不发真实 API 请求）────────────────────────────

def test_configure_list_output_structure():
    output = shell("tccli configure list")
    assert "credential:" in output
    assert "configure:" in output
    assert "cvm.version =" in output
    assert "cvm.endpoint =" in output


@recover_profile()
def test_configure_get_set_region():
    shell("tccli configure set region ap-guangzhou")
    assert "region = ap-guangzhou" in shell("tccli configure get region")


@recover_profile()
def test_configure_set_output_valid_values():
    for fmt in ["json", "text", "table"]:
        shell("tccli configure set output %s" % fmt)
        assert ("output = %s" % fmt) in shell("tccli configure get output")


@recover_profile()
def test_configure_set_secretid_and_get():
    sec_id = "AKIDabcdefghijklmn1234"
    shell("tccli configure set secretId %s" % sec_id)
    output = shell("tccli configure get secretId")
    assert sec_id in output


@recover_profile("user2")
def test_configure_profile_isolation():
    shell("tccli configure --profile user2 set region ap-shanghai")
    assert "region = ap-shanghai\n" == shell("tccli configure --profile user2 get region")
    assert "region = ap-shanghai\n" == shell("TCCLI_PROFILE=user2 tccli configure get region")
