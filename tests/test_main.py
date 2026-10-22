# -*- coding: utf-8 -*-
import importlib
import io
import sys
import unittest

import six

try:
    from unittest import mock
except ImportError:
    import mock  # type: ignore

import tccli.log as log_module
from tccli.exceptions import ConfigurationError, UnknownArgumentError
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


class _IsolatedStdout(object):
    encoding = "utf-8"

    def __init__(self):
        self.buffer = io.BytesIO()


def _import_main_module():
    """Isolate tccli.main's stdout replacement from pytest capture."""
    with mock.patch.object(log_module, "init", return_value=mock.Mock()):
        with mock.patch.object(sys, "stdout", _IsolatedStdout()):
            return importlib.import_module("tccli.main")


main_module = _import_main_module()


class TestMainErrorOutput(unittest.TestCase):

    def _run_with_error(self, error):
        stderr = six.StringIO()
        with mock.patch.object(main_module, "CLICommand") as command_class:
            with mock.patch.object(main_module.sys, "stderr", stderr):
                command_class.return_value.side_effect = error
                return_code = main_module.main()
        return return_code, stderr.getvalue()

    def test_configuration_error_does_not_print_usage(self):
        return_code, stderr = self._run_with_error(
            ConfigurationError("configuration failed"))

        self.assertEqual(return_code, 255)
        self.assertEqual(stderr, "configuration failed\n")
        self.assertNotIn("usage:", stderr)

    def test_sdk_error_does_not_print_usage(self):
        return_code, stderr = self._run_with_error(
            TencentCloudSDKException(
                "InvalidParameter", "invalid value", "request-id"))

        self.assertEqual(return_code, 255)
        self.assertIn("code:InvalidParameter", stderr)
        self.assertIn("message:invalid value", stderr)
        self.assertIn("requestId:request-id", stderr)
        self.assertNotIn("usage:", stderr)

    def test_unknown_argument_error_still_prints_usage(self):
        return_code, stderr = self._run_with_error(
            UnknownArgumentError("unknown option"))

        self.assertEqual(return_code, 255)
        self.assertIn("usage:", stderr)
        self.assertIn("unknown option", stderr)
