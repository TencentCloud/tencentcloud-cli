# -*- coding: utf-8 -*-
"""
针对 tccli/self_ref.py 环检测器的单元测试。

覆盖检测器的能力契约（不依赖任何 SDK / 真实 api.json）：
  A. _dfs_has_cycle 各种环形态：直接自环、间接环、多级环、无环、基础类型脱离。
  B. is_action_self_referencing 的 Request / Response 双入口口径。
  C. 异常兜底 fallback False。
"""
import os
import sys

try:
    import pytest  # noqa: F401
except ImportError:
    pass

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from tccli.self_ref import (  # noqa: E402
    _dfs_has_cycle, is_action_self_referencing,
)


def _obj(members):
    return {"members": members}


def _m(name, type_, member, required=True):
    return {"name": name, "type": type_, "member": member,
            "document": "", "required": required}


# ============================================================
# A. _dfs_has_cycle 环形态
# ============================================================
def test_A1_direct_self_cycle():
    """A→A：类型直接引用自身。"""
    objects = {"A": _obj([_m("Self", "object", "A", False)])}
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A2_indirect_cycle():
    """A→B→A：两级间接环。"""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToA", "object", "A", False)]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A3_multi_level_cycle():
    """A→B→C→A：多级环。"""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToC", "object", "C")]),
        "C": _obj([_m("ToA", "object", "A", False)]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is True


def test_A4_no_cycle_linear_chain():
    """A→B→C→(string)：线性无环。"""
    objects = {
        "A": _obj([_m("ToB", "object", "B")]),
        "B": _obj([_m("ToC", "object", "C")]),
        "C": _obj([_m("Leaf", "string", "string")]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


def test_A5_base_type_breaks_traversal():
    """基础类型成员不追索，不误判为环。"""
    objects = {
        "A": _obj([
            _m("Id", "string", "string"),
            _m("Count", "int", "int64", False),
        ]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


def test_A6_list_member_cycle():
    """List<A> 形式的自引用（如 Node.Children: list of Node）。"""
    objects = {
        "Node": _obj([
            _m("Val", "string", "string"),
            _m("Children", "list", "Node", False),
        ]),
    }
    assert _dfs_has_cycle(objects, "Node", frozenset(["Node"])) is True


def test_A7_diamond_no_cycle():
    """菱形共享类型但无环：A→B→D, A→C→D，D 为叶子。"""
    objects = {
        "A": _obj([_m("ToB", "object", "B"), _m("ToC", "object", "C")]),
        "B": _obj([_m("ToD", "object", "D")]),
        "C": _obj([_m("ToD", "object", "D")]),
        "D": _obj([_m("Leaf", "string", "string")]),
    }
    assert _dfs_has_cycle(objects, "A", frozenset(["A"])) is False


# ============================================================
# B. is_action_self_referencing 双入口口径
# ============================================================
def _model_request_cycle_only():
    """Request 有环、Response 无环。"""
    return {"objects": {
        "TreeRequest": _obj([_m("Root", "object", "Node")]),
        "TreeResponse": _obj([_m("Ok", "string", "string")]),
        "Node": _obj([_m("Self", "object", "Node", False)]),
    }}


def _model_response_cycle_only():
    """Request 无环、Response 有环。"""
    return {"objects": {
        "TreeRequest": _obj([_m("A", "string", "string")]),
        "TreeResponse": _obj([_m("Root", "object", "Node")]),
        "Node": _obj([_m("Self", "object", "Node", False)]),
    }}


def test_B1_request_side_detects_request_cycle():
    model = _model_request_cycle_only()
    assert is_action_self_referencing("s", "v", "Tree", model) is True
    # 默认 root_suffix="Request"
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Request") is True


def test_B2_request_side_ignores_response_cycle():
    """Request 无环时，输入侧默认判定为 False（即便 Response 有环）。"""
    model = _model_response_cycle_only()
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_B3_response_side_detects_response_cycle():
    """输出侧显式传 root_suffix='Response'，可检出 Response 环。"""
    model = _model_response_cycle_only()
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Response") is True


def test_B4_response_side_ignores_request_cycle():
    model = _model_request_cycle_only()
    assert is_action_self_referencing(
        "s", "v", "Tree", model, root_suffix="Response") is False


# ============================================================
# C. 异常兜底
#
# _dfs_has_cycle 本身只专注判环、不做防御性判断；坏数据（缺 objects/根类型/
# 悬空引用/members 非法）统一由 is_action_self_referencing 的 try/except 兜底为 False。
# 本组用例即验证这条外层容错契约。
# ============================================================
def test_C1_missing_objects_key_returns_false():
    assert is_action_self_referencing("s", "v", "X", {}) is False


def test_C2_none_service_model_returns_false():
    assert is_action_self_referencing("s", "v", "X", None) is False


def test_C3_missing_root_type_returns_false():
    """action 对应的根类型在 objects 中缺失时返回 False。"""
    model = {"objects": {"OtherRequest": _obj([_m("A", "string", "string")])}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C4_dangling_reference_returns_false():
    """悬空引用：字段 member 指向 objects 中不存在的类型，外层兜底为 False。"""
    model = {"objects": {
        "TreeRequest": _obj([_m("Root", "object", "NotThere", False)]),
    }}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C5_members_not_list_returns_false():
    """脏数据：根类型 members 非 list，外层兜底为 False。"""
    model = {"objects": {"TreeRequest": {"members": "not-a-list"}}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


def test_C6_non_dict_member_returns_false():
    """脏数据：members 中混入非 dict 元素，外层兜底为 False。"""
    model = {"objects": {"TreeRequest": {"members": ["garbage", 123]}}}
    assert is_action_self_referencing("s", "v", "Tree", model) is False


if __name__ == "__main__":
    import pytest as _pt
    sys.exit(_pt.main([os.path.abspath(__file__), "-v"]))
