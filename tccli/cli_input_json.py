# -*- coding: utf-8 -*-

import json
import os
from tccli.exceptions import ParamError, ParamSyntaxError
from tccli.argument import CustomArgument


class OverrideRequiredArgsArgument(CustomArgument):

    ARG_DATA = {'name': 'no-required-args'}

    def __init__(self):
        super(OverrideRequiredArgsArgument, self).__init__(**self.ARG_DATA)

    def override_required_args(self, argument_map, args, **kwargs):
        name_in_cmdline = '--' + self.name
        if name_in_cmdline in args:
            for arg_name in argument_map.keys():
                argument_map[arg_name].required = False


class CliInputArgument(OverrideRequiredArgsArgument):

    def add_to_call_parameters(self, call_parameters, parsed_args, **kwargs):
        # 从文件读取读取参数
        arg_value = self._get_arg_value(parsed_args)
        if arg_value is None:
            return

        loaded_params = self._load_parameters(arg_value)
        if not isinstance(loaded_params, dict):
            raise ParamError(
                self.cli_name,
                "Invalid type: expecting dict, "
                "received %s" % type(loaded_params)
            )
        self._update_call_parameters(call_parameters, loaded_params)

    def _get_arg_value(self, parsed_args):
        arg_value = getattr(parsed_args, self.py_name, None)
        if arg_value is None:
            return

        cli_input_args = [
            k for k, v in vars(parsed_args).items()
            if v is not None and k.startswith('cli_input')
        ]
        if len(cli_input_args) != 1:
            raise ParamSyntaxError(
                'Only one --cli-input- parameter may be specified.'
            )
        # get_paramfile 读取文件内容
        paramfile_data = self._get_paramfile(arg_value, 'file://')
        if paramfile_data is not None:
            return paramfile_data

        return arg_value

    def _get_paramfile(self, path, prefix):
        data = None
        if path.startswith(prefix):
            file_path = os.path.expandvars(os.path.expanduser(path[len(prefix):]))
            try:
                with open(file_path, 'r') as f:
                    data = f.read()
            except (OSError, IOError) as e:
                raise Exception('Unable to load paramfile %s: %s' % (file_path, e))
        else:
            raise Exception("--cli-input-json parameter must be "
                            "followed by a value beginning with 'file://'\n")
        return data

    def _load_parameters(self, arg_value):
        raise NotImplementedError('_load_parameters')

    def _update_call_parameters(self, call_parameters, loaded_parameters):
        for input_key in loaded_parameters.keys():
            if input_key not in call_parameters:
                call_parameters[input_key] = loaded_parameters[input_key]


class CliInputJSONArgument(CliInputArgument):

    ARG_DATA = {
        'name': 'cli-input-json',
        'group_name': 'cli_input',
        'help_text': (
            'Reads arguments from the JSON string provided. The JSON string '
            'follows the format provided by ``--generate-cli-skeleton``. '
        )
    }

    def _load_parameters(self, arg_value):
        try:
            return json.loads(arg_value)
        except ValueError:
            raise ParamError(self.name, "Invalid JSON received.")

