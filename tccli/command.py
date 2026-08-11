# -*- coding:utf-8 -*-

import os
import sys
import copy
import six
import tccli.services as Services
import tccli.options_define as Options_define
from collections import OrderedDict

from tccli import credentials
from tccli.utils import Utils
from tccli.argument import CLIArgument, CustomArgument, ListArgument, BooleanArgument
from tccli.exceptions import UnknownArgumentError
from tccli.loaders import Loader, MAX_INPUT_DEPTH, RECURSIVE_HINT_FILE_OPTION
from tccli.self_ref import is_action_self_referencing
from tccli.argparser import CLIArgParser, ActionArgParser, ArgMapArgParser
from tccli.help_command import CLIHelpCommand, ServiceHelpCommand, ActionHelpCommand
from tccli.configure import ConfigureCommand
from tccli.generatecliskeleton import GenerateCliSkeletonArgument
from tccli.cli_input_json import CliInputJSONArgument
from tccli.cli_unfold_argument import CliUnfoldArgument


class BaseCommand(object):

    def __init__(self):
        self._cli_data = Loader()


class CLICommand(BaseCommand):

    def __init__(self):
        self._command_map = None
        self._argument_map = None
        super(CLICommand, self).__init__()

    def __call__(self, args=None):
        if args is None:
            args = sys.argv[1:]

        if len(args) > 0 and args[0] == "as":
            args[0] = "autoscaling"

        command_map = self._get_command_map()
        parser = self._create_parser(command_map)

        # 解决接口版本(--version) 和 tccli版本(--version)字段冲突
        self._handle_service_version_argumnet(args, parser)
        self._handle_warning(args)

        parsed_args, remaining = parser.parse_known_args(args)
        return command_map[parsed_args.command](remaining, parsed_args)

    def _handle_warning(self, args):
        profile = os.environ.get("TCCLI_PROFILE", "default")
        if "--profile" in args:
            location = args.index("--profile") + 1
            if location < len(args):
                profile = args[location]
        conf_path = os.path.join(os.path.expanduser("~"), ".tccli")
        conf = {}
        if Utils.file_existed(conf_path, profile+".configure")[0]:
            conf = Utils.load_json_msg(os.path.join(conf_path, profile+".configure"))
        if "--warning" not in args and conf.get("warning", "") != "on":
            import warnings
            warnings.filterwarnings("ignore")

    def _handle_service_version_argumnet(self, args, parser):
        if "--version" in args:
            location = args.index("--version")+1
            if location < len(args) and Utils.is_valid_version(args[location]):
                parser.add_argument('--version', dest='service_version',
                                    help='Display the version of this service,'
                                         'For example cvm-2017-03-12-RunInstances')
        else:
            parser.add_argument('--version', dest='service_version',
                                help='Display the version of this service,'
                                     'For example cvm-2017-03-12-RunInstances')

    def _get_service_version(self):
        args = sys.argv[1:]
        if "--version" in args:
            location = args.index("--version")+1
            if location < len(args) and Utils.is_valid_version(args[location]):
                return args[0], args[location]
        return None, None

    def _get_command_map(self):
        if self._command_map is None:
            self._command_map = self._build_command_map()
        return self._command_map

    def _build_command_map(self):
        command_map = OrderedDict()
        # 增加configure命令
        command_map["configure"] = ConfigureCommand()
        available_services = self._get_available_services()
        service, version = self._get_service_version()
        for service_name in available_services:
            if service != service_name:
                service_version = None
            else:
                service_version = version
            command_map[service_name] = ServiceCommand(service_name, service_version)
        return command_map

    def _get_available_services(self):
        available_services = self._cli_data.get_available_services().keys()
        return available_services

    def _create_parser(self, command_map):
        command_map['help'] = CLIHelpCommand()
        parser = CLIArgParser(
            command_map,
            self._cli_data.get_cli_version(),
            self._cli_data.get_description(),
            self._get_argument_map(),
            prog="tccli")
        return parser

    def _get_cli_options(self):
        return self._cli_data.get_cli_option()

    def _create_cli_argument(self, option_name, option_params):
        return CustomArgument(
            option_name, help_text=option_params.get('help', ''),
            dest=option_params.get('dest'),
            default=option_params.get('default'),
            action=option_params.get('action'),
            required=option_params.get('required'),
            choices=option_params.get('choices'),
            cli_type_name=option_params.get('type'),
            const=option_params.get('const'),
            nargs=option_params.get('nargs'))

    def _build_argument_map(self):
        argument_map = OrderedDict()
        cli_options = self._get_cli_options()
        for option in cli_options:
            option_params = copy.copy(cli_options[option])
            cli_argument = self._create_cli_argument(option, option_params)
            cli_argument.add_to_arg_map(argument_map)
        return argument_map

    def _get_argument_map(self):
        if self._argument_map is None:
            self._argument_map = self._build_argument_map()
        return self._argument_map


class ServiceCommand(BaseCommand):

    def __init__(self, service_name, version=None):
        super(ServiceCommand, self).__init__()
        self._service_name = service_name
        if version is None:
            version = self._cli_data.get_service_default_version(service_name)
        available_version_list = self._cli_data.get_available_services()[service_name]
        if version not in available_version_list:
            raise Exception("Version: %s is invalid in service: %s, available versions: %s. \n"
                            "Please check your command or configure file to find out "
                            "if version setting is correct."
                            % (version, service_name, " ".join(available_version_list)))
        self._version = version
        self._command_map = None
        self._service_model = None

    def _get_service_model(self):
        self._service_model = self._cli_data.get_service_model(self._service_name, self._version)
        return self._service_model

    def _get_command_map(self):
        if self._command_map is None:
            self._command_map = self._build_command_map()
        return self._command_map

    def _build_command_map(self):
        command_map = OrderedDict()
        service_model = self._get_service_model()
        for action in service_model["actions"]:
            action_model = service_model["actions"][action]
            action_caller = action_model.get("action_caller", None)
            if not action_caller:
                action_caller = Services.action_caller(self._service_name)()[action]
            cmd = ActionCommand(
                service_name=self._service_name,
                version=self._version,
                action_name=action,
                action_model=action_model,
                action_caller=action_caller,
            )
            cmd._is_self_ref = is_action_self_referencing(
                self._service_name, self._version, action, service_model)
            command_map[action] = cmd
        return command_map

    def __call__(self, args, parsed_globals):
        command_map = self._get_command_map()
        service_parser = self._create_parser(command_map)
        parsed_args, remaining = service_parser.parse_known_args(args)
        return command_map[parsed_args.operation](remaining, parsed_globals)

    def _create_parser(self, command_map):
        command_map['help'] = self.create_help_command()
        return ActionArgParser(actions_map=command_map)

    def create_help_command(self):
        return ServiceHelpCommand(self._service_name, self._version)


class ActionCommand(BaseCommand):
    # 为了兼容老版本cli
    # ARG_TYPES = {
    #     'Array': ListArgument,
    #     'Boolean': BooleanArgument
    # }
    ARG_TYPES = {
        'Array': ListArgument
    }
    DEFAULT_ARG_CLASS = CLIArgument

    def __init__(self, service_name, version, action_name, action_model, action_caller):
        super(ActionCommand, self).__init__()
        self._argument_map = None
        self._service_name = service_name
        if version is None:
            version = self._cli_data.get_service_default_version(service_name)
        self._version = version
        self._action_name = action_name
        self._action_model = action_model
        self._action_caller = action_caller
        self._call_mode = None
        self.generate_cli_skeleton_argument = GenerateCliSkeletonArgument(service_name, version, action_name)
        self.cli_input_argument = CliInputJSONArgument()
        self.cli_unfold_argument = CliUnfoldArgument()
        self.profile = "default"
        self._is_self_ref = False

    @property
    def argument_map(self):
        if self._argument_map is None:
            self._argument_map = self._build_parameter_map()
        return self._argument_map

    def _get_param_model(self):
        if self._call_mode == Options_define.CliUnfoldArgument:
            return self._cli_data.get_unfold_param_info(
                self._service_name, self._version, self._action_name, profile=self.profile, param_array=True)
        else:
            return self._cli_data.get_param_info(self._service_name, self._version, self._action_name)

    def _build_parameter_map(self):
        argument_map = OrderedDict()

        if self._call_mode in [Options_define.GenerateCliSkeleton, Options_define.CliInputJson]:
            return argument_map

        arg_model = self._get_param_model()
        for arg_name, arg_info in arg_model.items():
            if self._call_mode == Options_define.CliUnfoldArgument:
                arg_class = self.ARG_TYPES.get(arg_info["type"], self.DEFAULT_ARG_CLASS)
            else:
                arg_class = self.DEFAULT_ARG_CLASS
            arg_object = arg_class(
                name=arg_name,
                argument_model=arg_info,
                is_required=True if arg_info.get("required") == "Required" else False,
                action_model=self._action_model)
            arg_object.add_to_arg_map(argument_map)
        return argument_map

    def __call__(self, args, parsed_globals):
        if self._is_self_ref:
            return self._call_with_depth_guard(args, parsed_globals)

        self._call_mode = self._get_call_mode(parsed_globals)
        self._get_profile(parsed_globals)

        action_parser = self._create_action_parser(self.argument_map)
        action_parser.add_argument('help', nargs='?')

        parsed_args, remaining = action_parser.parse_known_args(args)
        if parsed_args.help == 'help':
            help_command = self.create_help_command()
            return help_command(remaining, parsed_globals)
        elif parsed_args.help:
            remaining.append(parsed_args.help)
        if remaining:
            raise UnknownArgumentError(
                "Unknown options: %s" % ', '.join(remaining))

        if self._call_mode == Options_define.GenerateCliSkeleton:
            return self.generate_cli_skeleton_argument.generate_skeleton(parsed_globals)

        if self._call_mode == Options_define.CliInputJson:
            action_parameters = self.cli_input_argument.add_to_call_parameters(parsed_globals)
        elif self._call_mode == Options_define.CliUnfoldArgument:
            action_parameters = self.cli_unfold_argument.build_action_parameters(parsed_args)
        else:
            action_parameters = self._build_action_parameters(parsed_args, self.argument_map)
        credentials.maybe_refresh_credential(parsed_globals.profile if parsed_globals.profile else "default")
        return self._action_caller(action_parameters, vars(parsed_globals))

    def _call_with_depth_guard(self, args, parsed_globals):
        """Self-ref 接口专用入口：含 orphan key 过滤、深层嵌套提取、深度超限检测。"""

        self._call_mode = self._get_call_mode(parsed_globals)
        self._get_profile(parsed_globals)

        action_parser = self._create_action_parser(self.argument_map)
        action_parser.add_argument('help', nargs='?')

        if self._call_mode == Options_define.CliUnfoldArgument:
            self._prefilter_orphan_keys(args, action_parser)

        parsed_args, remaining = action_parser.parse_known_args(args)
        if parsed_args.help == 'help':
            help_command = self.create_help_command()
            return help_command(remaining, parsed_globals)
        elif parsed_args.help:
            for idx, tok in enumerate(remaining):
                if isinstance(tok, six.string_types) and tok.startswith("--"):
                    remaining.insert(idx + 1, parsed_args.help)
                    break
            else:
                remaining.append(parsed_args.help)

        extra_unfold_args = OrderedDict()
        oversized_tokens = []  # [(key, depth)]
        if self._call_mode == Options_define.CliUnfoldArgument and remaining:
            remaining = self._extract_deep_nested_args(
                remaining, extra_unfold_args, oversized_tokens)

        if remaining or oversized_tokens:
            hint = self._build_recursive_hint(remaining)
            oversized_hint = self._build_oversized_hint(oversized_tokens)
            error_parts = []
            if remaining:
                error_parts.append("Unknown options: %s" % ', '.join(remaining))
            if oversized_tokens:
                error_parts.append(
                    "Input nesting depth exceeds MAX_INPUT_DEPTH=%d: %s"
                    % (MAX_INPUT_DEPTH,
                       ', '.join("--%s (depth=%d)" % (k, d)
                                 for k, d in oversized_tokens)))
            msg = "\n".join(error_parts)
            tail_hints = [h for h in (hint, oversized_hint) if h]
            if tail_hints:
                msg += "\n\n" + "\n\n".join(tail_hints)
            raise UnknownArgumentError(msg)

        if self._call_mode == Options_define.GenerateCliSkeleton:
            return self.generate_cli_skeleton_argument.generate_skeleton(parsed_globals)

        if self._call_mode == Options_define.CliInputJson:
            action_parameters = self.cli_input_argument.add_to_call_parameters(parsed_globals)
        elif self._call_mode == Options_define.CliUnfoldArgument:
            action_parameters = self.cli_unfold_argument.build_action_parameters(
                parsed_args, extra_unfold_args=extra_unfold_args or None)
        else:
            action_parameters = self._build_action_parameters(parsed_args, self.argument_map)
        credentials.maybe_refresh_credential(parsed_globals.profile if parsed_globals.profile else "default")
        return self._action_caller(action_parameters, vars(parsed_globals))
    def create_help_command(self):
        return ActionHelpCommand(self._service_name, self._version, self._action_name)

    def _build_action_parameters(self, args, argument_map):
        action_params = {}
        parsed_args = vars(args)
        for argument_object in argument_map.values():
            name = argument_object.name
            if name in parsed_args:
                value = parsed_args[name]
                argument_object.add_to_params(action_params, value)
        return action_params

    def _build_recursive_hint(self, remaining):
        """为命中自引用截断前缀的未知参数生成提示文案，指向 --cli-input-json file://。"""
        # 仅在 --cli-unfold-argument 模式下才有意义
        if self._call_mode != Options_define.CliUnfoldArgument:
            return ""
        try:
            unfold_params = self._cli_data.get_unfold_param_info(
                self._service_name, self._version, self._action_name,
                profile=self.profile, param_array=True)
        except Exception:
            return ""

        # 收集所有被自引用截断的 leaf 前缀，例如：
        #   "RuleList.RuleDetail.Children.0" -> "AllocationRuleExpression"
        truncated = self._collect_truncated_prefixes(unfold_params)
        if not truncated:
            return ""

        matched = OrderedDict()  # 命中的非法参数 -> (截断前缀, 自引用类型名)
        for token in remaining:
            if not isinstance(token, six.string_types) or not token.startswith("--"):
                continue
            key = token[2:]
            for prefix, type_name in truncated.items():
                # 严格前缀匹配："RuleList.RuleDetail.Children.0.RuleValue"
                # 应被 "RuleList.RuleDetail.Children.0" 命中。
                if key.startswith(prefix + "."):
                    matched[token] = (prefix, type_name)
                    break

        if not matched:
            return ""

        lines = ["Hint: the following option(s) drill into a self-referencing type "
                 "that --cli-unfold-argument cannot expand further:"]
        for token, (prefix, type_name) in matched.items():
            lines.append("  %s  (under --%s, self-referencing type: %s)"
                         % (token, prefix, type_name or "unknown"))
        lines.append("")
        lines.append("To pass deeper nested values:")
        lines.append("  " + RECURSIVE_HINT_FILE_OPTION)
        return "\n".join(lines)

    @staticmethod
    def _collect_truncated_prefixes(unfold_params):
        """从 get_unfold_param_info 结果中收集自引用截断 leaf 前缀。

        :return: ``OrderedDict[prefix_key, type_name]``，仅含 recursive_truncated 为 True 的项。
        """
        truncated = OrderedDict()
        if not unfold_params:
            return truncated
        for name, info in unfold_params.items():
            if info and info.get("recursive_truncated"):
                truncated[name] = info.get("recursive_type") or ""
        return truncated

    def _extract_deep_nested_args(self, remaining, extra_unfold_args, oversized_tokens):
        """从 ``remaining`` 提取命中自引用截断前缀的扁平参数并按深度分流。

        :param remaining: argparse 未识别 token 列表。
        :param extra_unfold_args: 输出，深度 ≤ MAX_INPUT_DEPTH 的 ``OrderedDict[key, value]``。
        :param oversized_tokens: 输出，深度超限的 ``List[(key, depth)]``。
        :return: 剔除已消费 token 后剩余的未识别 token 列表。
        """
        if not remaining:
            return remaining
        try:
            unfold_params = self._cli_data.get_unfold_param_info(
                self._service_name, self._version, self._action_name,
                profile=self.profile, param_array=True)
        except Exception:
            return remaining
        truncated = self._collect_truncated_prefixes(unfold_params)
        if not truncated:
            return remaining

        object_model = None
        new_remaining = []
        i, n = 0, len(remaining)
        while i < n:
            tok = remaining[i]
            # --- 内联 token 解析：支持 --key=value 和 --key v1 v2 两种形式 ---
            if not isinstance(tok, six.string_types) or not tok.startswith("--"):
                new_remaining.append(tok)
                i += 1
                continue
            if "=" in tok:
                key, eq_value = tok[2:].split("=", 1)
                has_eq, paired, advance = True, [], 1
            else:
                key = tok[2:]
                j = i + 1
                paired = []
                while j < n and isinstance(remaining[j], six.string_types) \
                        and not remaining[j].startswith("--"):
                    paired.append(remaining[j])
                    j += 1
                has_eq, advance = False, 1 + len(paired)

            # 截断前缀只负责判断该 key 是否允许进入补偿链路。
            if not self._is_recursive_key(key, truncated):
                new_remaining.append(tok)
                new_remaining.extend(paired)
                i += advance
                continue

            # 深度限制优先于 schema 查询，超限参数无需加载和遍历 API 模型。
            depth = sum(1 for seg in key.split(".") if not seg.isdigit())
            if depth > MAX_INPUT_DEPTH:
                oversized_tokens.append((key, depth))
                i += advance
                continue

            if not has_eq and not paired:
                new_remaining.append(tok)
                i += advance
                continue

            if object_model is None:
                try:
                    service_model = self._cli_data.get_service_model(
                        self._service_name, self._version)
                    object_model = service_model.get("objects", {})
                except Exception:
                    object_model = {}
            shape = self._get_key_type(
                key, self._action_name + "Request", object_model)
            if shape is None:
                new_remaining.append(tok)
                new_remaining.extend(paired)
                i += advance
                continue

            if has_eq:
                value = [eq_value] if shape == "list" else eq_value
            elif shape == "list":
                value = paired
            elif len(paired) == 1:
                value = paired[0]
            else:
                # 标量参数只接受一个值，保持未消费以沿用 Unknown options 错误路径。
                new_remaining.append(tok)
                new_remaining.extend(paired)
                i += advance
                continue

            extra_unfold_args[key] = value
            i += advance

        return new_remaining

    @staticmethod
    def _get_key_type(key, root_type, object_model):
        """查询完整扁平 key 的值形态，返回 ``list``、``scalar`` 或 ``None``。"""
        if not key or not root_type or not object_model:
            return None

        segments = key.split(".")
        current_type = root_type
        index = 0
        while index < len(segments):
            segment = segments[index]
            if segment.isdigit():
                return None

            members = object_model.get(current_type, {}).get("members", [])
            if isinstance(members, dict):
                member_info = members.get(segment)
            else:
                member_info = next(
                    (item for item in members if item.get("name") == segment), None)
            if not member_info:
                return None

            member_type = str(member_info.get("type", "")).lower()
            if index == len(segments) - 1:
                return "list" if member_type in ("list", "array") else "scalar"

            member = member_info.get("member")
            if member_type in ("list", "array"):
                index += 1
                if index >= len(segments) or not segments[index].isdigit():
                    return None
                # 数组下标只能用于继续定位元素字段，不能作为完整 key 的末段。
                if index == len(segments) - 1:
                    return None

            if member not in object_model:
                return None
            current_type = member
            index += 1
        return None

    @staticmethod
    def _is_recursive_key(key, truncated):
        """判断 ``key`` 是否严格位于任一自引用截断前缀之下。"""
        return any(key.startswith(prefix + ".") for prefix in truncated)

    def _build_oversized_hint(self, oversized_tokens):
        """为深度超限项构造错误提示文案，指向 --cli-input-json file://；空列表返回空串。"""
        if not oversized_tokens:
            return ""
        lines = ["Hint: the following option(s) exceed --cli-unfold-argument's "
                 "supported nesting depth (MAX_INPUT_DEPTH=%d):" % MAX_INPUT_DEPTH]
        for key, depth in oversized_tokens:
            lines.append("  --%s  (depth=%d, exceeds MAX_INPUT_DEPTH=%d)"
                         % (key, depth, MAX_INPUT_DEPTH))
        lines.append("")
        lines.append("To pass this request:")
        lines.append("  " + RECURSIVE_HINT_FILE_OPTION)
        return "\n".join(lines)

    def _get_profile(self, parsed_globals):
        if getattr(parsed_globals, Options_define.Profile):
            self.profile = getattr(parsed_globals, Options_define.Profile)
        else:
            self.profile = "default"

    def _get_call_mode(self, parsed_globals):
        if getattr(parsed_globals, Options_define.GenerateCliSkeleton.replace('-', '_'), None):
            return Options_define.GenerateCliSkeleton

        if getattr(parsed_globals, Options_define.CliInputJson.replace('-', '_'), None):
            return Options_define.CliInputJson

        if getattr(parsed_globals, Options_define.CliUnfoldArgument.replace('-', '_'), None):
            return Options_define.CliUnfoldArgument

    def _create_action_parser(self, argument_map):
        parser = ArgMapArgParser(argument_map)
        return parser

    @staticmethod
    def _prefilter_orphan_keys(args, action_parser):
        """在 argparse 解析前扫描 args，检测无值的 --key 并抛错。"""
        if not args:
            return
        valueless_opts = set()
        for act in action_parser._actions:
            if act.nargs == 0:
                valueless_opts.update(act.option_strings)
        orphan_tokens = []
        n = len(args)
        i = 0
        while i < n:
            tok = args[i]
            if not isinstance(tok, six.string_types) or not tok.startswith("--") or "=" in tok:
                i += 1
                continue
            if tok in valueless_opts:
                i += 1
                continue
            is_last = (i == n - 1)
            next_is_opt = (not is_last) and isinstance(args[i + 1], six.string_types) \
                and args[i + 1].startswith("--")
            if is_last or next_is_opt:
                orphan_tokens.append(tok)
            i += 1
        if orphan_tokens:
            raise UnknownArgumentError(
                "Missing value for option(s): %s\n\n"
                "Under --cli-unfold-argument mode, every --key must be immediately "
                "followed by its value(s), or remove the key if you intend to leave it empty."
                % ", ".join(orphan_tokens))
