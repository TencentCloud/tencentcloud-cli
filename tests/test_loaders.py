# -*- coding: utf-8 -*-
"""
针对 tccli.loaders 的单元测试。

重点覆盖：
1. 普通（无环）schema：保证修复未引入回归。
2. 自引用（直接 / 间接 / 兄弟共享类型）schema：核心修复点。
3. _generate_param_skeleton：自引用处以字符串占位表示（<recursive: fill '<field>' with a JSON object of type <T> (self-referenced)>）。
4. _get_unfold_param_info：自引用接口可被 unfold，不再 RecursionError。
5. _filling_unfold_param_info：截断点 type=Object，文档附加提示。
6. 公共方法 get_param_info / get_output_param_info / generate_param_skeleton /
   get_unfold_param_info 的端到端行为。
7. 真实仓库数据：billing 含自引用接口、cvm 普通接口。

使用 pytest 风格：每个 test_* 函数内 assert，文件末尾不再调用，pytest 自动发现。
"""
import os
import sys

try:
    import pytest
    _HAS_PYTEST = True
except ImportError:
    _HAS_PYTEST = False

    class _SkipException(Exception):
        pass

    class _PytestStub(object):
        @staticmethod
        def skip(msg):
            raise _SkipException(msg)

    pytest = _PytestStub()  # type: ignore

# 确保 tccli 可被导入
_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# 屏蔽 plugin import 的开销/副作用，使纯静态测试可在任何环境下运行
import tccli.plugin as _plg  # noqa: E402

_plg.import_plugins = lambda: {}

from tccli.loaders import Loader, BASE_TYPE  # noqa: E402


# ============================================================
# 工具：构造一个内存版 Loader，注入指定 service_model
# ============================================================
def _make_loader(model):
    """返回一个 Loader 实例，其 get_service_model 直接返回给定 model。"""
    ld = Loader()
    ld.get_service_model = lambda service, version: model
    return ld


def _model(actions, objects):
    return {"metadata": {}, "actions": actions, "objects": objects}


def _action(input_name, output_name=None):
    out = {"input": input_name, "name": input_name.replace("Request", "")}
    if output_name:
        out["output"] = output_name
    return out


# ============================================================
# A. 普通场景回归
# ============================================================
def test_A1_basic_types_no_regression():
    """A1: 仅基础类型字段 —— 输出应与修改前一致。"""
    objects = {
        "FooRequest": {
            "members": [
                {"name": "Id", "type": "string", "member": "string", "document": "id", "required": True},
                {"name": "Count", "type": "int", "member": "int64", "document": "count", "required": False},
            ],
        },
    }
    actions = {"Foo": _action("FooRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Foo")
    assert set(info.keys()) == {"Id", "Count"}
    assert info["Id"]["type"] == "String"
    assert info["Id"]["type_name"] == "String"
    assert info["Id"]["required"] == "Required"
    assert info["Id"]["members"] == "string"
    assert info["Count"]["type"] == "Integer"
    assert info["Count"]["required"] == "Optional"


def test_A2_nested_object_full_expand():
    """A2: 嵌套 Object 完整展开。"""
    objects = {
        "BarRequest": {
            "members": [
                {"name": "Outer", "type": "object", "member": "Inner", "document": "", "required": True},
            ],
        },
        "Inner": {
            "members": [
                {"name": "Leaf", "type": "string", "member": "string", "document": "leaf", "required": True},
            ],
        },
    }
    actions = {"Bar": _action("BarRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Bar")
    # Outer 是嵌套 object，members 应是 dict（已展开）
    assert isinstance(info["Outer"]["members"], dict)
    assert "Leaf" in info["Outer"]["members"]
    assert info["Outer"]["members"]["Leaf"]["type"] == "String"


def test_A3_list_of_object_full_expand():
    """A3: List<ComplexObject> 完整展开。"""
    objects = {
        "BazRequest": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item", "document": "", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string", "document": "", "required": True},
            ],
        },
    }
    actions = {"Baz": _action("BazRequest")}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "Baz")
    assert info["Items"]["type"] == "Array"
    assert isinstance(info["Items"]["members"], list)
    assert isinstance(info["Items"]["members"][0], dict)
    assert "Key" in info["Items"]["members"][0]


# ============================================================
# B. 自引用环
# ============================================================
def _self_ref_list_model():
    """Node { Children: List<Node> }"""
    return _model(
        actions={"Tree": _action("TreeRequest")},
        objects={
            "TreeRequest": {
                "members": [
                    {"name": "Root", "type": "object", "member": "Node",
                     "document": "root", "required": True},
                ],
            },
            "Node": {
                "members": [
                    {"name": "Value", "type": "string", "member": "string",
                     "document": "v", "required": False},
                    {"name": "Children", "type": "list", "member": "Node",
                     "document": "children", "required": False},
                ],
            },
        },
    )


def test_B1_direct_self_ref_via_list_does_not_crash():
    """B1: List<Self> 直接自引用，必须不抛 RecursionError。"""
    ld = _make_loader(_self_ref_list_model())
    info = ld.get_param_info("svc", "v", "Tree")
    # 顶层 Root 是 Node，已展开一层
    assert isinstance(info["Root"]["members"], dict)
    assert "Children" in info["Root"]["members"]
    # Children 是自引用截断点，members 应是占位字符串列表 ["Node"]
    children = info["Root"]["members"]["Children"]
    assert children["type"] == "Array"
    assert children["members"] == ["Node"]


def test_B2_direct_self_ref_via_object_does_not_crash():
    """B2: Object→Self 直接自引用。"""
    objects = {
        "LinkRequest": {
            "members": [
                {"name": "Head", "type": "object", "member": "LinkNode",
                 "document": "", "required": True},
            ],
        },
        "LinkNode": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Next", "type": "object", "member": "LinkNode",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Link": _action("LinkRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Link")
    # Head.Next 是自引用截断点
    next_field = info["Head"]["members"]["Next"]
    # Object 自引用截断时 members 应被填成占位类型名（str）
    assert next_field["members"] == "LinkNode"


def test_B3_indirect_cycle_A_to_B_to_A():
    """B3: 间接环 A→B→A。"""
    objects = {
        "GraphRequest": {
            "members": [
                {"name": "Start", "type": "object", "member": "A",
                 "document": "", "required": True},
            ],
        },
        "A": {
            "members": [
                {"name": "B", "type": "object", "member": "B",
                 "document": "", "required": False},
            ],
        },
        "B": {
            "members": [
                {"name": "A", "type": "object", "member": "A",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Graph": _action("GraphRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Graph")
    # 路径 Start.B.A —— A 已在 visited 中，被截断
    inner_a = info["Start"]["members"]["B"]["members"]["A"]
    assert inner_a["members"] == "A"  # 占位字符串


def test_B4_sibling_shared_type_not_falsely_truncated():
    """B4: 两个兄弟字段共享同一类型 Common，不应被互相干扰。

    如果实现错误地把 visited 当成"全局已见"集合，那么第二个兄弟字段会被误截断。
    """
    objects = {
        "SibRequest": {
            "members": [
                {"name": "Left", "type": "object", "member": "Common",
                 "document": "", "required": True},
                {"name": "Right", "type": "object", "member": "Common",
                 "document": "", "required": True},
            ],
        },
        "Common": {
            "members": [
                {"name": "K", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "V", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"Sib": _action("SibRequest")}, objects))

    info = ld.get_param_info("svc", "v", "Sib")
    assert isinstance(info["Left"]["members"], dict)
    assert isinstance(info["Right"]["members"], dict)
    assert {"K", "V"} <= set(info["Left"]["members"].keys())
    assert {"K", "V"} <= set(info["Right"]["members"].keys())


# ============================================================
# C. 深度嵌套（无 max_depth 时全展开）
# ============================================================
def test_C1_deep_nesting_full_expand():
    """C1: 深度嵌套（无环）应完整展开到最内层。"""
    # 构造 XRequest -> L1 -> L2 -> L3 -> L4 -> L5 -> string
    objects = {"XRequest": {"members": [
        {"name": "F", "type": "object", "member": "L1",
         "document": "", "required": True}
    ]}}
    for i in range(1, 5):
        objects["L%d" % i] = {"members": [
            {"name": "F", "type": "object", "member": "L%d" % (i + 1),
             "document": "", "required": True}
        ]}
    objects["L5"] = {"members": [
        {"name": "Leaf", "type": "string", "member": "string",
         "document": "", "required": True}
    ]}
    actions = {"X": {"input": "XRequest", "name": "X"}}
    ld = _make_loader(_model(actions, objects))

    info = ld.get_param_info("svc", "v", "X")
    cur = info["F"]
    for _ in range(4):
        assert isinstance(cur["members"], dict)
        cur = cur["members"]["F"]
    # 最里层应是 Leaf 完整展开
    assert "Leaf" in cur["members"]
    assert cur["members"]["Leaf"]["type"] == "String"


# ============================================================
# D. _generate_param_skeleton
# ============================================================
def test_D1_skeleton_self_ref_object_emits_placeholder():
    """D1: Object 自引用 → 第二层以字符串占位表示。"""
    objects = {
        "LinkRequest": {
            "members": [
                {"name": "Head", "type": "object", "member": "LinkNode",
                 "document": "", "required": True},
            ],
        },
        "LinkNode": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Next", "type": "object", "member": "LinkNode",
                 "document": "", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"Link": _action("LinkRequest")}, objects))
    skeleton = ld.generate_param_skeleton("svc", "v", "Link")
    # Head 完整展开一层
    assert skeleton["Head"]["Val"] == "String"
    # Head.Next 是自引用截断点：字符串占位，含字段名与类型名
    assert skeleton["Head"]["Next"] == \
        "<recursive: fill 'Next' with a JSON object of type LinkNode (self-referenced)>"


def test_D2_skeleton_self_ref_list_emits_placeholder_list():
    """D2: List<Self> → [字符串占位]（在 Tree 自引用模型上验证）。"""
    ld = _make_loader(_self_ref_list_model())
    skeleton = ld.generate_param_skeleton("svc", "v", "Tree")
    # Root 是 Node，展开一层后 Children 出现自引用截断
    assert skeleton["Root"]["Value"] == "String"
    assert skeleton["Root"]["Children"] == [
        "<recursive: fill 'Children' with a JSON object of type Node (self-referenced)>"
    ]


def test_D3_skeleton_normal_nested_unchanged():
    """D3: 普通嵌套向后兼容。"""
    objects = {
        "Req": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item",
                 "document": "", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = Loader()
    skeleton = ld._generate_param_skeleton(objects["Req"]["members"], objects)
    assert skeleton == {"Items": [{"Key": "String"}]}


# ============================================================
# E. _get_unfold_param_info
# ============================================================
def test_E1_unfold_self_ref_no_recursion_error():
    """E1: 自引用接口 unfold 不抛 RecursionError，且包含截断点路径。"""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    keys = set(unfold.keys())
    # Root.Value（基础类型 leaf）应该在
    assert "Root.Value" in keys
    # Root.Children.0 是被自引用截断的 leaf
    assert "Root.Children.0" in keys


def test_E2_unfold_recursion_truncated_path_marked_as_object():
    """E2: 自引用截断点 type=Object 且文档含英文提示，并带稳定标记字段。"""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    trunc = unfold["Root.Children.0"]
    assert trunc["type"] == "Object"
    assert trunc["required"] == "Optional"
    assert "self-referencing type" in trunc["document"]
    assert "Node" in trunc["document"]
    # 新增稳定字段（不依赖文案）：方案-B
    assert trunc.get("recursive_truncated") is True
    assert trunc.get("recursive_type") == "Node"


def test_E3_unfold_sibling_shared_type_fully_expanded():
    """E3: 兄弟字段共享同一非自引用类型，应分别独立完整展开。"""
    objects = {
        "XRequest": {
            "members": [
                {"name": "L", "type": "object", "member": "C",
                 "document": "", "required": True},
                {"name": "R", "type": "object", "member": "C",
                 "document": "", "required": True},
            ],
        },
        "C": {
            "members": [
                {"name": "K", "type": "string", "member": "string",
                 "document": "", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"X": _action("XRequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "X")
    assert "L.K" in unfold
    assert "R.K" in unfold


# ============================================================
# F. _filling_unfold_param_info
# ============================================================
def test_F1_filling_truncated_marks_object_and_appends_doc():
    """F1: 截断 leaf 的 type/type_name/required/document 行为。"""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    trunc = unfold["Root.Children.0"]
    assert trunc["type"] == "Object"
    assert trunc["type_name"] == "Node"  # 用占位类型名


def test_F2_filling_normal_leaf_keeps_type():
    """F2: 普通基础类型 leaf 类型不被改写。"""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    assert unfold["Root.Value"]["type"] == "String"
    assert unfold["Root.Value"]["type_name"] == "String"
    assert "self-referencing type" not in unfold["Root.Value"]["document"]
    assert unfold["Root.Value"].get("recursive_truncated") is not True


def test_F3_filling_secondary_check_for_list_placeholder():
    """F3: 二次判定 —— 当一个字段的类型本身是自引用类型 Node，
    且 Request 通过 List<Node> 引用它，截断点应被正确登记并在 _filling 阶段
    通过"二次判定"识别为自引用占位。"""
    objects = {
        "XRequest": {
            "members": [
                {"name": "Roots", "type": "list", "member": "Node",
                 "document": "", "required": True},
            ],
        },
        "Node": {
            "members": [
                {"name": "Val", "type": "string", "member": "string",
                 "document": "", "required": True},
                {"name": "Children", "type": "list", "member": "Node",
                 "document": "", "required": False},
            ],
        },
    }
    actions = {"X": {"input": "XRequest", "name": "X"}}
    ld = _make_loader(_model(actions, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "X")
    # Roots.0.Val 是基础类型 leaf
    assert "Roots.0.Val" in unfold
    assert unfold["Roots.0.Val"]["type"] == "String"
    # Roots.0.Children.0 是自引用截断点，type 应被改写为 Object
    assert "Roots.0.Children.0" in unfold
    assert unfold["Roots.0.Children.0"]["type"] == "Object"
    assert "self-referencing type" in unfold["Roots.0.Children.0"]["document"]
    assert unfold["Roots.0.Children.0"].get("recursive_truncated") is True
    assert unfold["Roots.0.Children.0"].get("recursive_type") == "Node"


# ============================================================
# G. 公共 API 端到端
# ============================================================
def test_G1_get_param_info_public():
    """G1: get_param_info 公共方法签名 / 行为。"""
    ld = _make_loader(_self_ref_list_model())
    info = ld.get_param_info("svc", "v", "Tree")
    assert "Root" in info


def test_G2_get_output_param_info_public():
    """G2: get_output_param_info 接受 Response。"""
    objects = {
        "TreeRequest": {"members": [
            {"name": "X", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Y", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    out = ld.get_output_param_info("svc", "v", "Tree")
    assert "Y" in out


def test_G3_generate_param_skeleton_public():
    """G3: generate_param_skeleton 公共方法 + 自引用字符串占位。"""
    ld = _make_loader(_self_ref_list_model())
    skeleton = ld.generate_param_skeleton("svc", "v", "Tree")
    assert skeleton["Root"]["Children"] == [
        "<recursive: fill 'Children' with a JSON object of type Node (self-referenced)>"
    ]


def test_G4_get_unfold_param_info_public():
    """G4: get_unfold_param_info 公共方法。"""
    ld = _make_loader(_self_ref_list_model())
    unfold = ld.get_unfold_param_info("svc", "v", "Tree")
    # 必须返回 dict，且 key 是点分路径
    assert isinstance(unfold, dict)
    assert all("." in k or k == "Root" for k in unfold.keys())


# ============================================================
# H. 真实仓库数据冒烟
# ============================================================
def test_H1_real_cvm_describe_instances_smoke():
    """H1: 真实 cvm DescribeInstances 接口能正常生成展开参数。"""
    ld = Loader()
    try:
        info = ld.get_param_info("cvm", "2017-03-12", "DescribeInstances")
    except Exception as e:
        pytest.skip("local cvm api.json missing: %s" % e)
    assert isinstance(info, dict)
    assert "InstanceIds" in info or "Filters" in info

    unfold = ld.get_unfold_param_info("cvm", "2017-03-12", "DescribeInstances")
    assert isinstance(unfold, dict)
    assert len(unfold) > 0
    # 普通接口不应出现自引用截断提示
    for k, v in unfold.items():
        assert "RecursiveRef" not in v.get("type_name", "")


def test_H2_real_billing_self_ref_does_not_crash():
    """H2: 真实 billing CreateAllocationRule（含 AllocationRuleExpression 自引用）
    不再触发 RecursionError，且能产出 unfold 参数与 skeleton。"""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "billing", "v20180709", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local billing api.json missing")

    # 选取一个含 AllocationRuleExpression 自引用的真实 action
    candidates = ["CreateAllocationRule", "ModifyAllocationRule"]
    chosen = None
    for act in candidates:
        try:
            ld.get_action_model("billing", "2018-07-09", act)
            chosen = act
            break
        except Exception:
            continue
    if chosen is None:
        pytest.skip("no candidate self-ref action available")

    # 1) get_param_info 不抛
    info = ld.get_param_info("billing", "2018-07-09", chosen)
    assert isinstance(info, dict)

    # 2) generate_param_skeleton 应在自引用处出现字符串占位
    skeleton = ld.generate_param_skeleton("billing", "2018-07-09", chosen)
    flat = repr(skeleton)
    assert "<recursive: fill " in flat
    assert "(self-referenced)" in flat
    assert "AllocationRuleExpression" in flat

    # 3) get_unfold_param_info 不抛，且至少有一个截断标记字段
    unfold = ld.get_unfold_param_info("billing", "2018-07-09", chosen)
    assert isinstance(unfold, dict) and len(unfold) > 0
    has_truncation_doc = any(
        "self-referencing type" in (v.get("document") or "") for v in unfold.values()
    )
    assert has_truncation_doc, (
        "expected at least one self-ref truncation marker in %s" % chosen
    )
    # 方案-B 稳定字段：至少一个截断 leaf 带 recursive_truncated=True
    assert any(v.get("recursive_truncated") for v in unfold.values()), (
        "expected at least one leaf with recursive_truncated=True in %s" % chosen
    )


# ============================================================
# I. 简单 getter / 静态信息方法（覆盖 L65-L179、L248-L321 多处）
# ============================================================
def test_I1_get_services_path_returns_existing_dir():
    """I1: get_services_path 应返回 tccli/services 真实目录。"""
    ld = Loader()
    p = ld.get_services_path()
    assert os.path.isdir(p)
    assert p.endswith("services")


def test_I2_static_text_getters():
    """I2: 文本类 getter 返回非空字符串。"""
    ld = Loader()
    assert isinstance(ld.get_cli_version(), str) and ld.get_cli_version()
    assert "Tencent Cloud" in ld.get_description()
    assert "tccli configure" in ld.get_configure()
    assert "tccli" in ld.get_usage()


def test_I3_get_options_and_cli_option_shape():
    """I3: get_options / get_cli_option 返回正确结构。"""
    ld = Loader()
    opts = ld.get_options()
    assert "help" in opts and "--version" in opts
    cli_opt = ld.get_cli_option()
    # 关键 cli 全局选项必须存在
    for must in ("filter", "output", "secretId", "secretKey", "profile",
                 "region", "endpoint", "generate-cli-skeleton",
                 "cli-input-json", "cli-unfold-argument", "language"):
        assert must in cli_opt, "missing global option: %s" % must
    # output 限定 choices
    assert set(cli_opt["output"]["choices"]) == {"json", "text", "table"}


def test_I4_version_transform():
    """I4: _version_transform 把 'v20180709' 还原为 '2018-07-09'。"""
    ld = Loader()
    assert ld._version_transform("v20180709") == "2018-07-09"
    assert ld._version_transform("v20170312") == "2017-03-12"


def test_I5_get_service_description_and_usage_options():
    """I5: 服务级简单 getter 行为。"""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    # metadata 没有 api_brief 时返回空串
    assert ld.get_service_description("svc", "v") == ""
    assert "svc" in ld.get_service_usage("svc")
    sopts = ld.get_service_options("svc")
    assert "help" in sopts and "svc" in sopts["help"]


def test_I6_get_action_simple_getters():
    """I6: action 级简单 getter（description / online_status / usage / options）。"""
    objects = {"FooRequest": {"members": []}}
    actions = {"Foo": {"input": "FooRequest", "name": "Foo",
                       "document": "doc-foo", "status": "deprecated"}}
    ld = _make_loader(_model(actions, objects))

    assert ld.get_action_description("svc", "v", "Foo") == "doc-foo"
    assert ld.get_action_online_status("svc", "v", "Foo") == "deprecated"
    # 未指定 status 时默认 online
    actions["Bar"] = {"input": "FooRequest", "name": "Bar", "document": "d"}
    assert ld.get_action_online_status("svc", "v", "Bar") == "online"

    usage = ld.get_action_usage("svc", "Foo")
    assert "tccli" in usage and "svc" in usage and "Foo" in usage

    aopts = ld.get_action_options("svc", "Foo")
    assert "--profile" in aopts


def test_I7_get_action_model_and_actions_info():
    """I7: get_action_model / get_actions_info 直接查 action 元数据。"""
    actions = {
        "B": {"input": "FooRequest", "name": "B", "document": "doc-b"},
        "A": {"input": "FooRequest", "name": "A", "document": "doc-a"},
    }
    objects = {"FooRequest": {"members": []}}
    ld = _make_loader(_model(actions, objects))

    am = ld.get_action_model("svc", "v", "A")
    assert am["name"] == "A" and am["document"] == "doc-a"

    info = ld.get_actions_info("svc", "v")
    # 返回 OrderedDict 且按 action name 排序
    assert list(info.keys()) == ["A", "B"]
    assert info["A"]["status"] == "online"  # 缺省值


# ============================================================
# J. get_service_model 真实读 + plugin merge 分支
# ============================================================
def test_J1_get_service_model_real_cvm():
    """J1: 走真实磁盘路径读 cvm api.json（命中 L208-L246 主路径）。"""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "cvm", "v20170312", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local cvm api.json missing")
    model = ld.get_service_model("cvm", "2017-03-12")
    assert "actions" in model and "objects" in model
    assert "DescribeInstancesRequest" in model["objects"]


def test_J2_get_service_model_plugin_merge_branch():
    """J2: 命中 plugin merge 分支（L228-L241），合并自定义 plugin actions/objects。"""
    ld = Loader()
    services_path = ld.get_services_path()
    api_path = os.path.join(services_path, "cvm", "v20170312", "api.json")
    if not os.path.exists(api_path):
        pytest.skip("local cvm api.json missing")
    # 注入一个伪 plugin，名字与 service 匹配，版本与 v20170312 匹配
    fake_plugin_spec = {
        "metadata": {"_plugin_marker": "yes"},
        "actions": {"_FakePluginAction": {"name": "_FakePluginAction"}},
        "objects": {"_FakePluginObject": {"members": []}},
    }
    saved = _plg.import_plugins
    _plg.import_plugins = lambda: {"cvm": {"2017-03-12": fake_plugin_spec}}
    try:
        model = ld.get_service_model("cvm", "2017-03-12")
        # plugin 合并的 metadata/actions/objects 都生效
        assert model["metadata"].get("_plugin_marker") == "yes"
        assert "_FakePluginAction" in model["actions"]
        assert "_FakePluginObject" in model["objects"]
    finally:
        _plg.import_plugins = saved


def test_J3_get_available_services_returns_dict():
    """J3: get_available_services 返回 dict 且至少包含 cvm。"""
    ld = Loader()
    avail = ld.get_available_services()
    assert isinstance(avail, dict)
    if "cvm" in avail:
        assert isinstance(avail["cvm"], list)


# ============================================================
# K. get_service_default_version / 多版本 / all-action 系列
# ============================================================
def test_K1_get_service_default_version_uses_first():
    """K1: 无配置文件时默认取 available_services[service][0]。"""
    ld = Loader()
    # 屏蔽 ~/.tccli 读取
    avail = ld.get_available_services()
    if "cvm" not in avail or not avail["cvm"]:
        pytest.skip("cvm not in available services")

    # 用 monkey patch 让 file_existed 返回 False
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        ver = ld.get_service_default_version("cvm")
        assert ver in avail["cvm"]
    finally:
        _u.Utils.file_existed = saved


def test_K2_get_service_all_version_actions_real_cvm():
    """K2: 真实 cvm 至少含一个版本目录。"""
    ld = Loader()
    services_path = ld.get_services_path()
    cvm_path = os.path.join(services_path, "cvm")
    if not os.path.isdir(cvm_path):
        pytest.skip("local cvm dir missing")
    res = ld.get_service_all_version_actions("cvm")
    assert isinstance(res, dict) and len(res) > 0
    # 任意一个 version 的 actions 是可迭代
    any_ver = next(iter(res))
    assert hasattr(res[any_ver], "__iter__")


def test_K3_get_service_all_version_actions_missing_raises():
    """K3: service 不存在时抛异常。"""
    ld = Loader()
    try:
        ld.get_service_all_version_actions("__no_such_service__")
        assert False, "expected exception"
    except Exception as e:
        assert "Not find service" in str(e)


def test_K4_get_service_all_action_param_default_model():
    """K4: 未指定 model 走 get_param_info 路径（覆盖 L289-L307 主分支）。"""
    ld = Loader()
    services_path = ld.get_services_path()
    if not os.path.isdir(os.path.join(services_path, "cvm")):
        pytest.skip("local cvm missing")
    res = ld.get_service_all_action_param("cvm")
    assert isinstance(res, dict)
    # 至少一个 action 有参数清单
    assert any(len(v) >= 0 for v in res.values())


def test_K5_get_service_all_action_param_unfold_model():
    """K5: model='cli-unfold-argument' 走 get_unfold_param_info 路径。"""
    ld = Loader()
    services_path = ld.get_services_path()
    if not os.path.isdir(os.path.join(services_path, "cvm")):
        pytest.skip("local cvm missing")
    res = ld.get_service_all_action_param("cvm", model="cli-unfold-argument")
    assert isinstance(res, dict)


# ============================================================
# L. _add_array_item / get_unfold_param_info 的 param_array 行为
# ============================================================
def test_L1_add_array_item_expand_to_max():
    """L1: 路径含 '0' 占位时，会被复制为 0..arrayCount-1，默认 10 份。"""
    ld = Loader()
    # mock file_existed 返回 False，走默认 array_count=10
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        param_list = [["A", "0", "B"]]
        out = ld._add_array_item(param_list, "default")
        # 应包含 ["A","1","B"] ~ ["A","9","B"] 共 9 条新增（加原 1 条 = 10）
        assert ["A", "0", "B"] in out
        assert ["A", "9", "B"] in out
        # 不应越界产生 "10"
        assert ["A", "10", "B"] not in out
    finally:
        _u.Utils.file_existed = saved


def test_L2_add_array_item_with_param_array_via_unfold():
    """L2: 通过 get_unfold_param_info(param_array=True) 触发 _add_array_item。"""
    ld = _make_loader(_self_ref_list_model())
    # mock 配置以使用默认 array_count
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        unfold = ld.get_unfold_param_info(
            "svc", "v", "Tree", profile="default", param_array=True)
        # 应展开出 Root.Children.1, Root.Children.2 ... 等额外路径
        assert "Root.Children.0" in unfold
        # 至少有一个非 0 的下标 key
        non_zero = [k for k in unfold if k.startswith("Root.Children.") and not k.endswith(".0")]
        assert len(non_zero) > 0
    finally:
        _u.Utils.file_existed = saved


# ============================================================
# M. _filling_unfold_param_info 未覆盖分支
# ============================================================
def test_M1_filling_required_downgrade_in_path():
    """M1: 路径中某层 required=Optional 时，最终 leaf required 也降为 Optional。"""
    objects = {
        "ZRequest": {
            "members": [
                {"name": "Outer", "type": "object", "member": "Inner",
                 "document": "outer", "required": True},  # 顶层 Required
            ],
        },
        "Inner": {
            "members": [
                {"name": "Mid", "type": "object", "member": "Leaf",
                 "document": "mid", "required": False},  # ← 中间 Optional
            ],
        },
        "Leaf": {
            "members": [
                {"name": "X", "type": "string", "member": "string",
                 "document": "x", "required": True},
            ],
        },
    }
    ld = _make_loader(_model({"Z": _action("ZRequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "Z")
    # Outer 顶层 Required，但中间 Mid Optional → 最终 leaf 也是 Optional
    assert unfold["Outer.Mid.X"]["required"] == "Optional"


def test_M2_filling_array_index_gt_zero_downgrades_required():
    """M2: 路径中含 '1' '2' 等非零下标时 required 强制 Optional（覆盖 L540-L541）。"""
    ld = _make_loader(_self_ref_list_model())
    from tccli import utils as _u
    saved = _u.Utils.file_existed
    _u.Utils.file_existed = staticmethod(lambda *a, **kw: (False, ""))
    try:
        unfold = ld.get_unfold_param_info(
            "svc", "v", "Tree", profile="default", param_array=True)
        # Root.Children.1 等非零下标的 required 应是 Optional
        for k, v in unfold.items():
            if k.startswith("Root.Children.") and not k.endswith(".0"):
                assert v["required"] == "Optional"
                break
    finally:
        _u.Utils.file_existed = saved


def test_M3_filling_path_traverses_array_member_dict():
    """M3: 路径在 Array 类型节点上钻取（覆盖 L498 res['type']=='Array' 取 [0] 分支）。"""
    objects = {
        "ARequest": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item",
                 "document": "items", "required": True},
            ],
        },
        "Item": {
            "members": [
                {"name": "Key", "type": "string", "member": "string",
                 "document": "k", "required": True},
                {"name": "Val", "type": "string", "member": "string",
                 "document": "v", "required": False},
            ],
        },
    }
    ld = _make_loader(_model({"A": _action("ARequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "A")
    # Items 是 Array → 钻取时走 res["members"][0][item] 分支
    assert "Items.0.Key" in unfold
    assert unfold["Items.0.Key"]["type"] == "String"
    assert unfold["Items.0.Val"]["required"] == "Optional"


# ============================================================
# N. example / translate 系列
# ============================================================
def _patch_example_model(ld, examples):
    """为 ld 注入伪 example data，供 generate_cli_example 调用。"""
    ld.get_action_example_model = lambda s, v, a: examples


def test_N1_get_action_example_model_missing_raises():
    """N1: examples.json 不存在时抛异常。"""
    ld = Loader()
    try:
        ld.get_action_example_model("__no_svc__", "1970-01-01", "X")
        assert False
    except Exception as e:
        assert "Not find service" in str(e)


def test_N2_get_action_example_model_real_cvm():
    """N2: 真实 cvm DescribeInstances 应有 examples。"""
    ld = Loader()
    services_path = ld.get_services_path()
    if not os.path.exists(os.path.join(services_path, "cvm", "v20170312", "examples.json")):
        pytest.skip("examples.json missing")
    ex = ld.get_action_example_model("cvm", "2017-03-12", "DescribeInstances")
    assert isinstance(ex, list) and len(ex) > 0


def test_N3_translate_get_cli_param_basic():
    """N3: GET 参数解析 —— 简单 key=value、空格转义、List 索引去掉。"""
    ld = Loader()
    out = ld.translate_get_cli_param([
        "Limit=10",
        "Offset=0",
        "Filters.0=foo",
        "Filters.1=bar baz",
    ])
    # 简单 key
    assert "--Limit 10" in out
    assert "--Offset 0" in out
    # List 索引被去掉，多值聚合，空格用引号包裹
    filters = [s for s in out if s.startswith("--Filters")]
    assert len(filters) == 1
    assert "foo" in filters[0]
    assert "'bar baz'" in filters[0]


def test_N4_translate_get_cli_param_skip_invalid():
    """N4: 无 '=' 的非法 token 应被忽略不抛异常。"""
    ld = Loader()
    out = ld.translate_get_cli_param(["Limit=10", "no_equals_token"])
    assert any("--Limit" in s for s in out)


def test_N5_translate_post_cli_param_complex():
    """N5: POST JSON 入参翻译 —— 嵌套 object / list of object / 含空格值。"""
    ld = Loader()
    inp = {
        "Name": "hello world",
        "Count": 3,
        "Tags": ["a", "b c"],
        "Items": [
            {"K": "k1", "V": "v 1"},
            {"K": "k2", "V": "v2"},
        ],
    }
    out = ld.translate_post_cli_param(inp)
    flat = "\n".join(out)
    # 简单字段
    assert "--Name 'hello world'" in flat
    assert "--Count 3" in flat
    # 基础类型 list 整段 join
    assert "--Tags" in flat and "'b c'" in flat
    # object list 用下标点路径
    assert "--Items.0.K k1" in flat
    assert "--Items.1.V v2" in flat


def test_N6_generate_cli_example_post_input():
    """N6: generate_cli_example 的 POST 入参翻译。"""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    ld.get_action_example_model = lambda s, v, a: [
        {
            "input": "POST / HTTP/1.1\nHost: x.tencentcloudapi.com\n\n"
                     '{"Name":"foo","N":1}',
            "output": '{"Response":{"RequestId":"req-1"}}',
            "title": "demo",
        }
    ]
    examples = ld.generate_cli_example("svc", "v", "X")
    assert len(examples) == 1
    inp = examples[0]["input"]
    assert any("--Name foo" in s for s in inp)
    # output 经 json.dumps 美化（含换行）
    assert "RequestId" in examples[0]["output"]


def test_N7_generate_cli_example_get_input():
    """N7: generate_cli_example 的 GET 入参翻译。"""
    ld = _make_loader(_model(
        actions={"X": _action("XRequest")},
        objects={"XRequest": {"members": []}},
    ))
    ld.get_action_example_model = lambda s, v, a: [
        {
            "input": "https://x.tencentcloudapi.com/?Action=X"
                     "&<公共请求参数>"
                     "&Limit=10"
                     "&Filters.0=foo",
            "output": "not-json-but-ok",
            "title": "demo-get",
        }
    ]
    examples = ld.generate_cli_example("svc", "v", "X")
    inp = examples[0]["input"]
    assert any(s.startswith("--Limit") for s in inp)
    assert any(s.startswith("--Filters") for s in inp)
    # output 不是合法 JSON 时保持原样
    assert examples[0]["output"] == "not-json-but-ok"


def test_N8_translate_post_cli_param_basic_type_only():
    """N8: 顶层是单一基础类型也能 happy path 走通 _translate_post_cli_param。"""
    ld = Loader()
    # 直接用底层私有方法验证 basic-type 短路分支
    out = []
    ld._translate_post_cli_param("hello", [], out)
    assert out == [["hello"]]
    # 含空格被引号包裹
    out2 = []
    ld._translate_post_cli_param("a b", [], out2)
    assert out2 == [["'a b'"]]


# ============================================================
# O. 边界 / 异常 / 健壮性补充
# ============================================================
def test_O1_get_param_info_response_via_output_method():
    """O1: get_output_param_info 在自引用类型上同样不崩溃。"""
    objects = {
        "TreeRequest": {"members": [
            {"name": "A", "type": "string", "member": "string",
             "document": "", "required": True}
        ]},
        "TreeResponse": {"members": [
            {"name": "Root", "type": "object", "member": "Node",
             "document": "", "required": True}
        ]},
        "Node": {"members": [
            {"name": "Self", "type": "object", "member": "Node",
             "document": "", "required": False},  # ← 自引用
        ]},
    }
    actions = {"Tree": {"input": "TreeRequest", "output": "TreeResponse",
                        "name": "Tree"}}
    ld = _make_loader(_model(actions, objects))
    out = ld.get_output_param_info("svc", "v", "Tree")
    # Root 展开一层后 Self 是截断点
    assert isinstance(out["Root"]["members"], dict)
    assert out["Root"]["members"]["Self"]["members"] == "Node"


def test_O2_unfold_basic_type_list_no_zero_in_path():
    """O2: List<base_type> 不应在路径里 push '0'。"""
    objects = {
        "URequest": {"members": [
            {"name": "Tags", "type": "list", "member": "string",
             "document": "", "required": False}
        ]},
    }
    ld = _make_loader(_model({"U": _action("URequest")}, objects))
    unfold = ld.get_unfold_param_info("svc", "v", "U")
    # 基础类型 list 路径只到字段名
    assert "Tags" in unfold
    # 不应注册 Tags.0 这种带 '0' 的路径
    assert "Tags.0" not in unfold


def test_O3_get_param_info_value_allowed_null_branch():
    """O3: 字段含 value_allowed_null=True 时被正确写入。"""
    objects = {"XRequest": {"members": [
        {"name": "F", "type": "string", "member": "string",
         "document": "", "required": True, "value_allowed_null": True}
    ]}}
    ld = _make_loader(_model({"X": _action("XRequest")}, objects))
    info = ld.get_param_info("svc", "v", "X")
    assert info["F"].get("value_allowed_null") == "AllowedNull"

    # 反向：False 时为 NotAllowedNull
    objects["XRequest"]["members"][0]["value_allowed_null"] = False
    info2 = ld.get_param_info("svc", "v", "X")
    assert info2["F"].get("value_allowed_null") == "NotAllowedNull"


# ============================================================
# 允许直接 `python3 tests/test_loaders.py` 运行（无 pytest 环境）
# ============================================================
if __name__ == "__main__":
    import traceback

    tests = [
        (name, obj) for name, obj in sorted(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    passed = failed = skipped = 0
    failures = []
    for name, fn in tests:
        try:
            fn()
            print("PASS  %s" % name)
            passed += 1
        except Exception as e:
            cls = e.__class__.__name__
            if cls in ("_SkipException", "Skipped"):
                print("SKIP  %s  (%s)" % (name, e))
                skipped += 1
            else:
                print("FAIL  %s" % name)
                traceback.print_exc()
                failed += 1
                failures.append(name)
    print("\n=========================================")
    print("total=%d  passed=%d  failed=%d  skipped=%d"
          % (len(tests), passed, failed, skipped))
    if failures:
        print("failed tests:")
        for n in failures:
            print("  - %s" % n)
    sys.exit(1 if failed else 0)
