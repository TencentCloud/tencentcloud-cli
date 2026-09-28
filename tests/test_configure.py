# -*- coding: utf-8 -*-
import argparse
import json
import os
import shutil
import sys
import tempfile
import unittest

import pytest
import six

try:
    from unittest import mock
except ImportError:
    import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import tccli.options_define as OptionsDefine
from tccli.configure import (
    BasicConfigure,
    ConfigureCommand,
    ConfigureGetCommand,
    ConfigureListCommand,
    ConfigureSetCommand,
    mask_secret,
)
from tccli.exceptions import ConfigurationError, ParamError
from tccli.utils import Utils
from utils import shell, recover_profile


# ── ConfigureSetCommand：output / language 非法值回退 ─────────────────────────

def _make_set_cmd():
    return ConfigureSetCommand()


def _write_json_text(path, data):
    path.write_text(six.text_type(json.dumps(data)))


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
    _write_json_text(conf_path, {"_sys_param": {"region": "ap-guangzhou"}})
    cred_path = tmp_path / "unit_test.credential"
    _write_json_text(cred_path, {})

    class FakeArgs:
        varname = ["nonexistent_key"]

    class FakeGlobals:
        profile = "unit_test"

    with pytest.raises(ConfigurationError):
        cmd._run_main(FakeArgs(), FakeGlobals())


def test_configure_get_existing_key_outputs_value(tmp_path, monkeypatch):
    stream = six.StringIO()
    cmd = ConfigureGetCommand(stream=stream)
    monkeypatch.setattr(cmd, "cli_path", str(tmp_path))

    conf_path = tmp_path / "unit_test.configure"
    _write_json_text(conf_path, {"_sys_param": {"region": "ap-beijing"}})
    cred_path = tmp_path / "unit_test.credential"
    _write_json_text(cred_path, {})

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
    assert mask_secret(sec_id) in output
    assert sec_id not in output


@recover_profile("user2")
def test_configure_profile_isolation():
    shell("tccli configure --profile user2 set region ap-shanghai")
    assert "region = ap-shanghai\n" == shell("tccli configure --profile user2 get region")
    assert "region = ap-shanghai\n" == shell("TCCLI_PROFILE=user2 tccli configure get region")


class TestMaskSecret(unittest.TestCase):

    def test_string_is_masked_with_fixed_prefix_and_last_four(self):
        self.assertEqual(
            mask_secret("aaaaaaaaaaaaaaaaaaaa"),
            "****************aaaa"
        )

    def test_empty_and_non_string_values_are_unchanged(self):
        self.assertEqual(mask_secret(""), "")
        self.assertIsNone(mask_secret(None))
        self.assertEqual(mask_secret(1234), 1234)

    def test_unicode_string_is_supported(self):
        self.assertEqual(mask_secret(u"\u51ed\u8bc1EFGH"),
                         u"****************EFGH")


class TestConfigureSecretMasking(unittest.TestCase):

    def setUp(self):
        self.cli_path = tempfile.mkdtemp()
        self.credential_path = os.path.join(
            self.cli_path, "default.credential")
        self.configure_path = os.path.join(
            self.cli_path, "default.configure")
        self.credential = {
            OptionsDefine.SecretId: "aaaaaaaaaaaaaaaaaaaa",
            OptionsDefine.SecretKey: "bbbbbbbbbbbbbbbbbbbb",
            OptionsDefine.Token: "cccccccccccccccccccc",
            OptionsDefine.RoleArn: "qcs::cam::uin/100000000001:roleName/test-role"
        }
        Utils.dump_json_msg(self.credential_path, self.credential)
        Utils.dump_json_msg(self.configure_path, {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-guangzhou"
            }
        })
        self.parsed_globals = argparse.Namespace(profile="default")

    def tearDown(self):
        shutil.rmtree(self.cli_path)

    def test_list_masks_sensitive_fields_only(self):
        stream = six.StringIO()
        command = ConfigureListCommand(stream=stream)
        command.cli_path = self.cli_path

        command._run_main(argparse.Namespace(), self.parsed_globals)

        output = stream.getvalue()
        self.assertIn("secretId = ****************aaaa", output)
        self.assertIn("secretKey = ****************bbbb", output)
        self.assertIn("token = ****************cccc", output)
        self.assertIn("role-arn = %s" % self.credential[OptionsDefine.RoleArn], output)
        self.assertIn("region = ap-guangzhou", output)
        self.assertNotIn(self.credential[OptionsDefine.SecretId], output)
        self.assertNotIn(self.credential[OptionsDefine.SecretKey], output)
        self.assertNotIn(self.credential[OptionsDefine.Token], output)
        self.assertEqual(Utils.load_json_msg(self.credential_path), self.credential)

    def test_get_masks_sensitive_fields_only(self):
        stream = six.StringIO()
        command = ConfigureGetCommand(stream=stream)
        command.cli_path = self.cli_path
        args = argparse.Namespace(varname=[
            OptionsDefine.SecretId,
            OptionsDefine.SecretKey,
            OptionsDefine.Token,
            OptionsDefine.Region
        ])

        command._run_main(args, self.parsed_globals)

        self.assertEqual(stream.getvalue().splitlines(), [
            "secretId = ****************aaaa",
            "secretKey = ****************bbbb",
            "token = ****************cccc",
            "region = ap-guangzhou"
        ])
        self.assertEqual(Utils.load_json_msg(self.credential_path), self.credential)


class TestConfigureDynamicCredentialMigration(unittest.TestCase):
    """交互式 configure 切换动态凭证时的安全行为。"""

    def setUp(self):
        self.cli_path = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.cli_path)

    def _create_command(self):
        command = ConfigureCommand.__new__(ConfigureCommand)
        BasicConfigure.__init__(command)
        command.cli_path = self.cli_path
        return command

    def _credential_path(self, profile):
        return os.path.join(self.cli_path, "%s.credential" % profile)

    def _write_credential(self, profile, credential):
        Utils.dump_json_msg(self._credential_path(profile), credential)

    def _read_credential(self, profile):
        return Utils.load_json_msg(self._credential_path(profile))

    def test_dynamic_credential_switch_requires_confirmation(self):
        old_credential = {
            "type": "sso",
            OptionsDefine.SecretId: "OLD_ID",
            OptionsDefine.SecretKey: "OLD_KEY",
            "sso": {"token": "old-token"},
        }
        self._write_credential("default", old_credential)
        command = self._create_command()

        with mock.patch.object(command, "_compat_input", return_value="n"):
            with mock.patch.object(command, "_init_configure") as init_configure:
                command._run_main(mock.Mock(), argparse.Namespace(profile="default"))

        init_configure.assert_not_called()
        self.assertEqual(self._read_credential("default"), old_credential)

    def test_confirmed_dynamic_credential_switch_replaces_refresh_data(self):
        for credential_type in ("sso", "oauth", "cvm-role"):
            profile = credential_type
            self._write_credential(profile, {
                "type": credential_type,
                OptionsDefine.SecretId: "OLD_ID",
                OptionsDefine.SecretKey: "OLD_KEY",
                "sso": {"token": "old-token"},
            })
            command = self._create_command()

            with mock.patch.object(
                    command, "_compat_input",
                    side_effect=["y", "NEW_ID", "NEW_KEY", "", ""]):
                with mock.patch.object(command, "_init_configure") as init_configure:
                    command._run_main(mock.Mock(), argparse.Namespace(profile=profile))

            init_configure.assert_called_once()
            self.assertEqual(self._read_credential(profile), {
                OptionsDefine.SecretId: "NEW_ID",
                OptionsDefine.SecretKey: "NEW_KEY",
            })
