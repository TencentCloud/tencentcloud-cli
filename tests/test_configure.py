# -*- coding: utf-8 -*-
import argparse
import os
import shutil
import tempfile
import unittest

import six

import tccli.options_define as OptionsDefine
from tccli.configure import ConfigureGetCommand, ConfigureListCommand, mask_secret
from tccli.utils import Utils


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


if __name__ == "__main__":
    unittest.main()
