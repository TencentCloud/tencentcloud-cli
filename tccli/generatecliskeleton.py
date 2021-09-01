
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


class GenerateCliSkeletonArgument(CustomArgument):
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
        super(GenerateCliSkeletonArgument, self).__init__(**self.ARG_DATA)
        self._service_name = service_name
        self._version = version
        self._action_name = action_name

    def generate_skeleton(self, parsed_args, **kwargs):
        if not getattr(parsed_args, 'generate_cli_skeleton', None):
            return
        arg_value = parsed_args.generate_cli_skeleton
        return getattr(
            self, '_generate_%s_skeleton' % arg_value.replace('-', '_'))()

    def _generate_input_skeleton(self, **kwargs):
        cli_data = Loader()
        outfile = sys.stdout
        skeleton = cli_data.generate_param_skeleton(self._service_name, self._version, self._action_name)
        json.dump(skeleton, outfile, indent=4, default=json_encoder)
        outfile.write('\n')
        return 0

    def _generate_output_skeleton(self, **kwargs):
        pass
