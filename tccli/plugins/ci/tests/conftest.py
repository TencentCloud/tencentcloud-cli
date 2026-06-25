# -*- coding: utf-8 -*-
"""
conftest.py — 自动将项目根目录加入 sys.path，
使 `from tccli.plugins.ci.xxx import ...` 在任何位置运行 pytest 时都能正确解析。
"""

import os
import sys

# tccli/plugins/ci/tests/ -> 上溯 4 级到包含 tccli/ 的根目录
_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
