# -*- coding:utf-8 -*-
"""
recursive-nesting-30：CliUnfoldArgument 单元测试。

覆盖目标：
  1. ``convert_to_dict`` 对任意深度（含 30 段自引用 / D=61）的扁平 key 仍能正确
     构造嵌套 dict；
  2. ``handle_array`` 对纯数字键正确转 list、对混合键报错；
  3. ``build_action_parameters`` 接受可选 ``extra_unfold_args`` 时，能把它和已注册
     的 argparse Namespace 合并；``None`` / 空 dict 行为与改动前一致；
  4. 红线（需求 1.4）：输出嵌套不补 None / 空 dict。

注意：本文件不依赖任何 services/*/v*/api.json，便于 CI 在仓库瘦身后仍可运行。
"""

import argparse

import pytest

from tccli.cli_unfold_argument import CliUnfoldArgument
from tccli.exceptions import UnknownArgumentError


# ============================================================
# 工具：用 argparse.Namespace 模拟 argparse 解析后的扁平参数
# ============================================================
def _ns(**kwargs):
    """构造 ``argparse.Namespace``，其 ``__dict__`` 即 ``vars(ns)``。"""
    return argparse.Namespace(**kwargs)


def _build_unfold_arg():
    return CliUnfoldArgument()


# ============================================================
# A. convert_to_dict 基本行为
# ============================================================
def test_A1_convert_to_dict_simple_flat_key():
    """A1: 单段 key 直接落到 params_set 顶层。"""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "Foo", "v")
    assert bag == {"Foo": "v"}


def test_A2_convert_to_dict_two_level():
    """A2: 两段 key 递归创建一层 dict。"""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "A.B", "v")
    assert bag == {"A": {"B": "v"}}


def test_A3_convert_to_dict_with_array_index():
    """A3: 含数字段的 key 在 convert_to_dict 阶段仍是 dict，依赖 handle_array 转 list。"""
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, "A.0.B", "v")
    assert bag == {"A": {"0": {"B": "v"}}}


# ============================================================
# B. convert_to_dict 在 D=5 / D=7 / D=61（30 段自引用）三档的正确性
# ============================================================
def _build_self_ref_keys(num_levels):
    """构造 ``num_levels`` 段自引用扁平 key。

    每段为 ``Children.0``，整体形如 ``Children.0.Children.0...LeafField``。
    返回 (key, depth)。
    """
    parts = ["Children", "0"] * num_levels + ["LeafField"]
    key = ".".join(parts)
    return key, len(parts)


def test_B3_convert_to_dict_depth_61_self_ref_30_levels():
    """B3: 30 段自引用（D=61）能正确构造嵌套；不会触发递归限制。"""
    key, depth = _build_self_ref_keys(30)
    assert depth == 61

    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, key, "deep_value")

    # 顺着 30 层 Children/0 走到末端 LeafField
    cursor = bag
    for _ in range(30):
        assert "Children" in cursor
        cursor = cursor["Children"]
        assert "0" in cursor
        cursor = cursor["0"]
    assert cursor == {"LeafField": "deep_value"}


# ============================================================
# C. handle_array 配套行为：30 层自引用经 handle_array 后 list 下标对齐
# ============================================================
def test_C1_handle_array_depth_61_no_padding():
    """C1: D=61 经 handle_array 后嵌套结构仍然不补 None / 空 dict（红线 1.4）。"""
    key, _ = _build_self_ref_keys(30)
    arg = _build_unfold_arg()
    bag = {}
    arg.convert_to_dict(bag, key, "deep_value")
    out = arg.handle_array(bag, "--")

    # 期望：每一层都是 {"Children": [{...}]}（list 长度 1，下标 0）
    cursor = out
    for _ in range(30):
        assert isinstance(cursor, dict)
        assert "Children" in cursor
        children = cursor["Children"]
        assert isinstance(children, list)
        assert len(children) == 1, "list 应严格只有下标 0，不补 None"
        cursor = children[0]
    # 末端是 dict 而非 None
    assert cursor == {"LeafField": "deep_value"}


def test_C2_handle_array_rejects_non_consecutive_index():
    """C2: handle_array 对不连续下标（1 而无 0）按既有约定报错——回归保护，不应受本次改动影响。"""
    arg = _build_unfold_arg()
    bag = {"A": {"1": "v"}}  # 缺少 "0"
    with pytest.raises(UnknownArgumentError):
        arg.handle_array(bag, "--")


# ============================================================
# D. build_action_parameters 接收 extra_unfold_args 注入
# ============================================================
def test_D1_build_action_parameters_without_extra_args_unchanged():
    """D1: 不传 extra_unfold_args 时与改动前完全一致。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v", "A.1.B": "w"})
    out = arg.build_action_parameters(ns)
    assert out == {"A": [{"B": "v"}, {"B": "w"}]}


def test_D2_build_action_parameters_with_none_extra_args_unchanged():
    """D2: 传 None / 空 dict 行为同 D1。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v"})
    assert arg.build_action_parameters(ns, extra_unfold_args=None) == {"A": [{"B": "v"}]}
    assert arg.build_action_parameters(_ns(**{"A.0.B": "v"}), extra_unfold_args={}) \
        == {"A": [{"B": "v"}]}


def test_D3_build_action_parameters_extra_args_merge_with_namespace():
    """D3: extra_unfold_args 与 Namespace 合并构造同一个嵌套结构（D=5）。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"Outer.Inner": "registered"})
    extra = {"Outer.Deep.0.X": "v1", "Outer.Deep.0.Y": "v2"}
    out = arg.build_action_parameters(ns, extra_unfold_args=extra)
    assert out == {
        "Outer": {
            "Inner": "registered",
            "Deep": [{"X": "v1", "Y": "v2"}],
        },
    }


def test_D4_build_action_parameters_extra_args_depth_61():
    """D4: extra_unfold_args 单独承载 D=61 的扁平 key，仍能正确构造 30 层嵌套。

    端到端覆盖路径：未注册到 argparse 的深嵌套 key → 由 command.py 兜底分支收集 →
    经 build_action_parameters(extra_unfold_args=...) → convert_to_dict + handle_array
    输出请求体。
    """
    key, _ = _build_self_ref_keys(30)
    arg = _build_unfold_arg()
    ns = _ns()  # 空 Namespace —— Namespace 自身只能挂注册过的扁平 key
    out = arg.build_action_parameters(ns, extra_unfold_args={key: "deep_value"})

    cursor = out
    for _ in range(30):
        assert isinstance(cursor, dict)
        assert "Children" in cursor
        children = cursor["Children"]
        assert isinstance(children, list) and len(children) == 1
        cursor = children[0]
    assert cursor == {"LeafField": "deep_value"}


def test_D5_build_action_parameters_extra_args_skip_none_values():
    """D5: extra_unfold_args 中 value 为 None 的项被跳过（与 Namespace 行为一致）。"""
    arg = _build_unfold_arg()
    ns = _ns()
    out = arg.build_action_parameters(
        ns,
        extra_unfold_args={"A.0.B": "v", "A.0.C": None},
    )
    assert out == {"A": [{"B": "v"}]}


# ============================================================
# E. 旧版兼容路径（build_action_parameters_old / gen_param_dict / merge_dict）
# ============================================================
def test_E1_gen_param_dict_simple_flat_key():
    """E1: gen_param_dict 处理单段 key。"""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"Foo": "v"})
    assert out == [{"Foo": "v"}]


def test_E2_gen_param_dict_array_index():
    """E2: gen_param_dict 处理含数字下标 key，构造预填 None 的 list。"""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"A.0.B": "v"})
    assert isinstance(out, list) and len(out) == 1
    assert out[0]["A"][0]["B"] == "v"


def test_E3_gen_param_dict_no_array_two_seg():
    """E3: gen_param_dict 单层无下标 key 直接挂值。"""
    arg = _build_unfold_arg()
    out = arg.gen_param_dict({"A.B": "v"})
    assert out == [{"A": {"B": "v"}}]


def test_E4_internal_gen_param_dict_empty_param():
    """E4: _gen_param_dict 入参为空时直接返回空 dict。"""
    arg = _build_unfold_arg()
    bag = {}
    out = arg._gen_param_dict([], bag)
    assert bag == {}


def test_E5_internal_gen_param_dict_three_seg_with_index():
    """E5: _gen_param_dict 处理 3 段含数字下标参数。"""
    arg = _build_unfold_arg()
    bag = {}
    arg._gen_param_dict(["A", "0", "x"], bag)
    assert bag == {"A": ["x"]}


def test_E6_internal_gen_param_dict_three_seg_object():
    """E6: _gen_param_dict 处理 3 段无下标参数。"""
    arg = _build_unfold_arg()
    bag = {}
    arg._gen_param_dict(["A", "B", "v"], bag)
    assert bag == {"A": {"B": "v"}}


def test_E7_recur_merge_dict_dict_branch():
    """E7: recur_merge_dict 在两个 dict 上递归合并新 key。"""
    arg = _build_unfold_arg()
    src = {"A": {"X": "1"}}
    dis = {"A": {"Y": "2"}}
    out = arg.recur_merge_dict(src, dis)
    assert out == {"A": {"X": "1", "Y": "2"}}


def test_E8_recur_merge_dict_list_branch():
    """E8: recur_merge_dict 在 list 上按下标合并标量 / dict 元素。"""
    arg = _build_unfold_arg()
    src = [{"X": "1"}, "scalar2"]
    dis = [{"Y": "2"}, None]
    out = arg.recur_merge_dict(src, dis)
    # list[0] 走 dict 递归，list[1] 走标量赋值
    assert out[0] == {"X": "1", "Y": "2"}
    assert out[1] == "scalar2"


def test_E9_merge_dict_empty_returns_empty():
    """E9: merge_dict 空列表返回空 dict。"""
    arg = _build_unfold_arg()
    assert arg.merge_dict([]) == {}


def test_E10_merge_dict_disjoint_keys():
    """E10: merge_dict 两个互斥 key 字典合并为一个。"""
    arg = _build_unfold_arg()
    out = arg.merge_dict([{"A": "1"}, {"B": "2"}])
    assert out == {"A": "1", "B": "2"}


def test_E11_merge_dict_overlapping_keys_recurse():
    """E11: merge_dict 重叠 key 递归合并子结构。"""
    arg = _build_unfold_arg()
    out = arg.merge_dict([
        {"A": {"X": "1"}},
        {"A": {"Y": "2"}},
    ])
    assert out == {"A": {"X": "1", "Y": "2"}}


def test_E12_build_action_parameters_old_simple():
    """E12: build_action_parameters_old 旧路径——单层无下标 key。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.B": "v"})
    out = arg.build_action_parameters_old(ns)
    assert out == {"A": {"B": "v"}}


def test_E13_build_action_parameters_old_with_array():
    """E13: build_action_parameters_old 旧路径——含数字下标 key。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.0.B": "v1", "A.1.B": "v2"})
    out = arg.build_action_parameters_old(ns)
    assert out["A"][0]["B"] == "v1"
    assert out["A"][1]["B"] == "v2"


def test_E14_build_action_parameters_old_skips_none():
    """E14: build_action_parameters_old 旧路径——value 为 None 的项被跳过。"""
    arg = _build_unfold_arg()
    ns = _ns(**{"A.B": "v", "A.C": None})
    out = arg.build_action_parameters_old(ns)
    assert out == {"A": {"B": "v"}}
