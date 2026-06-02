# -*- coding: utf-8 -*-
"""Unit tests for the global ``--request-client`` option.

Covers:
  * ``options_define`` constant & ``ACTION_GLOBAL_OPT`` registration
  * ``loaders.get_cli_option`` registration & help text
  * ``configure`` integration (``config_list`` / ``set`` / ``get`` / ``list``)
  * ``parse_global_arg`` reading priority: CLI > profile.configure > None
  * Final ``ClientProfile.request_client`` assembly inside an action call
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

import six

try:
    # Python 3.3+
    from unittest import mock
except ImportError:
    # Python 2: requires the third-party ``mock`` package.
    import mock

import tccli.options_define as OptionsDefine
from tccli import __version__
from tccli.configure import (
    BasicConfigure,
    ConfigureGetCommand,
    ConfigureListCommand,
    ConfigureSetCommand,
)
from tccli.loaders import HELPER_MAP, Loader
from tccli.services.cvm import cvm_client


# ----------------------------------------------------------------------------
# 1. options_define / loaders / configure static registration
# ----------------------------------------------------------------------------
class TestRequestClientRegistration(unittest.TestCase):
    def test_options_define_constant(self):
        self.assertEqual(OptionsDefine.RequestClient, "request-client")

    def test_action_global_opt_contains_request_client(self):
        self.assertIn(OptionsDefine.RequestClient, OptionsDefine.ACTION_GLOBAL_OPT)

    def test_loader_cli_option_registered(self):
        opts = Loader().get_cli_option()
        self.assertIn("request-client", opts)
        self.assertEqual(opts["request-client"]["help"], HELPER_MAP["--request-client"])

    def test_helper_map_has_request_client(self):
        self.assertIn("--request-client", HELPER_MAP)
        self.assertIn("request client", HELPER_MAP["--request-client"].lower())

    def test_configure_config_list_contains_request_client(self):
        bc = BasicConfigure()
        self.assertIn(OptionsDefine.RequestClient, bc.config_list)


# ----------------------------------------------------------------------------
# 2. parse_global_arg behaviour (cvm_client as representative)
# ----------------------------------------------------------------------------
def _build_parsed_globals(profile_name, request_client=None):
    """Build a dict mimicking ``vars(parsed_globals)`` produced by argparse.

    All keys use the same form (underscored where the option name has a dash)
    that argparse generates as ``dest``.
    """
    return {
        OptionsDefine.SecretId: "AKIDtest",
        OptionsDefine.SecretKey: "SKtest",
        OptionsDefine.Token: None,
        OptionsDefine.RoleArn.replace("-", "_"): None,
        OptionsDefine.RoleSessionName.replace("-", "_"): None,
        OptionsDefine.UseCVMRole.replace("-", "_"): False,
        OptionsDefine.Region: "ap-guangzhou",
        OptionsDefine.Endpoint: None,
        OptionsDefine.Version: None,
        OptionsDefine.ServiceVersion: None,
        OptionsDefine.Filter: None,
        OptionsDefine.Profile: profile_name,
        OptionsDefine.Timeout: None,
        OptionsDefine.Output: None,
        OptionsDefine.HttpsProxy.replace("-", "_"): None,
        OptionsDefine.GenerateCliSkeleton.replace("-", "_"): None,
        OptionsDefine.CliInputJson.replace("-", "_"): None,
        OptionsDefine.CliUnfoldArgument.replace("-", "_"): None,
        OptionsDefine.Waiter: None,
        OptionsDefine.Language: None,
        OptionsDefine.RequestClient.replace("-", "_"): request_client,
    }


class TestParseGlobalArgRequestClient(unittest.TestCase):
    """Verify priority: CLI value > configure file value > None."""

    def setUp(self):
        # Isolate ~/.tccli so the test does not depend on / pollute the user's
        # real config directory.
        self.tmp_home = tempfile.mkdtemp(prefix="tccli_test_home_")
        self.cli_path = os.path.join(self.tmp_home, ".tccli")
        os.makedirs(self.cli_path)
        self._home_patcher = mock.patch.dict(os.environ, {"HOME": self.tmp_home})
        self._home_patcher.start()
        # `os.path.expanduser` honours $HOME on POSIX. Force expanduser to use
        # tmp_home regardless of platform.
        self._expand_patcher = mock.patch(
            "os.path.expanduser", lambda p: p.replace("~", self.tmp_home)
        )
        self._expand_patcher.start()

        # Minimal cvm configure file so parse_global_arg can resolve version
        # and endpoint.
        self.profile = "rc_unittest"
        cfg = {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-guangzhou",
                OptionsDefine.Output: "json",
            },
            "cvm": {
                "endpoint": "cvm.tencentcloudapi.com",
                "version": "2017-03-12",
            },
        }
        self._write_configure(cfg)

    def tearDown(self):
        self._expand_patcher.stop()
        self._home_patcher.stop()
        shutil.rmtree(self.tmp_home, ignore_errors=True)

    # ---- helpers -------------------------------------------------------
    def _configure_path(self):
        return os.path.join(self.cli_path, self.profile + ".configure")

    def _write_configure(self, data):
        with open(self._configure_path(), "w") as f:
            json.dump(data, f)

    def _read_configure(self):
        with open(self._configure_path(), "r") as f:
            return json.load(f)

    # ---- tests ---------------------------------------------------------
    def test_no_cli_no_config_value_is_none(self):
        parsed = _build_parsed_globals(self.profile, request_client=None)
        g = cvm_client.parse_global_arg(parsed)
        self.assertIsNone(g[OptionsDefine.RequestClient.replace("-", "_")])

    def test_value_from_configure_file(self):
        cfg = self._read_configure()
        cfg[OptionsDefine.SysParam][OptionsDefine.RequestClient] = "my-cli-from-conf"
        self._write_configure(cfg)

        parsed = _build_parsed_globals(self.profile, request_client=None)
        g = cvm_client.parse_global_arg(parsed)
        self.assertEqual(
            g[OptionsDefine.RequestClient.replace("-", "_")], "my-cli-from-conf"
        )

    def test_cli_value_overrides_configure_file(self):
        cfg = self._read_configure()
        cfg[OptionsDefine.SysParam][OptionsDefine.RequestClient] = "from-conf"
        self._write_configure(cfg)

        parsed = _build_parsed_globals(self.profile, request_client="from-cli")
        g = cvm_client.parse_global_arg(parsed)
        self.assertEqual(
            g[OptionsDefine.RequestClient.replace("-", "_")], "from-cli"
        )

    def test_cli_value_used_when_no_configure_entry(self):
        parsed = _build_parsed_globals(self.profile, request_client="from-cli-only")
        g = cvm_client.parse_global_arg(parsed)
        self.assertEqual(
            g[OptionsDefine.RequestClient.replace("-", "_")], "from-cli-only"
        )


# ----------------------------------------------------------------------------
# 3. End-to-end: verify the value finally ends up on ClientProfile
# ----------------------------------------------------------------------------
class _FakeCvmModule(object):
    """A drop-in stand-in for ``tencentcloud.cvm.v20170312.cvm_client``."""

    captured_profile = None

    class CvmClient(object):
        def __init__(self, cred, region, profile):
            _FakeCvmModule.captured_profile = profile
            self._sdkVersion = "SDK_PYTHON_FAKE"

        def DescribeRegions(self, model):
            class _Resp(object):
                def to_json_string(self):
                    return json.dumps({"RequestId": "fake"})

            return _Resp()


class TestProfileRequestClientAssembly(unittest.TestCase):
    """Drive a real action through ``doDescribeRegions`` and inspect the
    resulting ``ClientProfile.request_client``."""

    def setUp(self):
        self.tmp_home = tempfile.mkdtemp(prefix="tccli_test_home_")
        self.cli_path = os.path.join(self.tmp_home, ".tccli")
        os.makedirs(self.cli_path)
        self._expand_patcher = mock.patch(
            "os.path.expanduser", lambda p: p.replace("~", self.tmp_home)
        )
        self._expand_patcher.start()

        self.profile = "rc_unittest_e2e"
        cfg = {
            OptionsDefine.SysParam: {
                OptionsDefine.Region: "ap-guangzhou",
                OptionsDefine.Output: "json",
            },
            "cvm": {
                "endpoint": "cvm.tencentcloudapi.com",
                "version": "2017-03-12",
            },
        }
        with open(os.path.join(self.cli_path, self.profile + ".configure"), "w") as f:
            json.dump(cfg, f)

        # Replace the real cvm v20170312 client module so the action does not
        # send any HTTP request.
        _FakeCvmModule.captured_profile = None
        self._client_map_patcher = mock.patch.object(
            cvm_client, "CLIENT_MAP", {"v20170312": _FakeCvmModule}
        )
        self._client_map_patcher.start()

        # Silence FormatOutput stdout noise during the test run.
        self._format_patcher = mock.patch.object(
            cvm_client.FormatOutput, "output", lambda *a, **kw: None
        )
        self._format_patcher.start()

    def tearDown(self):
        self._format_patcher.stop()
        self._client_map_patcher.stop()
        self._expand_patcher.stop()
        shutil.rmtree(self.tmp_home, ignore_errors=True)

    def _run(self, request_client):
        parsed = _build_parsed_globals(self.profile, request_client=request_client)
        cvm_client.doDescribeRegions({}, parsed)
        return _FakeCvmModule.captured_profile

    def test_default_request_client_only_cli_marker(self):
        profile = self._run(None)
        self.assertEqual(profile.request_client, "_CLI_" + __version__)

    def test_request_client_appended_when_provided(self):
        profile = self._run("my-app/v1.2.3")
        self.assertEqual(
            profile.request_client, "_CLI_" + __version__ + "; my-app/v1.2.3"
        )


# ----------------------------------------------------------------------------
# 4. tccli configure set / get / list for request-client
# ----------------------------------------------------------------------------
class TestConfigureCommands(unittest.TestCase):
    def setUp(self):
        self.tmp_home = tempfile.mkdtemp(prefix="tccli_test_home_")
        self.cli_path = os.path.join(self.tmp_home, ".tccli")
        os.makedirs(self.cli_path)
        self._expand_patcher = mock.patch(
            "os.path.expanduser", lambda p: p.replace("~", self.tmp_home)
        )
        self._expand_patcher.start()

        self.profile = "rc_unittest_conf"

    def tearDown(self):
        self._expand_patcher.stop()
        shutil.rmtree(self.tmp_home, ignore_errors=True)

    def _parsed_globals(self):
        ns = mock.Mock()
        ns.profile = self.profile
        return ns

    def test_set_then_get_request_client(self):
        # set
        set_cmd = ConfigureSetCommand()
        set_args = mock.Mock()
        set_args.varname = ["request-client", "my-test-cli"]
        set_cmd._run_main(set_args, self._parsed_globals())

        # validate raw json layout
        conf_path = os.path.join(self.cli_path, self.profile + ".configure")
        self.assertTrue(os.path.exists(conf_path))
        with open(conf_path) as f:
            cfg = json.load(f)
        self.assertEqual(
            cfg[OptionsDefine.SysParam][OptionsDefine.RequestClient], "my-test-cli"
        )

        # get
        stream = six.StringIO()
        get_cmd = ConfigureGetCommand(stream=stream)
        get_args = mock.Mock()
        get_args.varname = ["request-client"]
        get_cmd._run_main(get_args, self._parsed_globals())
        self.assertIn("request-client = my-test-cli", stream.getvalue())

    def test_list_includes_request_client(self):
        # seed configure
        set_cmd = ConfigureSetCommand()
        set_args = mock.Mock()
        set_args.varname = ["request-client", "listed-cli"]
        set_cmd._run_main(set_args, self._parsed_globals())

        stream = six.StringIO()
        list_cmd = ConfigureListCommand(stream=stream)
        list_cmd._run_main(mock.Mock(), self._parsed_globals())
        self.assertIn("request-client = listed-cli", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
