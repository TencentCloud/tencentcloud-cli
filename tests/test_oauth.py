# -*- coding: utf-8 -*-
import json
import os
import shutil
import tempfile
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tccli import oauth
from tccli.plugins.auth import login as login_module


class TestOAuthHttpsVerification(unittest.TestCase):
    """OAuth 网络请求必须校验服务端 HTTPS 证书。"""

    @staticmethod
    def _response(data):
        response = mock.Mock()
        response.json.return_value = data
        return response

    def test_refresh_user_token_enables_certificate_verification(self):
        response = self._response({
            "AccessToken": "new-access-token",
            "ExpiresAt": 123456,
        })
        with mock.patch.object(
                oauth.requests, "post", return_value=response) as post:
            result = oauth.refresh_user_token(
                "refresh-token", "open-id", "cn")

        args, kwargs = post.call_args
        self.assertEqual(
            args[0], oauth._API_ENDPOINT + "/refresh_user_token")
        self.assertIs(kwargs["verify"], True)
        self.assertEqual(kwargs["json"]["RefreshToken"], "refresh-token")
        self.assertEqual(kwargs["json"]["OpenId"], "open-id")
        self.assertEqual(kwargs["json"]["Site"], "cn")
        self.assertEqual(result, {
            "accessToken": "new-access-token",
            "expiresAt": 123456,
        })

    def test_get_temp_cred_enables_certificate_verification(self):
        response = self._response({
            "SecretId": "secret-id",
            "SecretKey": "secret-key",
            "Token": "token",
            "ExpiresAt": 123456,
        })
        with mock.patch.object(
                oauth.requests, "post", return_value=response) as post:
            result = oauth.get_temp_cred("access-token", "cn")

        args, kwargs = post.call_args
        self.assertEqual(
            args[0], oauth._API_ENDPOINT + "/get_temp_cred")
        self.assertIs(kwargs["verify"], True)
        self.assertEqual(kwargs["json"]["AccessToken"], "access-token")
        self.assertEqual(kwargs["json"]["Site"], "cn")
        self.assertEqual(result, {
            "secretId": "secret-id",
            "secretKey": "secret-key",
            "token": "token",
            "expiresAt": 123456,
        })


class TestOAuthCredentialReplacement(unittest.TestCase):
    """OAuth 登录成功后原子替换旧 credential。"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_oauth_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")
        self.path_patcher = mock.patch.object(
            oauth, "cred_path_of_profile", return_value=self.cred_path)
        self.path_patcher.start()

    def tearDown(self):
        self.path_patcher.stop()
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write_credential(self, data):
        with open(self.cred_path, "w") as cred_file:
            json.dump(data, cred_file)

    def _read_credential(self):
        with open(self.cred_path, "r") as cred_file:
            return json.load(cred_file)

    @staticmethod
    def _token():
        return {
            "openId": "open-id",
            "accessToken": "access-token",
            "expiresAt": 2000,
            "refreshToken": "refresh-token",
            "site": "cn",
        }

    @staticmethod
    def _credential():
        return {
            "secretId": "NEW_ID",
            "secretKey": "NEW_KEY",
            "token": "NEW_TOKEN",
            "expiresAt": 1000,
        }

    def test_success_replaces_cvm_role_with_oauth_credential(self):
        """OAuth 登录成功后清除 CVM Role 并切换为完整 OAuth credential。"""
        self._write_credential({"type": "cvm-role", "secretId": "OLD_ID"})
        oauth.save_credential(self._token(), self._credential(), "default")
        data = self._read_credential()
        self.assertEqual(data["type"], "oauth")
        self.assertEqual(data["secretId"], "NEW_ID")
        self.assertEqual(data["secretKey"], "NEW_KEY")
        self.assertEqual(data["token"], "NEW_TOKEN")
        self.assertEqual(data["oauth"]["refreshToken"], "refresh-token")

    def test_atomic_replace_failure_preserves_old_credential(self):
        """原子替换失败时旧 CVM Role credential 保持不变。"""
        old_cred = {"type": "cvm-role", "secretId": "OLD_ID"}
        self._write_credential(old_cred)
        with mock.patch("tccli.utils.os.rename", side_effect=OSError("rename failed")):
            with self.assertRaises(Exception):
                oauth.save_credential(self._token(), self._credential(), "default")
        self.assertEqual(self._read_credential(), old_cred)

    def test_login_failure_preserves_old_credential(self):
        """OAuth 登录流程失败时不调用保存，旧 credential 保持不变。"""
        old_cred = {"type": "cvm-role", "secretId": "OLD_ID"}
        self._write_credential(old_cred)
        with mock.patch.object(
                login_module, "_get_token", side_effect=RuntimeError("login failed")):
            with mock.patch.object(oauth, "save_credential") as save_credential:
                with self.assertRaises(RuntimeError):
                    login_module.login(True, "default", "zh-CN")
        save_credential.assert_not_called()
        self.assertEqual(self._read_credential(), old_cred)


if __name__ == "__main__":
    unittest.main()
