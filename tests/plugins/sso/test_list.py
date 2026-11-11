# -*- coding: utf-8 -*-
import time
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from tccli.plugins.sso import list as list_module


_ACCOUNTS = [
    {"Uin": 123, "Name": "a"},
    {"Uin": 456, "Name": "b"},
]

_ROLES = [
    {"RoleConfigurationName": "role-a", "RoleConfigurationId": "rid-a"},
    {"RoleConfigurationName": "role-b", "RoleConfigurationId": "rid-b"},
]

_SESSION = {"token": "login-token", "site": "cn", "expiresAt": time.time() + 3600}


class _BaseCase(unittest.TestCase):

    def _run(self, entrypoint, session=_SESSION, args=None, accounts=None, roles=None, is_tty=True):
        patchers = [
            ("session", mock.patch.object(list_module.sso, "load_login_token", return_value=session)),
            ("accounts", mock.patch.object(
                list_module.sso, "list_accounts_for_access_assignment",
                return_value=_ACCOUNTS if accounts is None else accounts)),
            ("roles", mock.patch.object(
                list_module.sso, "list_role_configurations_for_account",
                return_value=_ROLES if roles is None else roles)),
            ("tty", mock.patch.object(list_module, "_stdin_is_terminal", return_value=is_tty)),
            ("print", mock.patch.object(list_module, "print_message")),
            ("err", mock.patch.object(list_module, "print_error")),
        ]
        mocks = {}
        try:
            for name, patcher in patchers:
                mocks[name] = patcher.start()
            try:
                mocks["rc"] = entrypoint(args or {}, {"language": "zh-CN", "profile": "default"})
            except SystemExit as e:
                # 失败路径靠 SystemExit 把退出码带给 tccli 的 main(), main() 不采用返回值
                mocks["rc"] = e.code
        finally:
            for _, patcher in reversed(patchers):
                patcher.stop()
        return mocks

    @staticmethod
    def _lines(mocks):
        """按行还原 stdout 输出。"""
        return [call[0][0] for call in mocks["print"].call_args_list]


class TestListUin(_BaseCase):

    def test_prints_one_account_per_line(self):
        """每行一个账号, 制表符分隔 uin 与名称, 不带表头与统计行。"""
        mocks = self._run(list_module.list_uin_command_entrypoint)
        self.assertEqual(mocks["rc"], 0)
        self.assertEqual(mocks["accounts"].call_args[0], ("login-token", "cn"))
        self.assertEqual(self._lines(mocks), ["123\ta", "456\tb"])

    def test_uin_is_printed_as_string(self):
        """uin 以大整数形式输出时保持字符串, 避免精度丢失后无法回填。"""
        mocks = self._run(
            list_module.list_uin_command_entrypoint,
            accounts=[{"Uin": 100000000001, "Name": "corp"}])
        self.assertEqual(self._lines(mocks), ["100000000001\tcorp"])

    def test_expired_login_ask_for_relogin(self):
        """登录态失效时只提示重新登录, 不发起接口调用。"""
        mocks = self._run(list_module.list_uin_command_entrypoint, session=None)
        self.assertNotEqual(mocks["rc"], 0)
        mocks["accounts"].assert_not_called()
        self.assertEqual(self._lines(mocks), [])
        self.assertIn("登录", mocks["err"].call_args[0][0])

    def test_no_account_reports_message(self):
        mocks = self._run(list_module.list_uin_command_entrypoint, accounts=[])
        self.assertNotEqual(mocks["rc"], 0)
        self.assertEqual(self._lines(mocks), [])
        self.assertIn("账号", mocks["err"].call_args[0][0])


class TestListRole(_BaseCase):

    def test_prints_uin_name_and_role_id_per_line(self):
        """每行 <uin>\t<role name>\t<role id>, 同一 role 在不同 uin 下 id 不同也不去重。"""
        mocks = self._run(list_module.list_role_command_entrypoint, args={"uin": "456"})
        self.assertEqual(mocks["rc"], 0)
        self.assertEqual(mocks["roles"].call_args[0], (456, "login-token", "cn"))
        self.assertEqual(self._lines(mocks), [
            "456\trole-a\trid-a",
            "456\trole-b\trid-b",
        ])

    def test_uin_is_converted_to_int_before_api_call(self):
        """TargetUin 在 CIC 侧是 int64, --uin 在 CLI 入口就转成整数再往下传。"""
        with mock.patch.object(list_module.sso, "load_login_token", return_value=_SESSION), \
                mock.patch.object(list_module.sso, "list_role_configurations_for_account",
                                  return_value=_ROLES) as roles, \
                mock.patch.object(list_module, "print_message"), \
                mock.patch.object(list_module, "print_error"):
            list_module.list_role_command_entrypoint(
                {"uin": "100000000001"}, {"language": "zh-CN", "profile": "default"})
        uin = roles.call_args[0][0]
        self.assertIsInstance(uin, int)
        self.assertEqual(uin, 100000000001)

    def test_picked_uin_is_int(self):
        with mock.patch.object(list_module, "_pick_uin", return_value=100000000001):
            mocks = self._run(list_module.list_role_command_entrypoint, args={})
        self.assertIsInstance(mocks["roles"].call_args[0][0], int)

    def test_uin_is_asked_interactively_when_omitted(self):
        """未传 --uin 时进入交互选择。"""
        with mock.patch.object(list_module.terminal, "select_from_items", return_value=1) as select:
            mocks = self._run(list_module.list_role_command_entrypoint)
        self.assertEqual(select.call_args[0][1], ["a:123", "b:456"])
        uin = mocks["roles"].call_args[0][0]
        self.assertIsInstance(uin, int)
        self.assertEqual(uin, 456)

    def test_expired_login_ask_for_relogin(self):
        mocks = self._run(list_module.list_role_command_entrypoint, session=None, args={"uin": "456"})
        self.assertNotEqual(mocks["rc"], 0)
        mocks["roles"].assert_not_called()
        self.assertIn("登录", mocks["err"].call_args[0][0])

    def test_no_role_reports_message(self):
        mocks = self._run(list_module.list_role_command_entrypoint, args={"uin": "456"}, roles=[])
        self.assertNotEqual(mocks["rc"], 0)
        self.assertEqual(self._lines(mocks), [])
        self.assertIn("角色", mocks["err"].call_args[0][0])

    def test_invalid_uin_reports_message(self):
        """非数字 uin 直接报错, 不把脏数据发给 CIC。"""
        mocks = self._run(list_module.list_role_command_entrypoint, args={"uin": "abc"})
        self.assertNotEqual(mocks["rc"], 0)
        mocks["roles"].assert_not_called()
        self.assertIn("abc", mocks["err"].call_args[0][0])

    def test_omitted_uin_without_terminal_fails_fast(self):
        """stdin 不是终端(管道/脚本)时不能进交互, 必须报错退出而不是卡住。"""
        mocks = self._run(list_module.list_role_command_entrypoint, args={}, is_tty=False)
        self.assertNotEqual(mocks["rc"], 0)
        mocks["roles"].assert_not_called()
        self.assertEqual(self._lines(mocks), [])
        self.assertIn("--uin", mocks["err"].call_args[0][0])


if __name__ == "__main__":
    unittest.main()
