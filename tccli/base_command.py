# -*- coding: utf-8 -*-

import logging
from collections import OrderedDict
from tccli.argparser import ArgMapArgParser
from tccli.exceptions import ParamValidationError
from tccli.argument import CustomArgument

LOG = logging.getLogger(__name__)

class BasicCommand(object):
    NAME = ''
    DESCRIPTION = ''
    SYNOPSIS = ''
    EXAMPLES = ''
    ARG_TABLE = []
    SUBCOMMANDS = []

    def __init__(self):
        self._arg_map = None
        self._subcommand_map = None

    def __call__(self, args, parsed_globals):
        self._subcommand_map = self._build_subcommand_map()
        self._arg_map = self._build_arg_map()
        parser = ArgMapArgParser(self.arg_map, self.subcommand_map)
        parsed_args, remaining = parser.parse_known_args(args)

        if hasattr(parsed_args, 'help'):
            self._display_help(parsed_args, parsed_globals)
        elif getattr(parsed_args, 'subcommand', None) is None:
            if remaining:
                raise ParamValidationError(
                    "Unknown options: %s" % ','.join(remaining)
                )
            rc = self._run_main(parsed_args, parsed_globals)
            if rc is None:
                return 0
            else:
                return rc
        else:
            return self.subcommand_map[parsed_args.subcommand](remaining, parsed_globals)

    def _run_main(self, parsed_args, parsed_globals):
        raise NotImplementedError("_run_main")

    def _build_subcommand_map(self):
        subcommand_table = OrderedDict()
        for subcommand in self.SUBCOMMANDS:
            subcommand_name = subcommand['name']
            subcommand_class = subcommand['command_class']
            subcommand_table[subcommand_name] = subcommand_class()
        return subcommand_table

    def _display_help(self, parsed_args, parsed_globals):
        help_command = self.create_help_command()
        help_command(parsed_args, parsed_globals)

    def create_help_command(self):
        raise NotImplementedError("create_help_command")

    def create_help_command_map(self):
        commands = {}
        for command in self.SUBCOMMANDS:
            commands[command['name']] = command['command_class']()
        return commands

    def _build_arg_map(self):
        arg_table = OrderedDict()
        for arg_data in self.ARG_TABLE:
            custom_argument = CustomArgument(**arg_data)
            arg_table[arg_data['name']] = custom_argument
        return arg_table

    @property
    def arg_map(self):
        if self._arg_map is None:
            self._arg_map = self._build_arg_map()
        return self._arg_map

    @property
    def subcommand_map(self):
        if self._subcommand_map is None:
            self._subcommand_map = self._build_subcommand_map()
        return self._subcommand_map

    @property
    def name(self):
        return self.NAME


