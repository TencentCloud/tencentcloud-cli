# -*- coding: utf-8 -*-

import json
import os
from tccli.exceptions import ParamError, ParamSyntaxError
from tccli.argument import CustomArgument


class CliInputArgument(CustomArgument):

    def add_to_call_parameters(self, parsed_args, **kwargs):
        call_parameters = {}
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
        return call_parameters

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

    def __init__(self):
        super(CliInputJSONArgument, self).__init__(**self.ARG_DATA)

    def _load_parameters(self, arg_value):
        try:
            return json.loads(arg_value)
        except ValueError:
            raise ParamError(self.name, "Invalid JSON received.")

