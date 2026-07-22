# -*- coding: utf-8 -*-
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tccli.action_caller import GenericActionCaller


# ── convert_version_str ───────────────────────────────────────────────────────

@pytest.mark.parametrize("ver_input,expected", [
    ("v20170312", "2017-03-12"),
    ("v20230101", "2023-01-01"),
])
def test_convert_version_str(ver_input, expected):
    assert GenericActionCaller.convert_version_str(ver_input) == expected
