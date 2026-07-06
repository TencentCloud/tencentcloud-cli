# -*- coding: utf-8 -*-
"""针对 tccli.configure 脱敏改造与相关命令的单元测试。

覆盖：
  * mask_secret 函数（长/短/边界/None/非字符串）
  * ConfigureListCommand：credential 段敏感字段脱敏，非敏感字段与 configure 段保持原文
  * ConfigureGetCommand：单字段/多字段混合/敏感与非敏感字段行为
  * ConfigureSetCommand：secretId/secretKey/token/其它字段的写入路径
  * ConfigureRemoveCommand：删除现有/不存在的 profile 文件
  * ConfigureSetRootDomainCommand：批量重写 endpoint
  * 磁盘 credential 文件在读取路径下保持明文
"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

import tccli.options_define as OptionsDefine
from tccli.configure import (
    BasicConfigure,
    ConfigureGetCommand,
    ConfigureListCommand,
    ConfigureRemoveCommand,
    ConfigureSetCommand,
    ConfigureSetRootDomainCommand,
    mask_secret,
)
from tccli.exceptions import ConfigurationError, ParamError


# ----------------------------------------------------------------------------
# 1. mask_secret 单元测试
# ----------------------------------------------------------------------------
class TestMaskSecret(unittest.TestCase):
    def test_long_string_masks_all_but_last_four(self):
        self.assertEqual(mask_secret("AKIDabcdefghijklmn1234"), "******************1234")

    def test_length_five_keeps_last_four(self):
        self.assertEqual(mask_secret("abcde"), "*bcde")

    def test_length_four_all_stars(self):
        self.assertEqual(mask_secret("abcd"), "****")

    def test_length_three_all_stars(self):
        self.assertEqual(mask_secret("abc"), "***")

    def test_length_one_single_star(self):
        self.assertEqual(mask_secret("a"), "*")

    def test_empty_string_returned_as_is(self):
        self.assertEqual(mask_secret(""), "")

    def test_none_returned_as_is(self):
        self.assertIsNone(mask_secret(None))

    def test_non_string_returned_as_is(self):
        self.assertEqual(mask_secret(12345), 12345)
        self.assertEqual(mask_secret(True), True)
        self.assertEqual(mask_secret(["a", "b"]), ["a", "b"])


# ----------------------------------------------------------------------------
# 2. Configure 命令测试基类：隔离 ~/.tccli 目录
# ----------------------------------------------------------------------------
class _ConfigureCmdTestBase(unittest.TestCase):
    profile = "cfg_unittest"

    def setUp(self):
        self.tmp_home = tempfile.mkdtemp(prefix="tccli_test_home_")
        self.cli_path = os.path.join(self.tmp_home, ".tccli")
        os.makedirs(self.cli_path)
        self._expand_patcher = mock.patch(
            "os.path.expanduser", lambda p: p.replace("~", self.tmp_home)
        )
        self._expand_patcher.start()

    def tearDown(self):
        self._expand_patcher.stop()
        shutil.rmtree(self.tmp_home, ignore_errors=True)

    def _cred_path(self):
        return os.path.join(self.cli_path, self.profile + ".credential")

    def _conf_path(self):
        return os.path.join(self.cli_path, self.profile + ".configure")

    def _write_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f)

    def _read_json(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def _parsed_globals(self):
        ns = mock.Mock()
        ns.profile = self.profile
        return ns


# ----------------------------------------------------------------------------
# 3. ConfigureListCommand
# ----------------------------------------------------------------------------
class TestConfigureListCommand(_ConfigureCmdTestBase):
    RAW_SECRET_ID = "AKIDabcdefghijklmn1234"
    RAW_SECRET_KEY = "SKabcdefghijklmnopqrst5678"
    RAW_TOKEN = "TOKENabcdefghijklm9012"
    ROLE_ARN = "qcs::cam::uin/12345:roleName/tester"

    def _seed_files(self):
        self._write_json(self._cred_path(), {
            OptionsDefine.SecretId: self.RAW_SECRET_ID,
            OptionsDefine.SecretKey: self.RAW_SECRET_KEY,
            OptionsDefine.Token: self.RAW_TOKEN,
            OptionsDefine.RoleArn: self.ROLE_ARN,
        })
        self._write_json(self._conf_path(), {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-guangzhou",
                OptionsDefine.Output: "json",
                OptionsDefine.Language: "zh-CN",
            },
            "cvm": {
                "endpoint": "cvm.tencentcloudapi.com",
                "version": "2017-03-12",
            },
        })

    def _run_list(self):
        stream = io.StringIO()
        ConfigureListCommand(stream=stream)._run_main(mock.Mock(), self._parsed_globals())
        return stream.getvalue()

    def test_sensitive_fields_are_masked(self):
        self._seed_files()
        out = self._run_list()

        self.assertIn("secretId = %s" % mask_secret(self.RAW_SECRET_ID), out)
        self.assertIn("secretKey = %s" % mask_secret(self.RAW_SECRET_KEY), out)
        self.assertIn("token = %s" % mask_secret(self.RAW_TOKEN), out)
        # 明文绝不能出现
        self.assertNotIn(self.RAW_SECRET_ID, out)
        self.assertNotIn(self.RAW_SECRET_KEY, out)
        self.assertNotIn(self.RAW_TOKEN, out)

    def test_non_sensitive_field_kept_plaintext(self):
        self._seed_files()
        out = self._run_list()
        self.assertIn("role-arn = %s" % self.ROLE_ARN, out)

    def test_configure_section_kept_plaintext(self):
        self._seed_files()
        out = self._run_list()
        self.assertIn("region = ap-guangzhou", out)
        self.assertIn("output = json", out)
        self.assertIn("language = zh-CN", out)
        self.assertIn("cvm.version = 2017-03-12", out)
        self.assertIn("cvm.endpoint = cvm.tencentcloudapi.com", out)

    def test_missing_files_only_prints_headers(self):
        # 完全没有 credential / configure 文件时命令不应报错
        out = self._run_list()
        self.assertIn("credential:", out)
        self.assertIn("configure:", out)

    def test_disk_credential_stays_plaintext_after_list(self):
        self._seed_files()
        self._run_list()
        cred_disk = self._read_json(self._cred_path())
        self.assertEqual(cred_disk[OptionsDefine.SecretId], self.RAW_SECRET_ID)
        self.assertEqual(cred_disk[OptionsDefine.SecretKey], self.RAW_SECRET_KEY)
        self.assertEqual(cred_disk[OptionsDefine.Token], self.RAW_TOKEN)


# ----------------------------------------------------------------------------
# 4. ConfigureGetCommand
# ----------------------------------------------------------------------------
class TestConfigureGetCommand(_ConfigureCmdTestBase):
    RAW_SECRET_ID = "AKIDabcdefghijklmn1234"
    RAW_SECRET_KEY = "SKabcdefghijklmnopqrst5678"
    RAW_TOKEN = "TOKENabcdefghijklm9012"

    def _seed(self):
        self._write_json(self._cred_path(), {
            OptionsDefine.SecretId: self.RAW_SECRET_ID,
            OptionsDefine.SecretKey: self.RAW_SECRET_KEY,
            OptionsDefine.Token: self.RAW_TOKEN,
        })
        self._write_json(self._conf_path(), {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-guangzhou",
                OptionsDefine.Output: "json",
            },
            "cvm": {
                "endpoint": "cvm.tencentcloudapi.com",
                "version": "2017-03-12",
            },
        })

    def _run_get(self, varnames):
        stream = io.StringIO()
        args = mock.Mock()
        args.varname = varnames
        ConfigureGetCommand(stream=stream)._run_main(args, self._parsed_globals())
        return stream.getvalue()

    def test_get_secret_id_masked(self):
        self._seed()
        out = self._run_get([OptionsDefine.SecretId])
        self.assertEqual(
            out.strip(),
            "secretId = %s" % mask_secret(self.RAW_SECRET_ID),
        )
        self.assertNotIn(self.RAW_SECRET_ID, out)

    def test_get_secret_key_masked(self):
        self._seed()
        out = self._run_get([OptionsDefine.SecretKey])
        self.assertEqual(
            out.strip(),
            "secretKey = %s" % mask_secret(self.RAW_SECRET_KEY),
        )
        self.assertNotIn(self.RAW_SECRET_KEY, out)

    def test_get_token_masked(self):
        self._seed()
        out = self._run_get([OptionsDefine.Token])
        self.assertEqual(
            out.strip(),
            "token = %s" % mask_secret(self.RAW_TOKEN),
        )
        self.assertNotIn(self.RAW_TOKEN, out)

    def test_get_region_kept_plaintext(self):
        self._seed()
        out = self._run_get([OptionsDefine.Region])
        self.assertEqual(out.strip(), "region = ap-guangzhou")

    def test_get_service_endpoint_kept_plaintext(self):
        self._seed()
        out = self._run_get(["cvm.endpoint"])
        self.assertEqual(out.strip(), "cvm.endpoint = cvm.tencentcloudapi.com")

    def test_get_mixed_varnames_only_sensitive_masked(self):
        self._seed()
        out = self._run_get([OptionsDefine.SecretId, OptionsDefine.Region])
        lines = [line for line in out.split("\n") if line]
        self.assertEqual(lines[0], "secretId = %s" % mask_secret(self.RAW_SECRET_ID))
        self.assertEqual(lines[1], "region = ap-guangzhou")
        self.assertNotIn(self.RAW_SECRET_ID, out)

    def test_get_unknown_field_raises(self):
        self._seed()
        with self.assertRaises(ConfigurationError):
            self._run_get(["not-exist-field"])

    def test_disk_credential_stays_plaintext_after_get(self):
        self._seed()
        self._run_get([OptionsDefine.SecretId, OptionsDefine.SecretKey, OptionsDefine.Token])
        cred_disk = self._read_json(self._cred_path())
        self.assertEqual(cred_disk[OptionsDefine.SecretId], self.RAW_SECRET_ID)
        self.assertEqual(cred_disk[OptionsDefine.SecretKey], self.RAW_SECRET_KEY)
        self.assertEqual(cred_disk[OptionsDefine.Token], self.RAW_TOKEN)


# ----------------------------------------------------------------------------
# 5. ConfigureSetCommand
# ----------------------------------------------------------------------------
class TestConfigureSetCommand(_ConfigureCmdTestBase):
    def _run_set(self, varname_kv):
        cmd = ConfigureSetCommand()
        args = mock.Mock()
        args.varname = varname_kv
        cmd._run_main(args, self._parsed_globals())

    def test_set_secret_id_and_key_written_plaintext_to_disk(self):
        self._run_set([
            OptionsDefine.SecretId, "AKIDrawvalue1234567890",
            OptionsDefine.SecretKey, "SKrawvalue1234567890abcd",
        ])
        cred = self._read_json(self._cred_path())
        self.assertEqual(cred[OptionsDefine.SecretId], "AKIDrawvalue1234567890")
        self.assertEqual(cred[OptionsDefine.SecretKey], "SKrawvalue1234567890abcd")

    def test_set_use_cvm_role_true_writes_type(self):
        self._run_set([OptionsDefine.UseCVMRole, "true"])
        cred = self._read_json(self._cred_path())
        self.assertEqual(cred["type"], "cvm-role")

    def test_set_use_cvm_role_false_writes_default(self):
        self._run_set([OptionsDefine.UseCVMRole, "false"])
        cred = self._read_json(self._cred_path())
        self.assertEqual(cred["type"], "default")

    def test_set_use_cvm_role_invalid_raises(self):
        with self.assertRaises(ParamError):
            self._run_set([OptionsDefine.UseCVMRole, "notabool"])

    def test_set_region_and_output_kept_in_sys_param(self):
        self._run_set([
            OptionsDefine.Region, "ap-shanghai",
            OptionsDefine.Output, "json",
        ])
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Region], "ap-shanghai")
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Output], "json")

    def test_set_output_invalid_falls_back_to_json(self):
        self._run_set([OptionsDefine.Output, "yaml"])
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Output], "json")

    def test_set_language_invalid_falls_back(self):
        self._run_set([OptionsDefine.Language, "fr-FR"])
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Language], "zh-CN")

    def test_set_extra_key_dot_notation(self):
        self._run_set(["cvm.endpoint", "cvm.internal.tencentcloudapi.com"])
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf["cvm"]["endpoint"], "cvm.internal.tencentcloudapi.com")

    def test_set_odd_arg_count_raises(self):
        cmd = ConfigureSetCommand()
        args = mock.Mock()
        args.varname = [OptionsDefine.Region]
        with self.assertRaises(ParamError):
            cmd._run_main(args, self._parsed_globals())


# ----------------------------------------------------------------------------
# 6. ConfigureRemoveCommand
# ----------------------------------------------------------------------------
class TestConfigureRemoveCommand(_ConfigureCmdTestBase):
    def test_remove_existing_files(self):
        self._write_json(self._cred_path(), {"secretId": "x"})
        self._write_json(self._conf_path(), {"_sys_param": {}})
        err_stream = io.StringIO()
        ConfigureRemoveCommand(error_stream=err_stream)._run_main(
            mock.Mock(), self._parsed_globals()
        )
        self.assertFalse(os.path.exists(self._cred_path()))
        self.assertFalse(os.path.exists(self._conf_path()))

    def test_remove_missing_files_writes_error(self):
        err_stream = io.StringIO()
        ConfigureRemoveCommand(error_stream=err_stream)._run_main(
            mock.Mock(), self._parsed_globals()
        )
        err = err_stream.getvalue()
        self.assertIn("not exist", err)


# ----------------------------------------------------------------------------
# 7. ConfigureSetRootDomainCommand
# ----------------------------------------------------------------------------
class TestConfigureSetRootDomainCommand(_ConfigureCmdTestBase):
    def test_set_root_domain_rewrites_all_endpoints(self):
        self._write_json(self._conf_path(), {
            OptionsDefine.SysParam: {},
            "cvm": {"endpoint": "cvm.tencentcloudapi.com", "version": "2017-03-12"},
        })
        cmd = ConfigureSetRootDomainCommand()
        args = mock.Mock()
        args.varname = ["internal.tencentcloudapi.com"]
        cmd._run_main(args, self._parsed_globals())
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf["cvm"]["endpoint"], "cvm.internal.tencentcloudapi.com")

    def test_set_root_domain_wrong_arg_count_raises(self):
        cmd = ConfigureSetRootDomainCommand()
        args = mock.Mock()
        args.varname = ["a", "b"]
        with self.assertRaises(ParamError):
            cmd._run_main(args, self._parsed_globals())


# ----------------------------------------------------------------------------
# 8. BasicConfigure 常量断言
# ----------------------------------------------------------------------------
class TestBasicConfigureFields(unittest.TestCase):
    def test_sensitive_cred_fields_contains_all_three(self):
        bc = BasicConfigure()
        self.assertEqual(
            bc.sensitive_cred_fields,
            {OptionsDefine.SecretId, OptionsDefine.SecretKey, OptionsDefine.Token},
        )

    def test_sensitive_fields_are_subset_of_cred_list(self):
        bc = BasicConfigure()
        for field in bc.sensitive_cred_fields:
            self.assertIn(field, bc.cred_list)


# ----------------------------------------------------------------------------
# 9. ConfigureCommand 交互式录入路径
# ----------------------------------------------------------------------------
from tccli.configure import ConfigureCommand, ConfigureHelp, ConfigureDocumentHandler


class TestConfigureCommandInteractive(_ConfigureCmdTestBase):
    def _run_interactive(self, responses):
        # 依次返回 responses 的每个字符串，作为 input() 的返回值
        it = iter(responses)
        with mock.patch("tccli.configure.ConfigureCommand._compat_input", side_effect=lambda prompt: next(it)):
            # 阻断 init_configures 中扫描全部服务模块产生的耗时/副作用
            with mock.patch.object(ConfigureCommand, "init_configures", lambda self: None):
                cmd = ConfigureCommand.__new__(ConfigureCommand)
                # 手动初始化 BasicConfigure
                super(ConfigureCommand, cmd).__init__()
                cmd._run_main(mock.Mock(), self._parsed_globals())

    def test_interactive_first_time_writes_inputs(self):
        # 顺序: secretId, secretKey, region, output
        self._run_interactive(["AKID_input_1234", "SK_input_5678", "ap-shanghai", "json"])
        cred = self._read_json(self._cred_path())
        conf = self._read_json(self._conf_path())
        self.assertEqual(cred[OptionsDefine.SecretId], "AKID_input_1234")
        self.assertEqual(cred[OptionsDefine.SecretKey], "SK_input_5678")
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Region], "ap-shanghai")
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Output], "json")

    def test_interactive_empty_response_keeps_defaults(self):
        # 已有配置时，四次回车应保留原值
        self._write_json(self._cred_path(), {
            OptionsDefine.SecretId: "AKID_existing_1234",
            OptionsDefine.SecretKey: "SK_existing_5678",
        })
        self._write_json(self._conf_path(), {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-beijing",
                OptionsDefine.Output: "table",
            },
        })
        self._run_interactive(["", "", "", ""])
        cred = self._read_json(self._cred_path())
        conf = self._read_json(self._conf_path())
        self.assertEqual(cred[OptionsDefine.SecretId], "AKID_existing_1234")
        self.assertEqual(cred[OptionsDefine.SecretKey], "SK_existing_5678")
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Region], "ap-beijing")
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Output], "table")

    def test_interactive_invalid_output_falls_back(self):
        self._run_interactive(["AKID_x_1234", "SK_y_5678", "ap-shanghai", "yaml"])
        conf = self._read_json(self._conf_path())
        self.assertEqual(conf[OptionsDefine.SysParam][OptionsDefine.Output], "json")


class TestConfigureCommandInitConfigures(_ConfigureCmdTestBase):
    def test_init_configures_creates_default_profile(self):
        # 阻断实际的用户输入
        with mock.patch.object(ConfigureCommand, "_run_main", lambda *a, **k: None):
            # 同时清空 sys.argv 里可能的 --profile 干扰
            with mock.patch.object(sys, "argv", ["tccli"]):
                ConfigureCommand()
        default_conf = os.path.join(self.cli_path, "default.configure")
        self.assertTrue(os.path.exists(default_conf))
        conf = self._read_json(default_conf)
        # 首次创建时会写入基础配置
        self.assertEqual(conf[OptionsDefine.SysParam]["region"], "ap-guangzhou")

    def test_init_configures_leaves_existing_profiles(self):
        # 预置一个非 default 的 profile
        other = os.path.join(self.cli_path, "other.configure")
        self._write_json(other, {OptionsDefine.SysParam: {"region": "ap-beijing"}})
        with mock.patch.object(ConfigureCommand, "_run_main", lambda *a, **k: None):
            with mock.patch.object(sys, "argv", ["tccli"]):
                ConfigureCommand()
        conf = self._read_json(other)
        self.assertEqual(conf[OptionsDefine.SysParam]["region"], "ap-beijing")


# ----------------------------------------------------------------------------
# 10. ConfigureHelp 与 ConfigureDocumentHandler
# ----------------------------------------------------------------------------
class TestConfigureHelp(unittest.TestCase):
    def test_help_renders_all_sections_without_error(self):
        # ConfigureListCommand 拥有完整的 metadata，选它作为宿主命令
        cmd = ConfigureListCommand.__new__(ConfigureListCommand)
        super(ConfigureListCommand, cmd).__init__()
        help_cmd = ConfigureHelp(cmd.NAME, cmd)
        with mock.patch.object(sys, "stdout", io.StringIO()) as fake_out:
            help_cmd([], mock.Mock())
        output = fake_out.getvalue()
        self.assertIn("DESCRIPTION", output)
        self.assertIn("USEAGE", output)

    def test_help_rejects_unknown_arguments(self):
        from tccli.exceptions import UnknownArgumentError
        cmd = ConfigureListCommand.__new__(ConfigureListCommand)
        super(ConfigureListCommand, cmd).__init__()
        help_cmd = ConfigureHelp(cmd.NAME, cmd)
        with self.assertRaises(UnknownArgumentError):
            help_cmd(["unknown-arg"], mock.Mock())


if __name__ == "__main__":
    unittest.main()
