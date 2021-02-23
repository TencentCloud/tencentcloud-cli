# -*- coding:utf-8 -*-

import os
import sys
import copy
import tccli.services as Services
import tccli.options_define as Options_define
from collections import OrderedDict
from tccli.utils import Utils
from tccli.argument import CLIArgument, CustomArgument, ListArgument, BooleanArgument
from tccli.exceptions import UnknownArgumentError
from tccli.loaders import Loader
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

        parsed_args, remaining = parser.parse_known_args(args)
        return command_map[parsed_args.command](remaining, parsed_args)

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
            raise Exception("available versions: %s" % " ".join(available_version_list))
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
            command_map[action] = ActionCommand(
                service_name=self._service_name,
                version=self._version,
                action_name=action,
                action_model=action_model,
                action_caller=Services.action_caller(self._service_name)()[action],
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
                is_required=True if arg_info["required"] == "Required" else False,
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

