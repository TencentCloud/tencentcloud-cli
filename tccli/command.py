# -*- coding:utf-8 -*-

import sys
import copy
import tccli.services as Services
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
            cli_type_name=option_params.get('type'))

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
        self.generate_cli_skeleton_argument = GenerateCliSkeletonArgument(service_name, version, action_name)
        self.cli_input_argument = CliInputJSONArgument()


    @property
    def argument_map(self):
        if self._argument_map is None:
            self._argument_map = self._build_parameter_map()
        return self._argument_map

    def _get_param_model(self):
        return self._cli_data.get_param_info(self._service_name, self._version, self._action_name)

    def _build_parameter_map(self):
        argument_map = OrderedDict()
        arg_model = self._get_param_model()
        for arg_name, arg_info in arg_model.items():
            arg_class = self.ARG_TYPES.get(arg_info["type"], self.DEFAULT_ARG_CLASS)
            arg_object = arg_class(
                name=arg_name,
                argument_model=arg_info,
                is_required=True if arg_info["required"] == "required" else False,
                action_model=self._action_model)
            arg_object.add_to_arg_map(argument_map)

        # building-argument-table #
        self.generate_cli_skeleton_argument.add_to_arg_map(argument_map)
        self.cli_input_argument.add_to_arg_map(argument_map)
        # building-argument-table #

        return argument_map

    def __call__(self, args, parsed_globals):

        # before-building-argument-table-parser
        self.generate_cli_skeleton_argument.override_required_args(self.argument_map, args)
        self.cli_input_argument.override_required_args(self.argument_map, args)
        # before-building-argument-table-parser

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
        action_parameters = self._build_action_parameters(parsed_args, self.argument_map)
        
        # calling-command
        override = self.generate_cli_skeleton_argument.generate_skeleton(
            action_parameters, parsed_args, parsed_globals)
        if override is not None:
            if isinstance(override, Exception):
                raise override
            else:
                return override
        else:
            self.cli_input_argument.add_to_call_parameters(
                action_parameters, parsed_args)
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

    def _create_action_parser(self, argument_map):
        parser = ArgMapArgParser(argument_map)
        return parser

