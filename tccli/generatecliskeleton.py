
import json
import sys
import datetime

from tccli.loaders import Loader
from tccli.argument import CustomArgument


def json_encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj


class OverrideRequiredArgsArgument(CustomArgument):

    ARG_DATA = {'name': 'no-required-args'}

    def __init__(self):
        super(OverrideRequiredArgsArgument, self).__init__(**self.ARG_DATA)

    def override_required_args(self, argument_map, args, **kwargs):
        name_in_cmdline = '--' + self.name
        if name_in_cmdline in args:
            for arg_name in argument_map.keys():
                argument_map[arg_name].required = False


class GenerateCliSkeletonArgument(OverrideRequiredArgsArgument):
    ARG_DATA = {
        'name': 'generate-cli-skeleton',
        'help_text': (
            'Prints a JSON skeleton to standard output without sending '
            'an API request. If provided with no value or the value '
            '``input``, prints a sample input JSON that can be used as an '
            'argument for ``--cli-input-json``.'
        ),
        'nargs': '?',
        'const': 'input',
        'choices': ['input'],
    }

    def __init__(self, service_name, version, action_name):
        super(GenerateCliSkeletonArgument, self).__init__()
        self._service_name = service_name
        self._version = version
        self._action_name = action_name

    def override_required_args(self, argument_map, args, **kwargs):
        arg_name = '--' + self.name
        if arg_name in args:
            arg_location = args.index(arg_name)
            try:
                if args[arg_location + 1] == 'output':
                    return
            except IndexError:
                pass
            super(GenerateCliSkeletonArgument, self).override_required_args(argument_map, args, **kwargs)

    def generate_skeleton(self, call_parameters, parsed_args,
                          parsed_globals, **kwargs):
        if not getattr(parsed_args, 'generate_cli_skeleton', None):
            return
        arg_value = parsed_args.generate_cli_skeleton
        return getattr(
            self, '_generate_%s_skeleton' % arg_value.replace('-', '_'))(
                call_parameters=call_parameters, parsed_globals=parsed_globals
        )

    def _generate_input_skeleton(self, **kwargs):
        cli_data = Loader()
        outfile = sys.stdout
        skeleton = cli_data.generate_param_skeleton(self._service_name, self._version,  self._action_name)
        json.dump(skeleton, outfile, indent=4, default=json_encoder)
        outfile.write('\n')
        return 0

    def _generate_output_skeleton(self, **kwargs):
        pass
