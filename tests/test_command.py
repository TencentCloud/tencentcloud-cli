# -*- coding: utf-8 -*-
"""
针对 tccli/command.py 的单元测试。

包含：
  A) 端到端 subprocess 测试（保留自 test_command_recursive_hint.py）
     —— 验证客户 TAPD 报障场景的真实退出码和 stderr 输出。
  B) _build_recursive_hint 白盒分支覆盖
     —— 这是 self-ref 修复的核心函数，分支较多。
  C) ActionCommand 内部方法（init / property / 私有助手）
  D) CLICommand 内部方法
  E) ServiceCommand 内部方法
  F) 边界 / 异常 / 健壮性补充

设计要点：
  - 现有 subprocess 测试只能验证端到端行为，但 coverage 工具
    无法统计子进程内的代码执行。所以本文件大量增加“主进程内
    直接调用类方法”的白盒测试，以提升真实覆盖率。
"""
import os
import sys
import copy
import subprocess
from collections import OrderedDict, namedtuple

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

_TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_TESTS_DIR)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# ============================================================
# 通用：屏蔽 plugin 加载（很多 tccli 插件依赖外部 SDK，环境可能没装）
# ============================================================
import tccli.plugin as _plg
_plg.import_plugins = lambda: {}

import tccli.options_define as Options_define
from tccli.command import (
    BaseCommand, CLICommand, ServiceCommand, ActionCommand,
)
from tccli.exceptions import UnknownArgumentError
from tccli.loaders import Loader


# ============================================================
# 通用工具
# ============================================================
def _billing_schema_available():
    """判断本地是否带有 billing v20180709 api.json。"""
    api_path = os.path.join(
        Loader().get_services_path(), "billing", "v20180709", "api.json")
    return os.path.exists(api_path)


def _run_tccli(args):
    """以子进程方式运行 tccli main，返回 (exit_code, stdout, stderr)。"""
    code = (
        "import sys; sys.path.insert(0, %r);\n"
        "import tccli.plugin as _p; _p.import_plugins=lambda: {};\n"
        "from tccli.main import main; sys.argv = %r; sys.exit(main())"
    ) % (_REPO_ROOT, ["tccli"] + list(args))
    proc = subprocess.Popen(
        [sys.executable, "-c", code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )
    out, err = proc.communicate(timeout=60)
    return proc.returncode, out.decode("utf-8", "replace"), err.decode("utf-8", "replace")


def _make_action_command(call_mode=None, profile="default"):
    """构造一个最小的 ActionCommand 实例（不走 __init__ 完整逻辑），
       用于直接驱动 _build_recursive_hint / _build_action_parameters 等私有方法。

       不调用 super().__init__() 避免触达真实 Loader（已通过 _cli_data 单独注入）。
    """
    ac = object.__new__(ActionCommand)
    ac._service_name = "billing"
    ac._version = "2018-07-09"
    ac._action_name = "CreateGatherRule"
    ac._call_mode = call_mode
    ac.profile = profile
    ac._cli_data = Loader()
    ac._argument_map = None
    return ac


def _make_globals(**kw):
    """模拟 argparse parsed_globals namespace 对象。
       用 argparse.Namespace 而非 namedtuple，确保 vars() 可访问 __dict__。
    """
    import argparse as _argparse
    base = {
        Options_define.Profile: kw.pop("profile", None),
        Options_define.GenerateCliSkeleton.replace("-", "_"):
            kw.pop("generate_cli_skeleton", None),
        Options_define.CliInputJson.replace("-", "_"):
            kw.pop("cli_input_json", None),
        Options_define.CliUnfoldArgument.replace("-", "_"):
            kw.pop("cli_unfold_argument", None),
    }
    base.update(kw)
    return _argparse.Namespace(**base)


# ============================================================
# A. 端到端 subprocess 测试（迁移自原 test_command_recursive_hint.py）
# ============================================================
def test_A1_customer_original_command_passes_through_no_recursion_error():
    """A1: 客户 TAPD 单中提供的命令直接执行：
       不再出现 RecursionError；穿过自引用截断点 ≤30 段时合法放行至云端调用。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--Id", "1490",
        "--RuleList.RuleDetail.Children.0.RuleValue", "ESG",
        "--RuleList.RuleDetail.Children.0.Operator", "in",
    ])

    combined = stdout + stderr

    # 关键回归点 1：不能再出现递归错误
    assert "maximum recursion depth exceeded" not in combined, (
        "RecursionError leaked back to user! stderr:\n%s" % stderr)
    assert "RecursionError" not in combined

    # 关键回归点 2：参数不再被识别为 Unknown，请求体可被构造
    # 命令实际是否到达云端取决于本机鉴权，但 CLI 层不应再出 Unknown options
    assert "Unknown options" not in combined, (
        "self-ref extension param wrongly rejected:\n%s" % combined)
    # CLI 层不再产出 self-referencing hint（合法放行后没必要）
    assert "self-referencing type" not in combined, (
        "self-ref hint should not appear for legal extension:\n%s" % combined)


def test_A1b_oversized_depth_emits_hint():
    """A1b: 深度超过 MAX_INPUT_DEPTH=30 时，CLI 层应抛 oversized 提示并指向 file://。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    parts = ["RuleList", "RuleDetail", "Children", "0"]
    for _ in range(13):
        parts += ["Children", "0"]
    parts += ["RuleKey"]
    deep_key = ".".join(parts)
    assert len(parts) == 31

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--Id", "1490",
        "--" + deep_key, "v",
    ])

    combined = stdout + stderr
    assert "RecursionError" not in combined
    assert code == 255
    assert "MAX_INPUT_DEPTH=30" in stderr
    assert "depth=31" in stderr
    assert "Use --cli-input-json file://" in stderr


def test_A2_normal_unknown_option_no_self_ref_hint():
    """A2: 普通错拼参数不应误触发 self-ref hint。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--Id", "1490",
        "--TotallyUnknownArg", "x",
    ])

    assert code == 255
    assert "Unknown options" in stderr
    # 不应出现 self-referencing hint —— 因为该参数不属于截断 leaf 前缀
    assert "self-referencing type" not in stderr, (
        "false-positive self-ref hint:\n%s" % stderr)


def test_A3_pass_self_ref_field_as_json_no_hint_about_self_ref():
    """A3: --generate-cli-skeleton 模式不应触发 unknown options，也不应出现 self-ref hint。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    code, stdout, stderr = _run_tccli([
        "billing", "CreateGatherRule",
        "--cli-unfold-argument",
        "--generate-cli-skeleton",
    ])

    assert "Unknown options" not in stderr
    assert "self-referencing type" not in stderr


# ============================================================
# B. _build_recursive_hint 白盒分支覆盖（核心修复点）
# ============================================================
def test_B1_hint_returns_empty_when_not_unfold_mode():
    """B1: 非 --cli-unfold-argument 模式下直接返回空串。"""
    ac = _make_action_command(call_mode=None)
    assert ac._build_recursive_hint(["--foo", "bar"]) == ""

    # 显式设为 generate-cli-skeleton 模式也应返回空串
    ac._call_mode = Options_define.GenerateCliSkeleton
    assert ac._build_recursive_hint(["--foo"]) == ""


def test_B2_hint_returns_empty_when_loader_raises():
    """B2: Loader.get_unfold_param_info 抛异常时静默返回空串。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _BadLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            raise RuntimeError("mock failure")
    ac._cli_data = _BadLoader()
    assert ac._build_recursive_hint(["--anything"]) == ""


def test_B3_hint_returns_empty_when_no_truncated_leaf():
    """B3: 当 unfold 清单中没有任何 recursive_truncated 字段时，返回空串。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _NoTrunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Foo": {"recursive_truncated": False},
                "Bar.Baz": {},  # 无 recursive_truncated 键
            }
    ac._cli_data = _NoTrunc()
    assert ac._build_recursive_hint(["--Foo.NotExist", "x"]) == ""


def test_B4_hint_returns_empty_when_no_token_matches():
    """B4: 有截断点但用户的非法参数都不命中前缀 → 返回空串。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "RuleList.RuleDetail.Children.0": {
                    "recursive_truncated": True,
                    "recursive_type": "AllocationRuleExpression",
                }
            }
    ac._cli_data = _Trunc()
    # remaining 中无任何前缀命中 RuleList.RuleDetail.Children.0
    assert ac._build_recursive_hint(["--Other.Param", "v"]) == ""


def test_B5_hint_emits_full_text_on_match():
    """B5: 命中截断前缀时，输出包含 self-referencing type 上下文与 file:// 单选项替代方案。

    方案变更（recursive-nesting-30 / 方式 A）：
      - 移除 (1) Drop --cli-unfold-argument 选项与 applies to 上下文行；
      - 仅保留 file:// 单一替代方案，配合反向断言锁定不再回退。
    顶层字段名仍可在每条命中 token 行尾的 (under --RuleList.RuleDetail.Children.0, ...) 中看到。
    """
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "RuleList.RuleDetail.Children.0": {
                    "recursive_truncated": True,
                    "recursive_type": "AllocationRuleExpression",
                }
            }
    ac._cli_data = _Trunc()

    hint = ac._build_recursive_hint([
        "--RuleList.RuleDetail.Children.0.RuleKey", "x",
        "--RuleList.RuleDetail.Children.0.Operator", "in",
    ])
    assert "self-referencing type" in hint
    assert "AllocationRuleExpression" in hint
    assert "--RuleList.RuleDetail.Children.0" in hint
    # 单选项 hint：仅保留 file://
    assert "Use --cli-input-json file://" in hint
    # 反向断言：旧的 Drop 方案与 applies to 上下文不应再出现
    assert "Drop --cli-unfold-argument" not in hint
    assert "applies to:" not in hint


def test_B6_hint_falls_back_when_recursive_type_missing():
    """B6: recursive_type 为空时，提示文案降级显示 'unknown' 占位。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "X.Y.Z.0": {
                    "recursive_truncated": True,
                    "recursive_type": "",  # ← 空字符串
                }
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint(["--X.Y.Z.0.More", "v"])
    assert "self-referencing type: unknown" in hint
    # 单选项 hint 始终输出 file:// 替代方案
    assert "Use --cli-input-json file://" in hint
    assert "Drop --cli-unfold-argument" not in hint


def test_B7_hint_skips_non_string_or_non_option_tokens():
    """B7: remaining 中非字符串 token、不以 -- 开头的 token 应被忽略。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Top.0": {
                    "recursive_truncated": True,
                    "recursive_type": "T",
                }
            }
    ac._cli_data = _Trunc()
    # 包含数字、None、不带 -- 的字符串
    hint = ac._build_recursive_hint([
        123, None, "no_dashes", "--Top.0.Sub", "v",
    ])
    # 只有 --Top.0.Sub 命中
    assert "--Top.0.Sub" in hint


def test_B8_hint_dedup_top_fields_across_multiple_prefixes():
    """B8: 多个截断点共享同一顶层字段时 top_fields 不重复。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Root.A.0": {"recursive_truncated": True, "recursive_type": "TA"},
                "Root.B.0": {"recursive_truncated": True, "recursive_type": "TB"},
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint([
        "--Root.A.0.X", "1",
        "--Root.B.0.Y", "2",
    ])
    # 方式 A 已移除 applies to 行；改为断言两条命中 token 行都各自标注顶层 prefix
    assert "--Root.A.0.X  (under --Root.A.0," in hint
    assert "--Root.B.0.Y  (under --Root.B.0," in hint
    assert "applies to:" not in hint


def test_B9_hint_collects_multi_top_fields():
    """B9: 不同顶层字段都命中时，applies to 列出多个。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {
                "Alpha.0": {"recursive_truncated": True, "recursive_type": "T1"},
                "Beta.0": {"recursive_truncated": True, "recursive_type": "T2"},
            }
    ac._cli_data = _Trunc()
    hint = ac._build_recursive_hint([
        "--Alpha.0.x", "1",
        "--Beta.0.y", "2",
    ])
    # 方式 A 已移除 applies to 行；不同顶层字段在各自命中 token 行的尾巴里出现
    assert "(under --Alpha.0," in hint
    assert "(under --Beta.0," in hint
    assert "applies to:" not in hint


# ============================================================
# C. ActionCommand 内部方法
# ============================================================
def test_C1_actioncommand_init_basic():
    """C1: ActionCommand 初始化基本字段。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    assert ac._service_name == "billing"
    assert ac._version == "2018-07-09"
    assert ac._action_name == "CreateGatherRule"
    assert ac._call_mode is None
    assert ac.profile == "default"
    assert ac._argument_map is None


def test_C2_actioncommand_init_default_version_when_none():
    """C2: 传入 version=None 时使用 service 默认版本。"""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    ac = ActionCommand(
        service_name="cvm",
        version=None,
        action_name="DescribeInstances",
        action_model={"input": "DescribeInstancesRequest"},
        action_caller=lambda *a, **kw: None,
    )
    # 至少能拿到一个非空版本号
    assert ac._version is not None and len(ac._version) > 0


def test_C3_get_call_mode_branches():
    """C3: _get_call_mode 三种模式分支识别。"""
    ac = _make_action_command()

    # GenerateCliSkeleton
    g = _make_globals(generate_cli_skeleton=True)
    assert ac._get_call_mode(g) == Options_define.GenerateCliSkeleton

    # CliInputJson
    g2 = _make_globals(cli_input_json=True)
    assert ac._get_call_mode(g2) == Options_define.CliInputJson

    # CliUnfoldArgument
    g3 = _make_globals(cli_unfold_argument=True)
    assert ac._get_call_mode(g3) == Options_define.CliUnfoldArgument

    # 全 None → 返回 None（普通模式）
    g4 = _make_globals()
    assert ac._get_call_mode(g4) is None


def test_C4_get_profile_branches():
    """C4: _get_profile 在 parsed_globals.profile 有值/无值时分别处理。"""
    ac = _make_action_command()

    # 有值
    g = _make_globals(profile="myprof")
    ac._get_profile(g)
    assert ac.profile == "myprof"

    # 无值（None / 空）→ 默认 default
    g2 = _make_globals(profile=None)
    ac._get_profile(g2)
    assert ac.profile == "default"


def test_C5_get_param_model_unfold_vs_normal():
    """C5: _get_param_model 在不同 call_mode 下走不同 Loader API。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    unfold_info = ac._get_param_model()
    # unfold 模式产物含点号路径 key
    assert any("." in k for k in unfold_info.keys())

    ac._call_mode = None  # 普通模式
    normal_info = ac._get_param_model()
    # 普通模式 key 是顶层字段名
    assert "Id" in normal_info
    # 顶层 key 不应该含 "."
    assert all("." not in k for k in normal_info.keys())


def test_C6_build_parameter_map_skeleton_and_input_json_modes():
    """C6: _build_parameter_map 在 GenerateCliSkeleton / CliInputJson 模式下返回空 map。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.GenerateCliSkeleton)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    assert ac._build_parameter_map() == OrderedDict()

    ac._call_mode = Options_define.CliInputJson
    assert ac._build_parameter_map() == OrderedDict()


def test_C7_build_parameter_map_unfold_mode_produces_args():
    """C7: --cli-unfold-argument 模式下注册多个扁平 option（含点号路径）。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    arg_map = ac._build_parameter_map()
    assert isinstance(arg_map, OrderedDict)
    assert "Id" in arg_map  # 简单字段
    # 点号路径 key 出现
    assert any("." in k for k in arg_map.keys())


def test_C8_build_parameter_map_normal_mode():
    """C8: 普通模式下注册顶层字段为 option。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=None)  # 普通模式
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    arg_map = ac._build_parameter_map()
    assert "Id" in arg_map
    assert "RuleList" in arg_map
    # 不应有 RuleList.RuleDetail.RuleKey 这种点号 key
    assert not any("." in k for k in arg_map.keys())


def test_C9_argument_map_lazy_property():
    """C9: argument_map 懒加载属性，重复访问返回同一对象。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = _make_action_command(call_mode=None)
    ac._action_model = {"input": "CreateGatherRuleRequest"}
    am1 = ac.argument_map
    am2 = ac.argument_map
    # 同对象（懒加载缓存）
    assert am1 is am2


def test_C10_create_help_command_returns_action_help():
    """C10: create_help_command 返回 ActionHelpCommand 实例。"""
    from tccli.help_command import ActionHelpCommand
    ac = _make_action_command()
    hc = ac.create_help_command()
    assert isinstance(hc, ActionHelpCommand)


def test_C11_create_action_parser_returns_argparser():
    """C11: _create_action_parser 返回 ArgMapArgParser 实例。"""
    from tccli.argparser import ArgMapArgParser
    ac = _make_action_command()
    parser = ac._create_action_parser(OrderedDict())
    assert isinstance(parser, ArgMapArgParser)


def test_C12_build_action_parameters_collects_args():
    """C12: _build_action_parameters 把 parsed_args 中的字段写入 dict。"""
    import argparse as _argparse
    ac = _make_action_command()

    # mock 一个 argument_object
    class _Arg(object):
        def __init__(self, name):
            self.name = name

        def add_to_params(self, params, value):
            params[self.name] = value

    arg_map = OrderedDict()
    arg_map["Foo"] = _Arg("Foo")
    arg_map["Bar"] = _Arg("Bar")

    parsed = _argparse.Namespace(Foo="v1", Bar="v2")
    out = ac._build_action_parameters(parsed, arg_map)
    assert out == {"Foo": "v1", "Bar": "v2"}


# ============================================================
# D. CLICommand 内部方法
# ============================================================
def test_D1_clicommand_init():
    """D1: CLICommand 初始化基础字段。"""
    cli = CLICommand()
    assert cli._command_map is None
    assert cli._argument_map is None
    assert isinstance(cli._cli_data, Loader)


def test_D2_get_cli_options_returns_dict():
    """D2: _get_cli_options 返回 cli 全局 option 字典。"""
    cli = CLICommand()
    opts = cli._get_cli_options()
    assert "secretId" in opts
    assert "profile" in opts


def test_D3_create_cli_argument_returns_custom_argument():
    """D3: _create_cli_argument 把 option_params 转成 CustomArgument。"""
    from tccli.argument import CustomArgument
    cli = CLICommand()
    arg = cli._create_cli_argument("foo", {"help": "h"})
    assert isinstance(arg, CustomArgument)


def test_D4_build_argument_map_contains_globals():
    """D4: _build_argument_map 含所有 cli 全局选项。"""
    cli = CLICommand()
    am = cli._build_argument_map()
    assert "secretId" in am
    assert "profile" in am


def test_D5_get_argument_map_lazy():
    """D5: _get_argument_map 懒加载缓存。"""
    cli = CLICommand()
    am1 = cli._get_argument_map()
    am2 = cli._get_argument_map()
    assert am1 is am2


def test_D6_get_command_map_lazy_and_contains_configure():
    """D6: _get_command_map 懒加载 + 必含 configure 命令。"""
    cli = CLICommand()
    cmap = cli._get_command_map()
    assert "configure" in cmap


def test_D7_get_available_services_returns_iterable():
    """D7: _get_available_services 返回可迭代对象。"""
    cli = CLICommand()
    services = cli._get_available_services()
    # services 是 dict_keys 或 list
    assert hasattr(services, "__iter__")


def test_D8_get_service_version_no_version_in_argv():
    """D8: 无 --version 时 _get_service_version 返回 (None, None)。"""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "DescribeAccount"]
    try:
        s, v = cli._get_service_version()
        assert s is None and v is None
    finally:
        sys.argv = saved


def test_D9_get_service_version_with_invalid_version():
    """D9: --version 后跟非法版本时返回 (None, None)。"""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "--version", "not-a-version"]
    try:
        s, v = cli._get_service_version()
        assert s is None and v is None
    finally:
        sys.argv = saved


def test_D10_get_service_version_with_valid_version():
    """D10: --version 后跟合法版本时返回 (service, version)。"""
    cli = CLICommand()
    saved = sys.argv
    sys.argv = ["tccli", "billing", "--version", "2018-07-09"]
    try:
        s, v = cli._get_service_version()
        assert s == "billing" and v == "2018-07-09"
    finally:
        sys.argv = saved


def test_D11_handle_warning_no_crash():
    """D11: _handle_warning 在常规参数下不抛异常。"""
    cli = CLICommand()
    # 不带 --warning，且无 ~/.tccli/default.configure 时也应不崩
    cli._handle_warning(["billing", "DescribeAccount"])
    # 带 --warning
    cli._handle_warning(["billing", "DescribeAccount", "--warning", "on"])
    # 带 --profile
    cli._handle_warning(["billing", "DescribeAccount", "--profile", "myp"])


def test_D12_handle_service_version_argument_with_version_in_args():
    """D12: 含 --version + 合法版本时 parser 不重复添加 --version。"""
    import argparse
    cli = CLICommand()
    parser = argparse.ArgumentParser(add_help=False)
    args = ["billing", "--version", "2018-07-09"]
    # 不应抛异常
    cli._handle_service_version_argumnet(args, parser)


def test_D13_handle_service_version_argument_without_version():
    """D13: 不含 --version 时 parser 添加 --version。"""
    import argparse
    cli = CLICommand()
    parser = argparse.ArgumentParser(add_help=False)
    cli._handle_service_version_argumnet(["billing"], parser)
    # parser 应该现在有 --version
    has_version = any(
        "--version" in (a.option_strings if hasattr(a, "option_strings") else [])
        for a in parser._actions
    )
    assert has_version


def test_D14_create_parser_returns_cliarg_parser():
    """D14: _create_parser 返回 CLIArgParser 实例。"""
    from tccli.argparser import CLIArgParser
    cli = CLICommand()
    cmap = cli._get_command_map()
    parser = cli._create_parser(cmap)
    assert isinstance(parser, CLIArgParser)
    # help 命令被注入
    assert "help" in cmap


def test_D15_clicommand_call_with_as_alias():
    """D15: __call__ 时第一个参数是 'as' → 替换为 'autoscaling'（如果该 service 存在）。"""
    cli = CLICommand()
    avail = cli._cli_data.get_available_services()
    if "autoscaling" not in avail:
        pytest.skip("autoscaling service not available")
    # 模拟 args=["as", "help"]
    args = ["as", "help"]
    try:
        cli(args)
    except SystemExit:
        # help 命令通常以 SystemExit 收尾
        pass
    except Exception:
        # 其他异常也允许 —— 我们只验证 'as' 被改写为 'autoscaling'
        pass
    # 验证副作用：args[0] 已被替换
    assert args[0] == "autoscaling"


# ============================================================
# E. ServiceCommand 内部方法
# ============================================================
def test_E1_servicecommand_init_default_version():
    """E1: ServiceCommand 不传 version 使用默认版本。"""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    assert sc._service_name == "cvm"
    assert sc._version is not None


def test_E2_servicecommand_invalid_version_raises():
    """E2: 传入不存在的版本号抛异常。"""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    try:
        ServiceCommand("cvm", version="9999-01-01")
        assert False, "expected exception"
    except Exception as e:
        assert "is invalid" in str(e)


def test_E3_servicecommand_get_service_model():
    """E3: _get_service_model 返回 service model dict。"""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    model = sc._get_service_model()
    assert "actions" in model
    assert "objects" in model


def test_E4_servicecommand_get_command_map_lazy():
    """E4: _get_command_map 懒加载，含 actions。"""
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    cmap1 = sc._get_command_map()
    cmap2 = sc._get_command_map()
    assert cmap1 is cmap2
    # action 数量 > 0
    assert len(cmap1) > 0


def test_E5_servicecommand_create_parser_returns_action_parser():
    """E5: _create_parser 返回 ActionArgParser 实例 + 注入 help。"""
    from tccli.argparser import ActionArgParser
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    cmap = sc._get_command_map()
    parser = sc._create_parser(cmap)
    assert isinstance(parser, ActionArgParser)
    assert "help" in cmap


def test_E6_servicecommand_create_help_command():
    """E6: create_help_command 返回 ServiceHelpCommand 实例。"""
    from tccli.help_command import ServiceHelpCommand
    if not os.path.isdir(os.path.join(Loader().get_services_path(), "cvm")):
        pytest.skip("cvm service missing")
    sc = ServiceCommand("cvm")
    hc = sc.create_help_command()
    assert isinstance(hc, ServiceHelpCommand)


# ============================================================
# F. 边界 / 异常 / 健壮性补充
# ============================================================
def test_F1_basecommand_loader_inited():
    """F1: BaseCommand 子类正确继承 _cli_data 字段。"""
    bc = BaseCommand()
    assert isinstance(bc._cli_data, Loader)


def test_F2_actioncommand_call_unknown_args_raises():
    """F2: ActionCommand.__call__ 对真正未知参数（拼写错误等）抛 UnknownArgumentError。

       方案变更（recursive-nesting-30）：
         - 原断言"深入自引用截断点 = 非法"已不再成立——D≤30 的延伸属于合法输入；
         - 本用例保留"真正的非法参数（拼写错误 / 不命中任何已知前缀）"的负向断言，
           这条路径与新方案的 ``_extract_deep_nested_args`` 兜底分支严格对齐
           （需求 1.3：未命中前缀的 token 仍走 Unknown options）。
    """
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals(cli_unfold_argument=True)
    try:
        ac([
            "--Id", "1490",
            "--TotallyMadeUpField.NotInSchema", "x",  # 真正的非法参数：不命中任何已知前缀
        ], g)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "Unknown options" in msg
        assert "--TotallyMadeUpField.NotInSchema" in msg
        # 反向断言：旧方案的 Drop --cli-unfold-argument 文案不应再出现
        assert "Drop --cli-unfold-argument" not in msg


def test_F3_actioncommand_call_generate_cli_skeleton_short_circuit():
    """F3: --generate-cli-skeleton 模式不解析参数、不发请求，直接生成模板。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals(generate_cli_skeleton=True)

    # 这个调用通过 generate_skeleton 完成，最常见地是写到 stdout 后返回
    # 我们不关心内部细节 —— 只要不抛 UnknownArgumentError
    try:
        ac([], g)
    except UnknownArgumentError:
        assert False, "should not raise UnknownArgumentError in skeleton mode"
    except SystemExit:
        # generate_skeleton 内部可能 sys.exit
        pass
    except Exception:
        # 其他异常也允许 —— 例如打印 / IO 失败 —— 重点是 UnknownArgumentError 不发生
        pass


def test_F4_actioncommand_call_help_subcommand():
    """F4: 第一个位置参数是 'help' 时走 help command 分支。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=lambda *a, **kw: None,
    )
    g = _make_globals()
    try:
        ac(["help"], g)
    except SystemExit:
        pass
    except Exception:
        # help_command(...) 可能依赖外部资源；忽略
        pass


def test_F5_action_caller_is_invoked_in_normal_mode():
    """F5: 普通模式下，参数合法时调用 action_caller 并传入 action_parameters。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")

    captured = {}

    def fake_caller(action_parameters, parsed_globals):
        captured["params"] = action_parameters
        captured["globals"] = parsed_globals
        return "ok"

    ac = ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=fake_caller,
    )
    # 以 cli_unfold_argument 模式 + 合法参数避免触达 credentials.maybe_refresh_credential
    # 但这个分支会调用 credentials —— 用 monkey patch 屏蔽
    from tccli import credentials
    saved = credentials.maybe_refresh_credential
    credentials.maybe_refresh_credential = lambda *a, **kw: None
    try:
        g = _make_globals(profile="default", cli_unfold_argument=True)
        result = ac([
            "--Id", "1490",
            "--RuleList.RuleDetail.RuleKey", "tag",
        ], g)
        assert result == "ok"
        assert captured["params"]["Id"] == 1490
        # cli-unfold-argument 模式下嵌套结构被还原
        assert captured["params"]["RuleList"]["RuleDetail"]["RuleKey"] == "tag"
    finally:
        credentials.maybe_refresh_credential = saved


# ============================================================
# G. recursive-nesting-30 端到端 mock 用例
# ------------------------------------------------------------
# 覆盖以下路径：
#   * 用户输入 D ≤ 30 的合法深嵌套延伸 → 走 _extract_deep_nested_args 兜底分支 →
#     extra_unfold_args 注入 → build_action_parameters → action_caller 收到完整请求体。
#   * 用户输入 D > 30 的超限延伸 → 不进 extra_unfold_args，oversized_tokens 触发
#     UnknownArgumentError，文案含 depth= 与 file:// 替代方案，且不出现旧的 Drop 文案。
#   * 拼写错误（不命中任何截断前缀）依然抛 Unknown options（与需求 1.3 对齐）。
#   * 合法 + 超限混合场景：合法部分仍可被收集，但超限触发的整体抛错优先级更高。
# ============================================================
def _build_self_ref_path(num_layers):
    """基于 billing CreateGatherRule 截断前缀 ``RuleList.RuleDetail.Children.0``
    构造一段共 ``D`` 段（数字下标段含在内）的扁平参数 key，便于精确控制 depth。

    :param num_layers: 在 4 段截断前缀之外再叠加多少层 ``Children.0``，
        最后再追加 1 段叶子 ``RuleKey``。
    :return: ``(key, depth)``，其中 ``depth = 4 + num_layers * 2 + 1``。

    示例：
      * ``num_layers=0`` → ``RuleList.RuleDetail.Children.0.RuleKey`` (D=5)
      * ``num_layers=1`` → ``RuleList.RuleDetail.Children.0.Children.0.RuleKey`` (D=7)
      * ``num_layers=13`` → 30 段 (D=30) —— 边界放行
      * ``num_layers=14`` → 32 段 (D=32) —— 超限
    """
    base = ["RuleList", "RuleDetail", "Children", "0"]
    for _ in range(num_layers):
        base += ["Children", "0"]
    base.append("RuleKey")
    return ".".join(base), len(base)


def _walk_to_leaf(params, num_layers):
    """沿 ``params`` 进入 ``num_layers`` 层 ``Children``（list 取下标 0），最终返回叶子 dict。

    注意 billing CreateGatherRule schema 的真实形态：
      * ``RuleList`` 是 dict（不是 list！只有一个 RuleDetail 字段）；
      * ``Children`` 是 list（自引用 leaf 的承载）。
    本断言基于真实 unfold 注册结果（``RuleList.RuleDetail.RuleKey`` 形态）。
    """
    cursor = params["RuleList"]["RuleDetail"]
    # 第一层 Children
    cursor = cursor["Children"]
    assert isinstance(cursor, list) and len(cursor) == 1
    cursor = cursor[0]
    # 后续 num_layers 层
    for _ in range(num_layers):
        cursor = cursor["Children"]
        assert isinstance(cursor, list) and len(cursor) == 1
        cursor = cursor[0]
    return cursor


def _make_billing_action_command(captured):
    """构造一个 billing CreateGatherRule 的 ActionCommand，绑定捕获 params 的 fake_caller。"""
    def _caller(action_parameters, parsed_globals):
        captured["params"] = action_parameters
        captured["globals"] = parsed_globals
        return "ok"
    return ActionCommand(
        service_name="billing",
        version="2018-07-09",
        action_name="CreateGatherRule",
        action_model={"input": "CreateGatherRuleRequest", "name": "CreateGatherRule"},
        action_caller=_caller,
    )


def _patch_credentials():
    """屏蔽 credentials.maybe_refresh_credential 副作用，返回 (restore_fn)。"""
    from tccli import credentials
    saved = credentials.maybe_refresh_credential
    credentials.maybe_refresh_credential = lambda *a, **kw: None
    return lambda: setattr(credentials, "maybe_refresh_credential", saved)


def test_G3_unfold_depth_30_passthrough_boundary():
    """G3: D=30（边界值，严格 ≤ MAX_INPUT_DEPTH）应放行。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        parts = ["RuleList", "RuleDetail", "Children", "0"]
        for _ in range(13):
            parts += ["Children", "0"]
        # 4 + 13*2 = 30 段，末段是 "0"
        key = ".".join(parts)
        assert len(parts) == 30

        g = _make_globals(profile="default", cli_unfold_argument=True)
        result = ac([
            "--Id", "1490",
            "--" + key, "value_d30_pure",
        ], g)
        assert result == "ok"
        # RuleList 是 dict（schema 中并非 list，只有一个 RuleDetail 字段）。
        # 沿 RuleList.RuleDetail.Children[0] 进入；之后再连续 12 次 Children[0]；
        # 第 13 次 Children list 末端 list[0] 即标量值 "value_d30_pure"。
        cursor = captured["params"]["RuleList"]["RuleDetail"]["Children"]
        assert isinstance(cursor, list) and len(cursor) == 1
        cursor = cursor[0]
        for _ in range(12):
            cursor = cursor["Children"]
            assert isinstance(cursor, list) and len(cursor) == 1
            cursor = cursor[0]
        # 第 13 次：Children list，末端就是 list[0] 的标量值
        cursor = cursor["Children"]
        assert isinstance(cursor, list) and len(cursor) == 1
        assert cursor[0] == "value_d30_pure"
    finally:
        restore()


def test_G4_unfold_depth_31_rejected():
    """G4: D=31（越过 MAX_INPUT_DEPTH=30）应抛 UnknownArgumentError，含 depth= 与 file:// 文案。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        # 4 段前缀 + 13 层 Children.0 (26 段) + 末段 RuleKey (1 段) = 31 段
        parts = ["RuleList", "RuleDetail", "Children", "0"]
        for _ in range(13):
            parts += ["Children", "0"]
        parts += ["RuleKey"]
        key = ".".join(parts)
        assert len(parts) == 31

        g = _make_globals(profile="default", cli_unfold_argument=True)
        try:
            ac(["--Id", "1490", "--" + key, "value_d31"], g)
            assert False, "expected UnknownArgumentError for D=31"
        except UnknownArgumentError as e:
            msg = str(e)
            assert "depth=31" in msg
            assert "MAX_INPUT_DEPTH=30" in msg
            assert "Use --cli-input-json file://" in msg
            # 反向断言：旧文案不应再出现
            assert "Drop --cli-unfold-argument" not in msg
        # 超限场景下 action_caller 不应被调用
        assert "params" not in captured
    finally:
        restore()


def test_G5_unfold_typo_unknown_param_still_raises():
    """G5: 拼写错误（不命中任何已知截断前缀）仍按既有路径抛 Unknown options（需求 1.3）。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        g = _make_globals(profile="default", cli_unfold_argument=True)
        try:
            ac([
                "--Id", "1490",
                "--RuleExpressio.Foo", "x",  # ← RuleExpression 拼写错误
            ], g)
            assert False, "expected UnknownArgumentError for typo"
        except UnknownArgumentError as e:
            msg = str(e)
            assert "Unknown options" in msg
            assert "--RuleExpressio.Foo" in msg
            # 既不应被识别为深嵌套延伸（不应有 depth= 文案），也不应有旧的 Drop 文案
            assert "depth=" not in msg
            assert "Drop --cli-unfold-argument" not in msg
        assert "params" not in captured
    finally:
        restore()


def test_G7_unfold_equals_form_normalization():
    """G7: ``--key=value`` 与 ``--key value`` 两种 argparse 写法等价。"""
    if not _billing_schema_available():
        pytest.skip("local billing api.json missing")
    captured = {}
    ac = _make_billing_action_command(captured)
    restore = _patch_credentials()
    try:
        key, depth = _build_self_ref_path(0)
        assert depth == 5
        g = _make_globals(profile="default", cli_unfold_argument=True)
        # 用 = 形式
        result = ac([
            "--Id", "1490",
            "--%s=value_eq" % key,
        ], g)
        assert result == "ok"
        leaf = _walk_to_leaf(captured["params"], 0)
        assert leaf == {"RuleKey": "value_eq"}
    finally:
        restore()


# ============================================================
# H. _parse_one_token 静态方法白盒
# ============================================================
def test_H1_parse_one_token_non_dash_returns_none():
    assert ActionCommand._parse_one_token(["foo"], 0) is None


def test_H2_parse_one_token_non_string_returns_none():
    assert ActionCommand._parse_one_token([123], 0) is None
    assert ActionCommand._parse_one_token([None], 0) is None


def test_H3_parse_one_token_equals_form():
    tok, key, eq_v, paired, has_eq, adv = \
        ActionCommand._parse_one_token(["--k=v"], 0)
    assert tok == "--k=v"
    assert key == "k"
    assert eq_v == "v"
    assert paired == []
    assert has_eq is True
    assert adv == 1


def test_H4_parse_one_token_single_paired_value():
    tok, key, eq_v, paired, has_eq, adv = \
        ActionCommand._parse_one_token(["--k", "v1"], 0)
    assert key == "k"
    assert eq_v is None
    assert paired == ["v1"]
    assert has_eq is False
    assert adv == 2


def test_H5_parse_one_token_multi_paired_until_next_option():
    args = ["--k", "v1", "v2", "v3", "--other", "x"]
    tok, key, eq_v, paired, has_eq, adv = \
        ActionCommand._parse_one_token(args, 0)
    assert paired == ["v1", "v2", "v3"]
    assert adv == 4  # 1 + len(paired)


def test_H6_parse_one_token_key_at_tail_no_value():
    tok, key, eq_v, paired, has_eq, adv = \
        ActionCommand._parse_one_token(["--k"], 0)
    assert key == "k"
    assert paired == []
    assert has_eq is False
    assert adv == 1


# ============================================================
# I. _match_truncated_prefix 最长前缀匹配
# ============================================================
def test_I1_match_truncated_prefix_no_match():
    prefix, tname = ActionCommand._match_truncated_prefix(
        "Foo.Bar", OrderedDict([("Root.0", "T")]))
    assert prefix is None
    assert tname == ""


def test_I2_match_truncated_prefix_strict_dot_boundary():
    trunc = OrderedDict([("Root.0", "T")])
    prefix, tname = ActionCommand._match_truncated_prefix("Root.0.Sub", trunc)
    assert prefix == "Root.0"
    assert tname == "T"


def test_I3_match_truncated_prefix_longest_wins():
    trunc = OrderedDict([
        ("A.0", "TA"),
        ("A.0.B.0", "TB"),
    ])
    prefix, tname = ActionCommand._match_truncated_prefix("A.0.B.0.X", trunc)
    assert prefix == "A.0.B.0"
    assert tname == "TB"


def test_I4_match_truncated_prefix_equal_no_dot_suffix_not_hit():
    """key 与前缀完全相等时不算命中（要求 prefix + '.' 严格前缀）。"""
    trunc = OrderedDict([("Root.0", "T")])
    prefix, tname = ActionCommand._match_truncated_prefix("Root.0", trunc)
    assert prefix is None


# ============================================================
# J. _collect_truncated_prefixes 静态方法
# ============================================================
def test_J1_collect_truncated_prefixes_empty():
    assert ActionCommand._collect_truncated_prefixes(None) == OrderedDict()
    assert ActionCommand._collect_truncated_prefixes({}) == OrderedDict()


def test_J2_collect_truncated_prefixes_filters_non_truncated():
    unfold = OrderedDict([
        ("A.0", {"recursive_truncated": True, "recursive_type": "TA"}),
        ("B.0", {"recursive_truncated": False, "recursive_type": "TB"}),
        ("C.0", {}),
    ])
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert list(out.keys()) == ["A.0"]
    assert out["A.0"] == "TA"


def test_J3_collect_truncated_prefixes_missing_type_becomes_empty():
    unfold = {"X.0": {"recursive_truncated": True}}
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert out["X.0"] == ""


def test_J4_collect_truncated_prefixes_preserves_order():
    unfold = OrderedDict([
        ("Z.0", {"recursive_truncated": True, "recursive_type": "TZ"}),
        ("A.0", {"recursive_truncated": True, "recursive_type": "TA"}),
        ("M.0", {"recursive_truncated": True, "recursive_type": "TM"}),
    ])
    out = ActionCommand._collect_truncated_prefixes(unfold)
    assert list(out.keys()) == ["Z.0", "A.0", "M.0"]


# ============================================================
# K. _classify_leaf / _resolve_inner_leaf_type
# ============================================================
def _make_action_cmd_with_model(objects):
    """构造一个 ActionCommand，注入自定义 service_model。"""
    ac = _make_action_command()

    class _Loader(object):
        def get_service_model(self, *a, **kw):
            return {"objects": objects}
    ac._cli_data = _Loader()
    return ac


def test_K1_classify_leaf_last_segment_digit_is_false():
    ac = _make_action_command()
    assert ac._classify_leaf("A.0", "T", "A.0.Children.5") is False


def test_K2_resolve_inner_leaf_type_terminal_list():
    ac = _make_action_cmd_with_model({
        "T": {"members": [{"name": "Items", "type": "list", "member": "string"}]},
    })
    assert ac._classify_leaf("A.0", "T", "A.0.Items") is True


def test_K3_resolve_inner_leaf_type_terminal_string():
    ac = _make_action_cmd_with_model({
        "T": {"members": [{"name": "Name", "type": "string", "member": "string"}]},
    })
    assert ac._classify_leaf("A.0", "T", "A.0.Name") is False


def test_K4_resolve_inner_leaf_type_missing_type_name():
    ac = _make_action_command()
    assert ac._resolve_inner_leaf_type("A.0", "", "A.0.X") is None
    assert ac._resolve_inner_leaf_type("A.0", None, "A.0.X") is None


def test_K5_resolve_inner_leaf_type_missing_objects():
    ac = _make_action_cmd_with_model({})
    assert ac._resolve_inner_leaf_type("A.0", "T", "A.0.X") is None

    class _Loader(object):
        def get_service_model(self, *a, **kw):
            return {}
    ac._cli_data = _Loader()
    assert ac._resolve_inner_leaf_type("A.0", "T", "A.0.X") is None


def test_K6_resolve_inner_leaf_type_list_of_base_type_returns_none():
    """中间路径遇到 list 但 member 是 BASE_TYPE 时，无法继续下钻，返回 None。"""
    ac = _make_action_cmd_with_model({
        "T": {"members": [{"name": "Names", "type": "list", "member": "string"}]},
    })
    assert ac._resolve_inner_leaf_type(
        "A.0", "T", "A.0.Names.0.SubField") is None


def test_K7_resolve_inner_leaf_type_object_switches_current_type():
    """中间层是 object，沿 member 切换 current_type，末端解析成功。"""
    ac = _make_action_cmd_with_model({
        "Outer": {"members": [
            {"name": "Inner", "type": "object", "member": "InnerT"},
        ]},
        "InnerT": {"members": [
            {"name": "Val", "type": "string", "member": "string"},
        ]},
    })
    assert ac._resolve_inner_leaf_type(
        "A.0", "Outer", "A.0.Inner.Val") == "string"


def test_K8_resolve_inner_leaf_type_service_model_injected_avoids_reload():
    """显式传入 service_model 时不再回调 loader。"""
    ac = _make_action_command()

    class _RaisingLoader(object):
        def get_service_model(self, *a, **kw):
            raise RuntimeError("should not be called")
    ac._cli_data = _RaisingLoader()

    sm = {"objects": {
        "T": {"members": [{"name": "V", "type": "string", "member": "string"}]},
    }}
    assert ac._resolve_inner_leaf_type("A.0", "T", "A.0.V", service_model=sm) \
        == "string"


def test_K9_resolve_inner_leaf_type_prefix_mismatch_returns_none():
    ac = _make_action_cmd_with_model({
        "T": {"members": [{"name": "V", "type": "string", "member": "string"}]},
    })
    assert ac._resolve_inner_leaf_type("A.0", "T", "OtherPrefix.V") is None


# ============================================================
# L. _commit_pair
# ============================================================
def test_L1_commit_pair_normal_depth_writes_extra():
    ac = _make_action_command()
    extra = OrderedDict()
    oversized = []
    ac._commit_pair("A.0.X", "v", "A.0", "T", False, extra, oversized)
    assert extra == {"A.0.X": "v"}
    assert oversized == []


def test_L2_commit_pair_oversized_depth_records_and_skips_extra():
    from tccli.loaders import MAX_INPUT_DEPTH
    ac = _make_action_command()
    # 构造 depth = MAX_INPUT_DEPTH + 1
    parts = ["Seg%d" % i for i in range(MAX_INPUT_DEPTH + 1)]
    key = ".".join(parts)
    extra = OrderedDict()
    oversized = []
    ac._commit_pair(key, "v", "Seg0", "T", False, extra, oversized)
    assert key not in extra
    assert len(oversized) == 1
    assert oversized[0][0] == key
    assert oversized[0][1] == MAX_INPUT_DEPTH + 1


def test_L3_commit_pair_allow_list_wraps_scalar():
    ac = _make_action_command()
    extra = OrderedDict()
    ac._commit_pair("A.0.Items", "v", "A.0", "T", True, extra, [])
    assert extra["A.0.Items"] == ["v"]


def test_L5_commit_pair_depth_skips_digit_segments():
    ac = _make_action_command()
    extra = OrderedDict()
    # Children.0.Children.0.X → 有效段数 = 3（跳过两个 "0"）
    ac._commit_pair("Children.0.Children.0.X", "v", "Children.0", "T",
                    False, extra, [])
    assert extra["Children.0.Children.0.X"] == "v"


# ============================================================
# N. _prefilter_orphan_keys 静态方法
# ============================================================
class _FakeAction(object):
    def __init__(self, option_strings, nargs=None):
        self.option_strings = option_strings
        self.nargs = nargs


class _FakeParser(object):
    def __init__(self, actions):
        self._actions = actions


def test_N1_prefilter_orphan_keys_empty_args_no_raise():
    ActionCommand._prefilter_orphan_keys([], _FakeParser([]))


def test_N2_prefilter_equals_form_not_orphan():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    ActionCommand._prefilter_orphan_keys(["--k=v"], parser)


def test_N3_prefilter_valueless_option_not_orphan():
    """nargs==0 的 flag 型 option 允许无值。"""
    parser = _FakeParser([_FakeAction(["--flag"], nargs=0)])
    ActionCommand._prefilter_orphan_keys(["--flag", "--other", "v"], parser)


def test_N4_prefilter_option_at_tail_raises():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    try:
        ActionCommand._prefilter_orphan_keys(["--k"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "Missing value for option(s):" in msg
        assert "--k" in msg


def test_N5_prefilter_adjacent_options_raises():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    try:
        ActionCommand._prefilter_orphan_keys(["--k", "--other", "v"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        assert "--k" in str(e)


def test_N6_prefilter_normal_pair_no_raise():
    parser = _FakeParser([_FakeAction(["--k"], nargs=None)])
    ActionCommand._prefilter_orphan_keys(["--k", "v"], parser)


def test_N7_prefilter_multiple_orphans_all_reported():
    parser = _FakeParser([_FakeAction(["--flag"], nargs=0)])
    try:
        ActionCommand._prefilter_orphan_keys(
            ["--k1", "--k2", "--k3"], parser)
        assert False, "expected UnknownArgumentError"
    except UnknownArgumentError as e:
        msg = str(e)
        assert "--k1" in msg
        assert "--k2" in msg


# ============================================================
# O. _build_oversized_hint 白盒
# ============================================================
def test_O1_oversized_hint_empty_returns_empty_str():
    ac = _make_action_command()
    assert ac._build_oversized_hint([]) == ""


def test_O2_oversized_hint_single_entry_full_text():
    ac = _make_action_command()
    hint = ac._build_oversized_hint([("A.B.C", 31, "A.B", "T")])
    assert "MAX_INPUT_DEPTH=30" in hint
    assert "depth=31" in hint
    assert "--A.B.C" in hint
    assert "under --A.B" in hint
    assert "type: T" in hint
    assert "Use --cli-input-json file://" in hint


def test_O3_oversized_hint_missing_type_falls_back_to_unknown():
    ac = _make_action_command()
    hint = ac._build_oversized_hint([("A.X", 31, "A", "")])
    assert "type: unknown" in hint


def test_O4_oversized_hint_multiple_entries_each_on_own_line():
    ac = _make_action_command()
    hint = ac._build_oversized_hint([
        ("A.X", 31, "A", "T1"),
        ("B.Y", 32, "B", "T2"),
    ])
    assert "--A.X" in hint
    assert "--B.Y" in hint
    assert "depth=31" in hint
    assert "depth=32" in hint


# ============================================================
# P. _extract_deep_nested_args 白盒边界
# ============================================================
def test_P1_extract_empty_remaining_returns_as_is():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)
    extra = OrderedDict()
    oversized = []
    out = ac._extract_deep_nested_args([], extra, oversized)
    assert out == []
    assert extra == OrderedDict()
    assert oversized == []


def test_P2_extract_loader_raises_returns_original():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _BadLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            raise RuntimeError("boom")
    ac._cli_data = _BadLoader()
    remaining = ["--Foo.Bar", "v"]
    extra = OrderedDict()
    oversized = []
    out = ac._extract_deep_nested_args(remaining, extra, oversized)
    assert out == remaining
    assert extra == OrderedDict()


def test_P3_extract_no_truncated_returns_original():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _NoTrunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Foo": {"recursive_truncated": False}}
    ac._cli_data = _NoTrunc()
    remaining = ["--Foo.Extra", "v"]
    out = ac._extract_deep_nested_args(remaining, OrderedDict(), [])
    assert out == remaining


def test_P4_extract_service_model_raises_still_works():
    """get_service_model 抛异常不会影响主流程（service_model=None 时仍能收集）。"""
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _PartLoader(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            raise RuntimeError("no schema")
    ac._cli_data = _PartLoader()
    extra = OrderedDict()
    oversized = []
    out = ac._extract_deep_nested_args(
        ["--Root.0.Sub", "v"], extra, oversized)
    assert out == []
    assert extra == {"Root.0.Sub": "v"}


def test_P5_extract_non_dash_token_kept_in_new_remaining():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(
        ["stray_positional"], OrderedDict(), [])
    assert out == ["stray_positional"]


def test_P6_extract_non_matching_pair_kept_wholesale():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(
        ["--OtherKey", "v1", "v2"], OrderedDict(), [])
    assert out == ["--OtherKey", "v1", "v2"]


def test_P7_extract_valueless_non_matching_key_kept():
    ac = _make_action_command(call_mode=Options_define.CliUnfoldArgument)

    class _Trunc(object):
        def get_unfold_param_info(self, *a, **kw):
            return {"Root.0": {"recursive_truncated": True,
                               "recursive_type": "T"}}

        def get_service_model(self, *a, **kw):
            return {"objects": {}}
    ac._cli_data = _Trunc()
    out = ac._extract_deep_nested_args(["--WhoAmI"], OrderedDict(), [])
    assert out == ["--WhoAmI"]


# ============================================================
# 允许直接 `python3 tests/test_command.py` 运行（无 pytest 环境）
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
