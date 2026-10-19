# -*- coding: utf-8 -*-
import os
import sys
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

_BUILTINS_MODULE = "__builtin__" if sys.version_info[0] == 2 else "builtins"

from tccli.plugins.sso import terminal


_ITEMS = ["alpha", "beta", "gamma"]


class TestSelectFromItemsUnix(unittest.TestCase):
    """Unix 选择器的默认光标、回车和退格。"""

    def _run(self, keys, default=0, items=None, page_size=10):
        with mock.patch.object(terminal, "_getch_wrap", side_effect=keys):
            with mock.patch.object(terminal.sys, "stdout"):
                return terminal._select_from_items_unix(
                    "prompt ", items or _ITEMS, page_size, default)

    def test_enter_returns_default_index(self):
        """直接回车选中默认下标，包括落在下一页的项。"""
        self.assertEqual(self._run([terminal._ENTER], default=2), 2)
        items = ["i%d" % i for i in range(12)]
        self.assertEqual(self._run([terminal._ENTER], default=11, items=items), 11)

    def test_empty_backspace_keeps_default_index(self):
        """搜索框为空时，退格不把光标打回第一项。"""
        idx = self._run([terminal._BACKSPACE, terminal._ENTER], default=2)
        self.assertEqual(idx, 2)

    def test_search_enter_returns_original_index(self):
        """输入搜索后回车，返回原始列表中的下标。"""
        idx = self._run(["b", terminal._ENTER], default=2)
        self.assertEqual(idx, 1)

    def test_backspace_after_search_resets_selection(self):
        """搜索框里有内容时，退格清空搜索并把光标回到第一项。"""
        idx = self._run(["b", terminal._BACKSPACE, terminal._ENTER], default=2)
        self.assertEqual(idx, 0)


class TestSelectFromItemsWin(unittest.TestCase):
    """Windows 选择器的默认下标。"""

    def _input_name(self):
        if sys.version_info[0] == 2:
            return "raw_input"
        return "input"

    def _run(self, answers, default=0, items=None):
        input_patch = mock.patch(
            _BUILTINS_MODULE + "." + self._input_name(), side_effect=answers)
        with input_patch:
            with mock.patch.object(terminal.sys, "stdout") as stdout:
                idx = terminal._select_from_items_win(
                    "choose: ", items or _ITEMS, 10, default)
        return idx, stdout

    def test_empty_input_returns_default_and_shows_it(self):
        """直接回车选中提示里给出的默认下标。"""
        idx, stdout = self._run([""], default=1)
        self.assertEqual(idx, 1)
        stdout.write.assert_any_call("choose: [1] ")

    def test_blank_input_returns_default(self):
        """只输入空白时同样使用默认下标。"""
        idx, _ = self._run(["  "], default=2)
        self.assertEqual(idx, 2)

    def test_numeric_input_returns_that_index(self):
        """输入合法数字时按数字选择。"""
        idx, _ = self._run(["1"], default=0)
        self.assertEqual(idx, 1)

    def test_invalid_input_is_retried(self):
        """非法输入会继续询问，直到得到合法下标。"""
        idx, _ = self._run(["x", "9", "0"], default=2)
        self.assertEqual(idx, 0)


class TestSelectFromItemsDispatch(unittest.TestCase):

    def test_public_selector_matches_platform(self):
        if os.name == "nt":
            self.assertIs(terminal.select_from_items, terminal._select_from_items_win)
        else:
            self.assertIs(terminal.select_from_items, terminal._select_from_items_unix)


if __name__ == "__main__":
    unittest.main()
