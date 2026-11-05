# -*- coding:utf8 -*-
import argparse
import unittest

from tccli.argument import BooleanArgument, CLIArgument
from tccli.argparser import ArgMapArgParser


def test_bool_argument():
    args = ["--TestTrue", "true",
            "--TestFalse", "false",
            "--TestT", "t",
            "--TestF", "f",
            "--TestOne", "1",
            "--TestZero", "0",]
    arg_model = {
        "TestTrue": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
        "TestFalse": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
        "TestT": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
        "TestF": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
        "TestOne": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
        "TestZero": {
            "type": "Boolean",
            "type_name": "Boolean",
            "required": "Required",
            "document": "test bool parse"
        },
    }
    action_model = {}
    argument_map = {}
    for arg_name, arg_info in arg_model.items():
        argument_map[arg_name] = CLIArgument(
            name=arg_name,
            argument_model=arg_info,
            is_required=True if arg_info.get("required") == "Required" else False,
            action_model=action_model
        )
    parser = ArgMapArgParser(argument_map)
    parsed_args, _ = parser.parse_known_args(args)
    assert parsed_args.TestTrue == True
    assert parsed_args.TestFalse == False
    assert parsed_args.TestT == True
    assert parsed_args.TestF == False
    assert parsed_args.TestOne == True
    assert parsed_args.TestZero == False


test_bool_argument()


class TestArgparseHelpEscaping(unittest.TestCase):

    @staticmethod
    def _argument_model(document):
        return {
            "document": document,
            "type": "Boolean",
        }

    def test_cli_argument_preserves_literal_percent_in_formatted_help(self):
        document = "Stop warmup when more than 50% of nodes are warming up."
        argument = CLIArgument(
            "EnabledProtection",
            self._argument_model(document),
            action_model={},
        )
        parser = argparse.ArgumentParser()

        argument.add_to_parser(parser)
        help_text = parser.format_help()
        normalized_help = " ".join(help_text.split())

        self.assertEqual(argument.documentation, document)
        self.assertIn(document, normalized_help)
        self.assertNotIn("50%%", help_text)

    def test_boolean_argument_preserves_multiple_literal_percents(self):
        document = "CPU 50%, memory 25%%."
        argument = BooleanArgument(
            "EnabledProtection",
            self._argument_model(document),
            action_model={},
        )
        parser = argparse.ArgumentParser()

        argument.add_to_parser(parser)
        help_text = parser.format_help()
        normalized_help = " ".join(help_text.split())

        self.assertEqual(argument.documentation, document)
        self.assertIn(document, normalized_help)
        self.assertNotIn("50%%", help_text)