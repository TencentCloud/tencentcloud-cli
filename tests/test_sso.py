# -*- coding: utf-8 -*-
import json
import os
import shutil
import sys
import tempfile
import time
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

_BUILTINS_MODULE = "__builtin__" if sys.version_info[0] == 2 else "builtins"

from tccli import sso as sso_module
from tccli.plugins.sso import login as login_module


def _make_cred_resp():
    """构造 assume_role_with_saml 的模拟返回值。"""
    return {
        "Credentials": {
            "TmpSecretId": "sid",
            "TmpSecretKey": "skey",
            "Token": "tok",
        },
        "ExpiredTime": int(time.time()) + 7200,
    }


def _make_sso_info():
    """构造 sso_info 基础字段。"""
    return {
        "token": "t",
        "uin": 123,
        "roleConfigurationId": "rid",
        "roleConfigurationName": "rname",
        "zoneId": "z",
        "site": "ap",
        "authUrl": "https://example.com",
        "expiresAt": int(time.time()) + 3600 * 12,
    }


def _make_refresh_credential(now, sso_remaining):
    """构造即将过期、可进入自动刷新流程的 SSO credential。"""
    return {
        "type": "sso",
        "expiresAt": now + 10,
        "sso": {
            "expiresAt": now + sso_remaining,
            "token": "t",
            "uin": 123,
            "roleConfigurationId": "rid",
            "roleConfigurationName": "rname",
            "zoneId": "z",
            "site": "ap",
            "authUrl": "https://example.com",
        },
    }


# ---------------------------------------------------------------------------
# TestSaveCredential
# ---------------------------------------------------------------------------

class TestSaveCredential(unittest.TestCase):
    """SSO 登录成功后原子替换旧 credential。"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_sso_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")
        self.path_patcher = mock.patch.object(
            sso_module, "cred_path_of_profile", return_value=self.cred_path)
        self.path_patcher.start()

    def tearDown(self):
        self.path_patcher.stop()
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _write_old_credential(self, data):
        with open(self.cred_path, "w") as cred_file:
            json.dump(data, cred_file)

    def _read_credential(self):
        with open(self.cred_path, "r") as cred_file:
            return json.load(cred_file)

    def _call_save(self, sso_info=None):
        sso_module.save_credential(
            _make_cred_resp(), sso_info or _make_sso_info(), "default")
        return self._read_credential()

    def test_legacy_default_duration_is_not_persisted(self):
        """即使输入包含旧字段，保存的新 credential 也应丢弃它。"""
        sso_info = _make_sso_info()
        sso_info["defaultDuration"] = 34200
        data = self._call_save(sso_info)
        self.assertNotIn("defaultDuration", data["sso"])

    def test_success_replaces_cvm_role_with_sso_credential(self):
        """SSO 登录成功后清除 CVM Role 并切换为完整 SSO credential。"""
        self._write_old_credential({"type": "cvm-role", "secretId": "OLD_ID"})
        data = self._call_save()
        self.assertEqual(data["type"], "sso")
        self.assertEqual(data["secretId"], "sid")
        self.assertEqual(data["secretKey"], "skey")
        self.assertEqual(data["token"], "tok")
        self.assertNotIn("defaultDuration", data["sso"])

    def test_atomic_replace_failure_preserves_old_credential(self):
        """原子替换失败时旧 CVM Role credential 保持不变。"""
        old_cred = {"type": "cvm-role", "secretId": "OLD_ID"}
        self._write_old_credential(old_cred)
        with mock.patch("tccli.utils.os.rename", side_effect=OSError("rename failed")):
            with self.assertRaises(Exception):
                self._call_save()
        self.assertEqual(self._read_credential(), old_cred)


# ---------------------------------------------------------------------------
# TestLoginDuration
# ---------------------------------------------------------------------------

class TestLoginDuration(unittest.TestCase):
    """login.py 单次 duration 参数的解析、校验和传递。"""

    def _run_login(self, args, legacy_duration=None):
        cred_data = {"sso": {"authUrl": "https://example.com"}}
        if legacy_duration is not None:
            cred_data["sso"]["defaultDuration"] = legacy_duration

        login_args = {"uin": "123", "rolename": "rname"}
        login_args.update(args)
        patchers = [
            ("open", mock.patch(_BUILTINS_MODULE + ".open", mock.mock_open(read_data=json.dumps(cred_data)))),
            ("exists", mock.patch.object(login_module.os.path, "exists", return_value=True)),
            ("cred_path", mock.patch.object(
                login_module.sso, "cred_path_of_profile", return_value="/tmp/default.credential")),
            ("get_token", mock.patch.object(
                login_module, "_get_token",
                side_effect=lambda auth_url, state, language: {
                    "State": state, "Token": "login-token", "Site": "ap"
                })),
            ("accounts", mock.patch.object(
                login_module.sso, "list_accounts_for_access_assignment",
                return_value=[{"Uin": 123, "Name": "account"}])),
            ("roles", mock.patch.object(
                login_module.sso, "list_role_configurations_for_account",
                return_value=[{"RoleConfigurationName": "rname", "RoleConfigurationId": "rid"}])),
            ("gen_saml", mock.patch.object(
                login_module.sso, "gen_saml_response", return_value={"SAMLResponse": "saml"})),
            ("verify", mock.patch.object(
                login_module.sso, "verify_login_skey", return_value={"ZoneId": "zone"})),
            ("assume", mock.patch.object(
                login_module.sso, "assume_role_with_saml", return_value=_make_cred_resp())),
            ("save", mock.patch.object(login_module.sso, "save_credential")),
            ("print", mock.patch.object(login_module, "print_message")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            login_module.login(login_args, "default", "zh-CN")
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    def test_cli_duration_is_used_only_for_current_login(self):
        """命令行 duration 传给 STS，但不写入 credential 配置。"""
        mocks = self._run_login({"duration": 34200})
        self.assertEqual(mocks["assume"].call_args[0][4], 34200)
        saved_sso_info = mocks["save"].call_args[0][1]
        self.assertNotIn("defaultDuration", saved_sso_info)

    def test_default_duration_ignores_legacy_persisted_duration(self):
        """未传参数时使用默认值，不读取历史 defaultDuration。"""
        mocks = self._run_login({}, legacy_duration=34200)
        self.assertEqual(mocks["assume"].call_args[0][4], login_module._DURATION_DEFAULT)

    def test_duration_boundaries_are_accepted(self):
        """1800 和 43200 两个边界值均可传给 STS。"""
        for duration in (1800, 43200):
            mocks = self._run_login({"duration": duration})
            self.assertEqual(mocks["assume"].call_args[0][4], duration)

    def test_out_of_range_duration_stops_before_login_flow(self):
        """越界值应在读取凭证、打开浏览器前被拒绝。"""
        for duration in (1799, 43201):
            with mock.patch.object(login_module.sso, "cred_path_of_profile") as cred_path:
                with mock.patch.object(login_module, "_get_token") as get_token:
                    with mock.patch.object(login_module, "print_message") as print_message:
                        login_module.login({"duration": duration}, "default", "zh-CN")
            cred_path.assert_not_called()
            get_token.assert_not_called()
            self.assertIn("duration", print_message.call_args[0][0])


# ---------------------------------------------------------------------------
# TestLoginCredentialReplacement
# ---------------------------------------------------------------------------

class TestLoginCredentialReplacement(unittest.TestCase):
    """SSO 登录失败时保留旧 credential。"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp(prefix="tccli_sso_login_test_")
        self.cred_path = os.path.join(self.temp_dir, "default.credential")
        self.old_cred = {
            "type": "cvm-role",
            "secretId": "OLD_ID",
            "sso": {"authUrl": "https://example.com"},
        }
        with open(self.cred_path, "w") as cred_file:
            json.dump(self.old_cred, cred_file)

    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_login_failure_preserves_old_credential(self):
        """SSO 网络登录失败时不保存新凭证，旧 CVM Role 保持不变。"""
        with mock.patch.object(
                login_module.sso, "cred_path_of_profile", return_value=self.cred_path):
            with mock.patch.object(
                    login_module, "_get_token", side_effect=RuntimeError("login failed")):
                with mock.patch.object(login_module.sso, "save_credential") as save_credential:
                    with self.assertRaises(RuntimeError):
                        login_module.login({}, "default", "zh-CN")
        save_credential.assert_not_called()
        with open(self.cred_path, "r") as cred_file:
            self.assertEqual(json.load(cred_file), self.old_cred)


# ---------------------------------------------------------------------------
# TestAutoRefresh
# ---------------------------------------------------------------------------

class TestAutoRefresh(unittest.TestCase):
    """sso.py 自动刷新逻辑。"""

    def _run_refresh(self, sso_remaining, time_values=None):
        now = 100000.0
        cred = _make_refresh_credential(now, sso_remaining)
        patchers = [
            ("open", mock.patch(_BUILTINS_MODULE + ".open", mock.mock_open(read_data=json.dumps(cred)))),
            ("time", mock.patch.object(
                sso_module.time, "time", side_effect=time_values or [now, now])),
            ("gen_saml", mock.patch.object(
                sso_module, "gen_saml_response", return_value={"SAMLResponse": "saml"})),
            ("assume", mock.patch.object(
                sso_module, "assume_role_with_saml", return_value=_make_cred_resp())),
            ("save", mock.patch.object(sso_module, "save_credential")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            sso_module.maybe_refresh_credential("default")
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    def test_refresh_minimum_session_remaining_is_300(self):
        """刷新下限与 SSO 自动刷新安全窗口一致。"""
        self.assertEqual(sso_module._SKEY_REFRESH_SAFE_DUR, 300)

    def test_no_refresh_below_minimum_session_remaining(self):
        """SSO 会话剩余不足 300 秒时不再尝试刷新。"""
        mocks = self._run_refresh(299)
        mocks["gen_saml"].assert_not_called()
        mocks["assume"].assert_not_called()

    def test_refresh_accepts_minimum_session_remaining(self):
        """SSO 会话恰好剩余 300 秒时可申请对应有效期凭证。"""
        mocks = self._run_refresh(300)
        self.assertEqual(mocks["assume"].call_args[0][4], 300)

    def test_refresh_duration_capped_by_session_remaining(self):
        """会话剩余不足默认值时，刷新凭证有效期应截断至会话剩余时间。"""
        mocks = self._run_refresh(3000)
        self.assertEqual(mocks["assume"].call_args[0][4], 3000)

    def test_refresh_duration_uses_default_when_session_sufficient(self):
        """会话剩余充足时，刷新凭证有效期使用默认值。"""
        mocks = self._run_refresh(36000)
        self.assertEqual(mocks["assume"].call_args[0][4], sso_module._CRED_DEFAULT_DUR)

    def test_refresh_checks_session_with_current_time(self):
        """计算会话剩余时间时若已不足 300 秒，不生成 SAML。"""
        now = 100000.0
        mocks = self._run_refresh(400, time_values=[now, now + 101])
        mocks["gen_saml"].assert_not_called()
        mocks["assume"].assert_not_called()


if __name__ == "__main__":
    unittest.main()
