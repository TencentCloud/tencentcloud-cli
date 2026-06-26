# -*- coding: utf-8 -*-
"""
recursive-nesting-30：document_handler 单元测试。

覆盖目标：
  1. CLIDocumentHandler / ServiceDocumentHandler / ActionDocumentHandler
     三个类的 doc_help / 子方法行为；
  2. 自引用截断（members 为字符串）时正确渲染 ``<RecursiveRef:Type>`` 占位；
  3. _json_format / _handle_object_members / _complex_object_doc / _unfold_complex_object
     在 Array / Object / 基础类型 / 截断占位四种 members 形态下的分支；
  4. example / input_example / output_example / 各种 getters。
"""

import os
import sys

import pytest

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

import tccli.plugin as _plg  # noqa: E402

_plg.import_plugins = lambda: {}

from tccli import document_handler as dh  # noqa: E402


# ============================================================
# 工具：构造一个 fake doc 对象，把所有写入累积到 lines 里
# ============================================================
class _FakeStyle(object):
    def __init__(self, parent):
        self._p = parent
        self.indentation = 0

    def h1(self, text):
        self._p.lines.append("[H1]" + text)

    def h2(self, text):
        self._p.lines.append("[H2]" + text)

    def indent(self):
        self.indentation += 2
        self._p.lines.append("[INDENT]")

    def dedent(self):
        self.indentation = max(0, self.indentation - 2)
        self._p.lines.append("[DEDENT]")

    def new_line(self):
        self._p.lines.append("[NL]")

    def spaces(self):
        return " " * self.indentation


class _FakeDoc(object):
    def __init__(self):
        self.lines = []
        self.style = _FakeStyle(self)

    def write(self, text):
        self.lines.append(text)

    def doc_title(self, text):
        self.lines.append("[TITLE]" + text)

    def doc_title_indent(self, text):
        self.lines.append("[TITLE_INDENT]" + text)

    def doc_description(self, text):
        self.lines.append("[DESC]" + text)

    def doc_description_indent(self, text):
        self.lines.append("[DESC_INDENT]" + str(text))


def _flat(doc):
    return "\n".join(str(x) for x in doc.lines)


# ============================================================
# 工具：构造一个 stub Loader，按需注入返回值
# ============================================================
class _StubLoader(object):
    def __init__(self, **overrides):
        self._overrides = overrides

    def __getattr__(self, name):
        if name in self._overrides:
            val = self._overrides[name]
            if callable(val):
                return val
            return lambda *a, **kw: val
        raise AttributeError(name)


def _patch_loader(handler, **overrides):
    """把 handler 的 _cli_data 替换为 stub。"""
    handler._cli_data = _StubLoader(**overrides)
    return handler


# ============================================================
# A. CLIDocumentHandler
# ============================================================
def test_A1_cli_description_writes_h2_and_text():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(h, get_description=lambda: "tccli root description")
    h.description()
    flat = _flat(doc)
    assert "[H2]Description" in flat
    assert "tccli root description" in flat


def test_A2_cli_configure_writes_h2_and_text():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(h, get_configure=lambda: "configure-snippet")
    h.configure()
    flat = _flat(doc)
    assert "[H2]Configure" in flat
    assert "configure-snippet" in flat


def test_A3_cli_usage_writes_h2_and_text():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(h, get_usage=lambda: "tccli usage line")
    h.usage()
    flat = _flat(doc)
    assert "[H2]Usage" in flat
    assert "tccli usage line" in flat


def test_A4_cli_options_lists_each_option():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(h, get_options=lambda: {"--foo": "foo desc", "--bar": "bar desc"})
    h.options()
    flat = _flat(doc)
    assert "[H2]Options" in flat
    assert "--foo" in flat and "foo desc" in flat
    assert "--bar" in flat and "bar desc" in flat


def test_A5_cli_available_services_brief_default():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(h, get_available_services=lambda: {"cvm": [], "billing": []})
    h.available_services(detailed=False)
    flat = _flat(doc)
    assert "[H2]Available Services" in flat
    assert "[cvm]" in flat
    assert "[billing]" in flat
    assert "tccli help --detail" in flat


def test_A6_cli_available_services_detailed():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(
        h,
        get_available_services=lambda: {"svc-a": [], "svc-b": []},
        get_service_default_version=lambda s: "2024-01-01",
        get_service_description=lambda s, v: ("desc-" + s) if s == "svc-a" else "",
    )
    h.available_services(detailed=True)
    flat = _flat(doc)
    assert "svc-a" in flat
    assert "desc-svc-a" in flat
    # svc-b 没 description，不应崩溃且也应能完成 new_line
    assert "svc-b" in flat


def test_A7_cli_doc_help_combines_all_sections():
    doc = _FakeDoc()
    h = dh.CLIDocumentHandler(doc)
    _patch_loader(
        h,
        get_usage=lambda: "tccli usage",
        get_options=lambda: {"--x": "x"},
        get_available_services=lambda: {"svc": []},
    )
    h.doc_help(detailed=False)
    flat = _flat(doc)
    assert "[H2]Usage" in flat
    assert "[H2]Options" in flat
    assert "[H2]Available Services" in flat


# ============================================================
# B. ServiceDocumentHandler
# ============================================================
def test_B1_service_available_versions_marks_first_as_recommended():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(h, get_available_services=lambda: {"cvm": ["2017-03-12", "2016-09-01"]})
    h.available_versions()
    flat = _flat(doc)
    assert "2017-03-12  (recommended)" in flat
    assert "2016-09-01" in flat


def test_B2_service_description_handles_none():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(h, get_service_description=lambda s, v: None)
    h.description()
    flat = _flat(doc)
    assert "[H2]Description" in flat


def test_B3_service_usage():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(h, get_service_usage=lambda s: "tccli cvm usage")
    h.usage()
    flat = _flat(doc)
    assert "tccli cvm usage" in flat


def test_B4_service_options():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(h, get_service_options=lambda s: {"--profile": "profile desc"})
    h.options()
    flat = _flat(doc)
    assert "--profile" in flat
    assert "profile desc" in flat


def test_B5_service_available_actions_brief():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(
        h,
        get_actions_info=lambda s, v: {"DescribeInstances": {"name": "DescribeInstances desc"}},
    )
    h.available_actions(detail=False)
    flat = _flat(doc)
    assert "<DescribeInstances>" in flat
    assert "tccli cvm help --detail" in flat


def test_B6_service_available_actions_detail():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(
        h,
        get_actions_info=lambda s, v: {"A1": {"name": "A1 desc"}, "A2": {"name": "A2 desc"}},
    )
    h.available_actions(detail=True)
    flat = _flat(doc)
    assert "[TITLE_INDENT]A1" in flat
    assert "A1 desc" in flat
    assert "[TITLE_INDENT]A2" in flat


def test_B7_service_doc_help_combines_all_sections():
    doc = _FakeDoc()
    h = dh.ServiceDocumentHandler(doc, "cvm", "2017-03-12")
    _patch_loader(
        h,
        get_available_services=lambda: {"cvm": ["2017-03-12"]},
        get_service_description=lambda s, v: "cvm desc",
        get_service_usage=lambda s: "cvm usage",
        get_service_options=lambda s: {"--profile": "p"},
        get_actions_info=lambda s, v: {"X": {"name": "x"}},
    )
    h.doc_help(detail=False)
    flat = _flat(doc)
    assert "[H2]Available Versions" in flat
    assert "[H2]Description" in flat
    assert "[H2]Usage" in flat
    assert "[H2]Options" in flat
    assert "[H2]Available Actions" in flat


# ============================================================
# C. ActionDocumentHandler 基础方法
# ============================================================
def _make_action_handler(doc=None, action="Foo"):
    if doc is None:
        doc = _FakeDoc()
    h = dh.ActionDocumentHandler(doc, "svc", "2024-01-01", action)
    return h


def test_C1_action_description():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(h, get_action_description=lambda s, v, a: "action desc")
    h.description()
    flat = _flat(doc)
    assert "[H2]Description" in flat
    assert "svc-2024-01-01-Foo" in flat
    assert "action desc" in flat


def test_C2_action_usage():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(h, get_action_usage=lambda s, a: "tccli svc Foo")
    h.usage()
    flat = _flat(doc)
    assert "tccli svc Foo" in flat


def test_C3_action_options_brief():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    # keys 中最后一个被 pop 后插入到首位 —— 这里给 3 个 key 验证排序行为
    _patch_loader(
        h,
        get_action_options=lambda s, a: {"--profile": "p", "--region": "r", "--help": "h"},
    )
    h.options(detail=False)
    flat = _flat(doc)
    assert "[--help]" in flat or "[--profile]" in flat or "[--region]" in flat
    # brief 模式都用 [name] 形式
    assert "[--profile]" in flat
    assert "[--region]" in flat


def test_C4_action_options_detail():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_action_options=lambda s, a: {"--profile": "profile desc", "--help": "help desc"},
    )
    h.options(detail=True)
    flat = _flat(doc)
    assert "--profile" in flat and "profile desc" in flat
    assert "--help" in flat and "help desc" in flat


# ============================================================
# D. _json_format / _handle_object_members 各分支
# ============================================================
def test_D1_json_format_array_of_base_type_top_level():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    # indentation == 0 走 doc_description 分支
    h._json_format({"type": "Array", "members": ["string"]})
    flat = _flat(doc)
    assert "[string ...]" in flat


def test_D2_json_format_array_of_base_type_indented():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    doc.style.indentation = 4
    h._json_format({"type": "Array", "members": ["string"]})
    flat = _flat(doc)
    # indentation > 2 走 doc.write 分支
    assert "[string ...]" in flat


def test_D3_json_format_array_recursive_truncation():
    """D3: Array 自引用截断 → ``[<RecursiveRef:T> ...]``。"""
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._json_format({"type": "Array", "members": ["AllocationRuleExpression"]})
    flat = _flat(doc)
    assert "<RecursiveRef:AllocationRuleExpression>" in flat


def test_D4_json_format_array_recursive_truncation_indented():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    doc.style.indentation = 4
    h._json_format({"type": "Array", "members": ["Node"]})
    flat = _flat(doc)
    assert "<RecursiveRef:Node>" in flat


def test_D5_json_format_array_of_object():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {"K": {"type": "String", "members": "string"}}
    h._json_format({"type": "Array", "members": [members]})
    flat = _flat(doc)
    assert '"K": String' in flat
    assert "..." in flat


def test_D6_json_format_object_base_type_returns_quietly():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    # type != Array 且 members 是 BASE_TYPE 元素 → 直接 return，不写入
    h._json_format({"type": "string", "members": "string"})
    assert doc.lines == []


def test_D7_json_format_object_recursive_truncation():
    """D7: 非 Array 自引用截断 → ``<RecursiveRef:T>``。"""
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._json_format({"type": "Node", "members": "Node"})
    flat = _flat(doc)
    assert "<RecursiveRef:Node>" in flat


def test_D8_json_format_object_full_dict_members():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {"X": {"type": "String", "members": "string"}}
    h._json_format({"type": "Inner", "members": members})
    flat = _flat(doc)
    assert '"X": String' in flat


def test_D9_handle_object_members_array_field_inside():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {
        "A": {"type": "String", "members": "string"},
        "B": {"type": "Array", "members": ["string"]},
    }
    h._handle_object_members(members, "Object")
    flat = _flat(doc)
    assert '"A": String' in flat
    assert '"B": ' in flat
    assert "[string ...]" in flat


def test_D10_handle_object_members_nested_object_field():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {
        "Inner": {
            "type": "Inner",
            "members": {"X": {"type": "String", "members": "string"}},
        },
    }
    h._handle_object_members(members, "Object")
    flat = _flat(doc)
    assert '"X": String' in flat


# ============================================================
# E. _unfold_complex_object / _complex_object_doc
# ============================================================
def test_E1_unfold_complex_object_skips_base_type():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    # 非 Array 且 members 是 BASE_TYPE → 直接 return
    h._unfold_complex_object({"type": "string", "members": "string"})
    assert doc.lines == []


def test_E2_unfold_complex_object_skips_recursive_truncation():
    """E2: 非 Array 自引用截断（members=类型名字符串）应直接 return。"""
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._unfold_complex_object({"type": "Node", "members": "Node"})
    # 不应写入 JSON Syntax 标题
    flat = _flat(doc)
    assert "JSON Syntax" not in flat


def test_E3_unfold_complex_object_writes_json_syntax():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._unfold_complex_object({
        "type": "Inner",
        "members": {"X": {"type": "String", "members": "string"}},
    })
    flat = _flat(doc)
    assert "JSON Syntax" in flat
    assert '"X": String' in flat


def test_E4_complex_object_doc_skips_base_type_members():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._complex_object_doc({"members": "string"}, "Available Parameters")
    assert doc.lines == []


def test_E5_complex_object_doc_skips_recursive_truncation():
    """E5: members 为类型名字符串（自引用截断）→ 直接 return，不递归。"""
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._complex_object_doc({"members": "Node"}, "Available Parameters")
    # 不应进入 indent / 子成员遍历
    assert doc.lines == []


def test_E6_complex_object_doc_recurses_into_dict_members():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {
        "Sub": {
            "type": "String",
            "type_name": "String",
            "required": "Required",
            "document": "doc-of-sub",
            "members": "string",
        }
    }
    h._complex_object_doc({"members": members}, "Available Parameters")
    flat = _flat(doc)
    assert "doc-of-sub" in flat


def test_E7_complex_object_doc_skips_recursive_subfield():
    """E7: 子字段 members 为类型名字符串时不再继续递归（避免自引用循环）。"""
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    members = {
        "Self": {
            "type": "Node",
            "type_name": "Node",
            "required": "Optional",
            "document": "self ref",
            "members": "Node",  # ← 自引用占位
        }
    }
    h._complex_object_doc({"members": members}, "Available Parameters")
    flat = _flat(doc)
    assert "self ref" in flat


# ============================================================
# F. _param_type / _doc_title
# ============================================================
def test_F1_param_type_array():
    h = _make_action_handler()
    out = h._param_type({"type": "Array", "type_name": "ItemType"})
    assert out == "Array of ItemType"


def test_F2_param_type_non_array():
    h = _make_action_handler()
    out = h._param_type({"type": "String", "type_name": "String"})
    assert out == "String"


def test_F3_doc_title_available_parameters_includes_required():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._doc_title("Available Parameters", "Foo",
                 {"type": "String", "type_name": "String", "required": "Required"})
    flat = _flat(doc)
    assert "--Foo" in flat
    assert "String" in flat
    assert "Required" in flat


def test_F4_doc_title_output_parameter_form():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h._doc_title("Output Parameter", "Bar",
                 {"type": "String", "type_name": "String"})
    flat = _flat(doc)
    assert "Bar -> (String)" in flat


# ============================================================
# G. _base_parameter / available_parameter / output_parameter
# ============================================================
def _stub_get_param_info(params):
    def _impl(s, v, a):
        return params
    return _impl


def test_G1_base_parameter_empty_writes_无():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_param_info=_stub_get_param_info({}),
        get_output_param_info=_stub_get_param_info({}),
    )
    h._base_parameter("Available Parameters", detail=False)
    flat = _flat(doc)
    assert "[H2]Available Parameters" in flat
    assert "无" in flat


def test_G2_base_parameter_brief_lists_titles_and_help_hint():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_param_info=_stub_get_param_info({}),
        get_output_param_info=_stub_get_param_info({
            "RequestId": {
                "type": "String", "type_name": "String",
                "members": "string",
                "required": None,
                "document": "request-id-doc",
            }
        }),
    )
    h._base_parameter("Output Parameter", detail=False)
    flat = _flat(doc)
    assert "RequestId -> (String)" in flat
    assert "tccli svc Foo help --detail" in flat


def test_G3_base_parameter_detail_writes_doc_and_recurses():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_param_info=_stub_get_param_info({
            "RuleList": {
                "type": "Inner", "type_name": "Inner",
                "required": "Required",
                "document": "rule-list-doc",
                "members": {
                    "Sub": {
                        "type": "String", "type_name": "String",
                        "members": "string",
                        "required": "Optional",
                        "document": "sub-doc",
                    }
                },
            }
        }),
        get_output_param_info=_stub_get_param_info({}),
    )
    h._base_parameter("Available Parameters", detail=True)
    flat = _flat(doc)
    assert "rule-list-doc" in flat
    assert "JSON Syntax" in flat
    assert "sub-doc" in flat


def test_G4_available_parameter_and_output_parameter_call_through():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_param_info=_stub_get_param_info({}),
        get_output_param_info=_stub_get_param_info({}),
    )
    h.available_parameter(detail=False)
    h.output_parameter(detail=False)
    flat = _flat(doc)
    assert "[H2]Available Parameters" in flat
    assert "[H2]Output Parameter" in flat


def test_G5_get_param_info_method_property():
    h = _make_action_handler()
    pim = h.param_info_method
    assert "Available Parameters" in pim
    assert "Output Parameter" in pim


# ============================================================
# H. example / input_example / output_example
# ============================================================
def test_H1_input_example_with_params():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h.input_example(["--Id 1", "--Name foo"])
    flat = _flat(doc)
    assert "Input:" in flat
    assert "--cli-unfold-argument" in flat
    assert "--Id 1" in flat
    assert "--Name foo" in flat


def test_H2_input_example_empty():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h.input_example([])
    flat = _flat(doc)
    assert "Input:" in flat
    # 空入参不应抛异常


def test_H3_output_example_writes_under_indent():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    h.output_example("{\"R\":1}")
    flat = _flat(doc)
    assert "Output:" in flat
    assert "{\"R\":1}" in flat


def test_H4_example_iterates_loader_examples():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        generate_cli_example=lambda s, v, a: [
            {"title": "demo", "document": "demo doc",
             "input": ["--A x"], "output": "{\"R\":1}"},
        ],
    )
    h.example()
    flat = _flat(doc)
    assert "[H2]Examples" in flat
    assert "Example 1: demo" in flat
    assert "demo doc" in flat
    assert "--A x" in flat


# ============================================================
# I. doc_help 端到端（detail=True 与 detail=False）
# ============================================================
def test_I1_action_doc_help_detail_false_skips_description_and_example():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_action_description=lambda s, v, a: "should-not-appear",
        get_action_usage=lambda s, a: "tccli svc Foo",
        get_action_options=lambda s, a: {"--help": "h"},
        get_param_info=_stub_get_param_info({}),
        get_output_param_info=_stub_get_param_info({}),
        generate_cli_example=lambda s, v, a: [],
    )
    h.doc_help(detail=False)
    flat = _flat(doc)
    # detail=False 跳过 description 与 example
    assert "should-not-appear" not in flat
    assert "[H2]Examples" not in flat
    assert "[H2]Usage" in flat
    assert "[H2]Available Parameters" in flat
    assert "[H2]Output Parameter" in flat


def test_I2_action_doc_help_detail_true_includes_description_and_example():
    doc = _FakeDoc()
    h = _make_action_handler(doc)
    _patch_loader(
        h,
        get_action_description=lambda s, v, a: "real action description",
        get_action_usage=lambda s, a: "tccli svc Foo",
        get_action_options=lambda s, a: {"--help": "h"},
        get_param_info=_stub_get_param_info({}),
        get_output_param_info=_stub_get_param_info({}),
        generate_cli_example=lambda s, v, a: [
            {"title": "t", "document": "d", "input": [], "output": "o"}
        ],
    )
    h.doc_help(detail=True)
    flat = _flat(doc)
    assert "real action description" in flat
    assert "[H2]Examples" in flat
    assert "Example 1: t" in flat
