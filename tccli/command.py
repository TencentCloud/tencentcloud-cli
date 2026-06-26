# -*- coding:utf-8 -*-

import os
import sys
import copy
import tccli.services as Services
import tccli.options_define as Options_define
from collections import OrderedDict

from tccli import credentials
from tccli.utils import Utils
from tccli.argument import CLIArgument, CustomArgument, ListArgument, BooleanArgument
from tccli.exceptions import UnknownArgumentError
from tccli.loaders import Loader, MAX_INPUT_DEPTH, RECURSIVE_HINT_FILE_OPTION, BASE_TYPE
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
            command_map[action] = ActionCommand(
                service_name=self._service_name,
                version=self._version,
                action_name=action,
                action_model=action_model,
                action_caller=action_caller,
            )
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

        # 深嵌套延伸识别：仅 --cli-unfold-argument 模式下，把命中截断前缀且
        # 深度 ≤ MAX_INPUT_DEPTH 的扁平参数收集到 extra_unfold_args，
        # 深度超限的记入 oversized_tokens 用于报错。
        extra_unfold_args = OrderedDict()
        oversized_tokens = []  # [(key, depth, prefix, type_name)]
        if self._call_mode == Options_define.CliUnfoldArgument and remaining:
            remaining = self._extract_deep_nested_args(
                remaining, extra_unfold_args, oversized_tokens)

        if remaining or oversized_tokens:
            # 分别为未知参数与深度超限项生成针对性提示
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
                                 for k, d, _p, _t in oversized_tokens)))
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
            if not isinstance(token, str) or not token.startswith("--"):
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

    def _resolve_inner_leaf_type(self, prefix, type_name, key, service_model=None):
        """按内层 schema 解析 ``key`` 末端字段的 ``type``。

        :param prefix: 截断 leaf 前缀，如 ``"RuleList.RuleDetail"``。
        :param type_name: 截断点的自引用类型名，如 ``"AllocationRuleExpression"``。
        :param key: 完整扁平键，如 ``"RuleList.RuleDetail.Children.0.RuleValue"``。
        :param service_model: 可选，调用方预取的 service_model，避免重复读盘。
        :return: 末端字段的 ``type`` 字符串（如 ``"list"``/``"string"``）；解析失败返回 None。
        """
        if not type_name:
            return None
        if service_model is None:
            try:
                service_model = self._cli_data.get_service_model(
                    self._service_name, self._version)
            except Exception:
                return None
        objects = service_model.get("objects") if service_model else None
        if not objects:
            return None
        if not key.startswith(prefix + "."):
            return None
        inner_segments = key[len(prefix) + 1:].split(".")
        current_type = type_name
        last_member_type = None
        idx = 0
        while idx < len(inner_segments):
            seg = inner_segments[idx]
            if seg.isdigit():
                idx += 1
                continue
            type_def = objects.get(current_type)
            if not type_def:
                return None
            members = type_def.get("members")
            if not isinstance(members, list):
                return None
            field = None
            for m in members:
                if isinstance(m, dict) and m.get("name") == seg:
                    field = m
                    break
            if not field:
                return None
            field_type = field.get("type")
            field_member = field.get("member")
            last_member_type = field_type
            if idx == len(inner_segments) - 1:
                return field_type
            if field_type == "list":
                if field_member in BASE_TYPE:
                    return None
                current_type = field_member
            elif field_type == "object":
                current_type = field_member
            else:
                return None
            idx += 1
        return last_member_type

    def _extract_deep_nested_args(self, remaining, extra_unfold_args, oversized_tokens):
        """从 ``remaining`` 提取命中自引用截断前缀的扁平参数并按深度分流。

        :param remaining: argparse 未识别 token 列表。
        :param extra_unfold_args: 输出，深度 ≤ MAX_INPUT_DEPTH 的 ``OrderedDict[key, value]``。
        :param oversized_tokens: 输出，深度超限的 ``List[(key, depth, prefix, type_name)]``。
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

        try:
            service_model = self._cli_data.get_service_model(
                self._service_name, self._version)
        except Exception:
            service_model = None

        new_remaining = []
        unmatched_orphan_keys = []
        orphan_value_pool = []
        list_field_keys = []
        i = 0
        n = len(remaining)
        while i < n:
            parsed = self._parse_one_token(remaining, i)
            if parsed is None:
                new_remaining.append(remaining[i])
                i += 1
                continue
            tok, key, eq_value, paired_values, has_eq, advance = parsed

            prefix, type_name = self._match_truncated_prefix(key, truncated)
            if prefix is None:
                new_remaining.append(tok)
                new_remaining.extend(paired_values)
                i += advance
                continue

            allow_list = self._classify_leaf(prefix, type_name, key, service_model)

            if has_eq:
                value = eq_value
            elif paired_values:
                if allow_list:
                    value = paired_values[0] if len(paired_values) == 1 else list(paired_values)
                else:
                    value = paired_values[0]
                    orphan_value_pool.extend(paired_values[1:])
            else:
                unmatched_orphan_keys.append((tok, key, prefix, type_name))
                new_remaining.append(tok)
                i += advance
                continue

            self._commit_pair(key, value, prefix, type_name, allow_list,
                              extra_unfold_args, oversized_tokens, list_field_keys)
            i += advance

        self._yield_to_orphans(unmatched_orphan_keys, orphan_value_pool,
                               list_field_keys, extra_unfold_args)
        return self._drain_orphan_pool(unmatched_orphan_keys, orphan_value_pool,
                                       extra_unfold_args, oversized_tokens, new_remaining,
                                       service_model)

    @staticmethod
    def _parse_one_token(remaining, i):
        """从 ``remaining[i]`` 解析一个 ``--k v`` / ``--k=v`` token。

        :return: ``(tok, key, eq_value, paired_values, has_eq, advance)``；非 ``--`` 开头返回 ``None``。
        """
        tok = remaining[i]
        if not isinstance(tok, str) or not tok.startswith("--"):
            return None
        if "=" in tok:
            key, eq_value = tok[2:].split("=", 1)
            return tok, key, eq_value, [], True, 1
        key = tok[2:]
        paired = []
        j = i + 1
        n = len(remaining)
        while j < n and isinstance(remaining[j], str) \
                and not remaining[j].startswith("--"):
            paired.append(remaining[j])
            j += 1
        return tok, key, None, paired, False, 1 + len(paired)

    def _classify_leaf(self, prefix, type_name, key, service_model=None):
        """判断 ``key`` 末段是否为 list 类型字段。"""
        last_seg = key.rsplit(".", 1)[-1] if "." in key else key
        if last_seg.isdigit():
            return False
        return self._resolve_inner_leaf_type(prefix, type_name, key, service_model) == "list"

    def _commit_pair(self, key, value, prefix, type_name, allow_list,
                     extra_unfold_args, oversized_tokens, list_field_keys=None):
        """根据深度把 ``(key, value)`` 归入 ``extra_unfold_args`` 或 ``oversized_tokens``。"""
        depth = len(key.split("."))
        if depth > MAX_INPUT_DEPTH:
            oversized_tokens.append((key, depth, prefix, type_name))
            return
        if allow_list and not isinstance(value, list):
            value = [value]
        extra_unfold_args[key] = value
        if list_field_keys is not None and allow_list \
                and isinstance(value, list) and len(value) > 1:
            list_field_keys.append(key)

    @staticmethod
    def _yield_to_orphans(unmatched_orphan_keys, orphan_value_pool,
                          list_field_keys, extra_unfold_args):
        """从最后注册的 list 字段尾部剥离值补给 ``orphan_value_pool``。"""
        deficit = len(unmatched_orphan_keys) - len(orphan_value_pool)
        while deficit > 0 and list_field_keys:
            target_key = list_field_keys[-1]
            target_value = extra_unfold_args.get(target_key)
            if isinstance(target_value, list) and len(target_value) > 1:
                orphan_value_pool.append(target_value.pop())
                deficit -= 1
                if len(target_value) == 1:
                    extra_unfold_args[target_key] = target_value
                    list_field_keys.pop()
                elif len(target_value) == 0:
                    list_field_keys.pop()
            else:
                list_field_keys.pop()

    def _drain_orphan_pool(self, unmatched_orphan_keys, orphan_value_pool,
                           extra_unfold_args, oversized_tokens, new_remaining,
                           service_model=None):
        """用 ``orphan_value_pool`` 按出现顺序补给前面缺值的孤 key，剔除已消费 token。"""
        if not unmatched_orphan_keys or not orphan_value_pool:
            return new_remaining
        consumed = set()
        pair_count = min(len(unmatched_orphan_keys), len(orphan_value_pool))
        for k_idx in range(pair_count):
            orig_tok, key, prefix, type_name = unmatched_orphan_keys[k_idx]
            allow_list = self._classify_leaf(prefix, type_name, key, service_model)
            self._commit_pair(key, orphan_value_pool[k_idx], prefix, type_name,
                              allow_list, extra_unfold_args, oversized_tokens)
            consumed.add(orig_tok)
        return [t for t in new_remaining if t not in consumed]

    @staticmethod
    def _match_truncated_prefix(key, truncated):
        """在 ``truncated`` 中按最长前缀匹配 ``key``，返回 ``(prefix, type_name)`` 或 ``(None, "")``。"""
        best_prefix = None
        best_type = ""
        for prefix, type_name in truncated.items():
            if key.startswith(prefix + ".") and \
                    (best_prefix is None or len(prefix) > len(best_prefix)):
                best_prefix = prefix
                best_type = type_name
        return best_prefix, best_type

    def _build_oversized_hint(self, oversized_tokens):
        """为深度超限项构造错误提示文案，指向 --cli-input-json file://；空列表返回空串。"""
        if not oversized_tokens:
            return ""
        lines = ["Hint: the following option(s) exceed --cli-unfold-argument's "
                 "supported nesting depth (MAX_INPUT_DEPTH=%d):" % MAX_INPUT_DEPTH]
        for key, depth, prefix, type_name in oversized_tokens:
            lines.append("  --%s  (depth=%d, exceeds MAX_INPUT_DEPTH=%d, "
                         "under --%s, type: %s)"
                         % (key, depth, MAX_INPUT_DEPTH, prefix, type_name or "unknown"))
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
