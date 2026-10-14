# -*- coding: utf-8 -*-
import json
import os
import sys

import pytest
import six

try:
    from unittest import mock
except ImportError:
    import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import tccli.options_define as opt
from tccli.action_caller import GenericActionCaller
from tccli.exceptions import ClientError, ConfigurationError, ParamError


@pytest.mark.parametrize("ver_input,expected", [
    ("v20170312", "2017-03-12"),
    ("v20230101", "2023-01-01"),
])
def test_convert_version_str(ver_input, expected):
    assert GenericActionCaller.convert_version_str(ver_input) == expected


def _globals(**overrides):
    parsed = {
        opt.SecretId: "AKIDtest",
        opt.SecretKey: "SKtest",
        opt.Token: None,
        opt.RoleArn.replace("-", "_"): None,
        opt.RoleSessionName.replace("-", "_"): None,
        opt.UseCVMRole.replace("-", "_"): False,
        opt.Region: "ap-guangzhou",
        opt.Endpoint: None,
        opt.Version: None,
        opt.ServiceVersion: None,
        opt.Filter: None,
        opt.Profile: "unit",
        opt.Timeout: None,
        opt.Output: None,
        opt.HttpsProxy.replace("-", "_"): None,
        opt.GenerateCliSkeleton.replace("-", "_"): None,
        opt.CliInputJson.replace("-", "_"): None,
        opt.CliUnfoldArgument.replace("-", "_"): None,
        opt.Waiter: None,
        opt.Language: None,
        opt.RequestClient.replace("-", "_"): None,
    }
    parsed.update(overrides)
    return parsed


def _clear_cred_env(monkeypatch):
    for key in (
        "TCCLI_PROFILE",
        opt.ENV_SECRET_ID, opt.ENV_SECRET_KEY, opt.ENV_TOKEN, opt.ENV_REGION,
        opt.ENV_ROLE_ARN, opt.ENV_ROLE_SESSION_NAME,
        opt.ENV_TKE_REGION, opt.ENV_TKE_PROVIDER_ID,
        opt.ENV_TKE_WEB_IDENTITY_TOKEN_FILE, opt.ENV_TKE_ROLE_ARN,
    ):
        monkeypatch.delenv(key, raising=False)


@pytest.fixture
def cli_home(monkeypatch, tmp_path):
    _clear_cred_env(monkeypatch)
    monkeypatch.setattr("os.path.expanduser", lambda p: p.replace("~", str(tmp_path)))
    home = tmp_path / ".tccli"
    home.mkdir()
    return home


def _as_text(data):
    text = json.dumps(data)
    if not isinstance(text, six.text_type):
        text = text.decode("utf-8")
    return text


def _write(home, profile, conf, cred=None):
    (home / (profile + ".configure")).write_text(_as_text(conf))
    if cred is not None:
        (home / (profile + ".credential")).write_text(_as_text(cred))


def _cvm_conf(extra_sys=None, version="2017-03-12", endpoint="cvm.tencentcloudapi.com"):
    sys_param = {opt.Region: "ap-guangzhou", opt.Output: "json"}
    if extra_sys:
        sys_param.update(extra_sys)
    return {
        opt.SysParam: sys_param,
        "cvm": {opt.Endpoint: endpoint, opt.Version: version},
    }


class _Http(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class _Profile(object):
    def __init__(self, httpProfile=None, signMethod=None):
        self.httpProfile = httpProfile
        self.signMethod = signMethod
        self.request_client = ""
        self.language = None


class _Client(object):
    def __init__(self, service, version, cred, region, profile):
        self.service = service
        self.version = version
        self.cred = cred
        self.region = region
        self.profile = profile
        self._sdkVersion = "SDK"
        self.json_calls = []
        self.octet_calls = []
        self._json_results = [{"Response": {"RequestId": "rid"}}]
        self._octet_result = {"Response": {"RequestId": "octet"}}

    def call_json(self, action, params):
        self.json_calls.append((action, params))
        return self._json_results.pop(0)

    def call_octet_stream(self, action, headers, body):
        self.octet_calls.append((action, headers, body))
        return self._octet_result


@pytest.fixture
def patched_sdk():
    created = []

    def factory(*args, **kwargs):
        client = _Client(*args)
        created.append(client)
        return client

    loader = mock.Mock()
    loader.get_service_model.return_value = {"metadata": {"serviceShortName": "cvm"}}
    with mock.patch("tccli.action_caller.credential.Credential", side_effect=lambda *a, **k: ("aksk", a, k)), \
            mock.patch("tccli.action_caller.credential.CVMRoleCredential", return_value="cvm-cred"), \
            mock.patch("tccli.action_caller.credential.STSAssumeRoleCredential", side_effect=lambda *a, **k: ("sts", a, k)), \
            mock.patch("tccli.action_caller.credential.DefaultTkeOIDCRoleArnProvider") as tke, \
            mock.patch("tccli.action_caller.HttpProfile", _Http), \
            mock.patch("tccli.action_caller.ClientProfile", _Profile), \
            mock.patch("tccli.action_caller.CommonClient", side_effect=factory), \
            mock.patch("tccli.action_caller.Loader", return_value=loader), \
            mock.patch("tccli.action_caller.format_output.output") as output:
        tke.return_value.get_credentials.return_value = "tke-cred"
        yield {"created": created, "loader": loader, "output": output, "tke": tke}


def test_available_versions_lists_and_caches(monkeypatch):
    caller = GenericActionCaller("cvm", "DescribeRegions")
    versions = caller.available_versions()
    assert "v20170312" in versions
    monkeypatch.setattr(os, "listdir", lambda path: (_ for _ in ()).throw(AssertionError("cached")))
    assert caller.available_versions() == versions


def test_available_versions_missing_service():
    with pytest.raises(ConfigurationError):
        GenericActionCaller("no-such-service", "Do").available_versions()


def test_action_traits_match_and_miss():
    caller = GenericActionCaller("CLS", "UploadLog")
    assert caller._get_action_traits({opt.Version: "v20201016"})["request_mode"] == "octet-stream"
    assert caller._get_action_traits({opt.Version: "v20170312"}) is None


def test_filter_by_schema_projects_nested_values():
    objects = {
        "Item": {"members": [{"name": "Id", "type": "string", "member": "string"}]},
    }
    members = [
        {"name": "Name", "type": "string", "member": "string"},
        {"name": "Items", "type": "list", "member": "Item"},
        {"name": "Tags", "type": "list", "member": "string"},
        {"name": "Bad", "type": "list", "member": "Item"},
        {"name": "Child", "type": "object", "member": "Item"},
        {"name": "Missing", "type": "string", "member": "string"},
    ]
    data = {
        "Name": "n",
        "Extra": "drop",
        "Items": [{"Id": "1", "X": 2}],
        "Tags": ["a"],
        "Bad": "not-a-list",
        "Child": {"Id": "c", "Z": 9},
    }
    caller = GenericActionCaller("cvm", "DescribeRegions")
    assert caller._filter_by_schema("plain", members, objects) == "plain"
    assert caller._filter_by_schema(data, members, objects) == {
        "Name": "n",
        "Items": [{"Id": "1"}],
        "Tags": ["a"],
        "Bad": "not-a-list",
        "Child": {"Id": "c"},
    }


def test_filter_response_keeps_data_without_schema_or_on_error():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    loader = mock.Mock()
    loader.get_service_model.return_value = {"objects": {}}
    with mock.patch("tccli.action_caller.Loader", return_value=loader):
        assert caller._filter_response({"RequestId": "r"}, "v20170312") == {"RequestId": "r"}
    with mock.patch("tccli.action_caller.Loader", side_effect=RuntimeError("boom")):
        assert caller._filter_response({"RequestId": "r"}, "v20170312") == {"RequestId": "r"}


def test_filter_response_applies_schema():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    loader = mock.Mock()
    loader.get_service_model.return_value = {
        "objects": {
            "DescribeRegionsResponse": {
                "members": [{"name": "RequestId", "type": "string", "member": "string"}]
            }
        }
    }
    with mock.patch("tccli.action_caller.Loader", return_value=loader):
        assert caller._filter_response(
            {"RequestId": "r", "Extra": 1}, "v20170312") == {"RequestId": "r"}


def test_octet_headers_validation():
    caller = GenericActionCaller("cls", "UploadLog")
    traits = caller._ACTION_TRAITS[("cls", "v20201016", "UploadLog")]
    headers = caller._build_octet_stream_headers(
        {"TopicId": "topic", "HashKey": None, "Other": 1}, traits)
    assert headers == {"X-CLS-TopicId": "topic"}
    with pytest.raises(ParamError):
        caller._build_octet_stream_headers(["bad"], traits)
    with pytest.raises(ParamError):
        caller._build_octet_stream_headers({"TopicId": 1}, traits)
    with pytest.raises(ParamError):
        caller._build_octet_stream_headers({"TopicId": "a\nb"}, traits)


def test_read_binary_stdin_requires_redirect():
    caller = GenericActionCaller("cls", "UploadLog")
    with mock.patch("sys.stdin.isatty", return_value=True):
        with pytest.raises(ParamError):
            caller._read_binary_stdin()
    if not six.PY2:
        with mock.patch("sys.stdin.isatty", return_value=False), \
                mock.patch("sys.stdin.buffer.read", return_value=b"payload"):
            assert caller._read_binary_stdin() == b"payload"
    with mock.patch("tccli.action_caller.six.PY2", True), \
            mock.patch("sys.stdin.isatty", return_value=False), \
            mock.patch("sys.stdin.read", return_value="py2-body"):
        assert caller._read_binary_stdin() == "py2-body"


def test_call_json_without_waiter_outputs_unwrapped_body():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    client = _Client("cvm", "2017-03-12", None, "ap-guangzhou", None)
    client._json_results = ["raw-text"]
    g_param = {opt.Waiter: None, opt.Version: "v20170312", opt.Output: "json", opt.Filter: None}
    with mock.patch.object(caller, "_filter_response", side_effect=lambda data, version: data), \
            mock.patch("tccli.action_caller.format_output.output") as output:
        caller._call_json({}, g_param, client)
    output.assert_called_once_with("action", "raw-text", "json", None)


def test_call_json_waiter_polls_then_succeeds(capsys):
    caller = GenericActionCaller("cvm", "DescribeRegions")
    client = _Client("cvm", "2017-03-12", None, "ap-guangzhou", None)
    client._json_results = [
        {"Response": {"Status": "PENDING"}},
        {"Response": {"Status": "OK"}},
    ]
    g_param = {
        opt.Waiter: '{"expr":"Status","to":"OK"}',
        opt.Version: "v20170312",
        opt.Output: "json",
        opt.Filter: None,
        "OptionsDefine.WaiterInfo": {"expr": "Status", "to": "OK", "timeout": 30, "interval": 1},
    }
    with mock.patch.object(caller, "_filter_response", side_effect=lambda data, version: data), \
            mock.patch("tccli.action_caller.time.sleep") as sleep, \
            mock.patch("tccli.action_caller.format_output.output") as output:
        caller._call_json({}, g_param, client)
    sleep.assert_called_once_with(1)
    output.assert_called_once()
    assert "PENDING" in capsys.readouterr().out


def test_call_json_waiter_timeout():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    client = _Client("cvm", "2017-03-12", None, "ap-guangzhou", None)
    client._json_results = [{"Response": {"Status": "PENDING"}}]
    g_param = {
        opt.Waiter: "{}",
        opt.Version: "v20170312",
        opt.Output: "json",
        opt.Filter: None,
        "OptionsDefine.WaiterInfo": {"expr": "Status", "to": "OK", "timeout": 0, "interval": 0},
    }
    with mock.patch.object(caller, "_filter_response", side_effect=lambda data, version: data):
        with pytest.raises(ClientError):
            caller._call_json({}, g_param, client)


def test_call_octet_stream_rejects_waiter_and_sends_body():
    caller = GenericActionCaller("cls", "UploadLog")
    traits = caller._ACTION_TRAITS[("cls", "v20201016", "UploadLog")]
    client = _Client("cls", "2020-10-16", None, "ap-guangzhou", None)
    with pytest.raises(ParamError):
        caller._call_octet_stream({}, {opt.Waiter: "{}"}, client, traits)
    g_param = {opt.Waiter: None, opt.Version: "v20201016", opt.Output: "json", opt.Filter: None}
    with mock.patch.object(caller, "_read_binary_stdin", return_value=b"bin"), \
            mock.patch.object(caller, "_filter_response", side_effect=lambda data, version: data), \
            mock.patch("tccli.action_caller.format_output.output") as output:
        caller._call_octet_stream({"TopicId": "topic"}, g_param, client, traits)
    assert client.octet_calls[0][1]["X-CLS-TopicId"] == "topic"
    assert client.octet_calls[0][2] == b"bin"
    output.assert_called_once()


def test_create_client_credential_modes(patched_sdk, monkeypatch):
    caller = GenericActionCaller("cvm", "DescribeRegions")
    caller._create_client(_client_param(use_cvm_role=True))
    assert patched_sdk["created"][-1].cred == "cvm-cred"

    caller._create_client(_client_param(role_arn="arn", role_session_name="sess"))
    assert patched_sdk["created"][-1].cred[0] == "sts"

    for key, value in (
        (opt.ENV_TKE_REGION, "ap-guangzhou"),
        (opt.ENV_TKE_PROVIDER_ID, "provider"),
        (opt.ENV_TKE_WEB_IDENTITY_TOKEN_FILE, "/tmp/token"),
        (opt.ENV_TKE_ROLE_ARN, "tke-arn"),
    ):
        monkeypatch.setenv(key, value)
    caller._create_client(_client_param())
    assert patched_sdk["created"][-1].cred == "tke-cred"

    caller._create_client(_client_param(
        timeout="15", request_client="my-app", language="en-US"))
    client = patched_sdk["created"][-1]
    assert client.profile.httpProfile.kwargs["reqTimeout"] == 15
    assert client.profile.request_client.endswith("; my-app")
    assert client.profile.language == "en-US"
    assert client._sdkVersion.endswith("_CLI_") or "_CLI_" in client._sdkVersion

    patched_sdk["loader"].get_service_model.return_value = {"metadata": {}}
    caller._create_client(_client_param())
    assert patched_sdk["created"][-1].service == "cvm"

    with pytest.raises(ParamError):
        caller._create_client(_client_param(request_client="bad\nvalue"))


def _client_param(**overrides):
    param = {
        opt.UseCVMRole.replace("-", "_"): False,
        opt.RoleArn.replace("-", "_"): None,
        opt.RoleSessionName.replace("-", "_"): None,
        opt.SecretId: "id",
        opt.SecretKey: "key",
        opt.Token: "tok",
        opt.Timeout: None,
        opt.Endpoint: "cvm.tencentcloudapi.com",
        opt.HttpsProxy.replace("-", "_"): None,
        opt.RequestClient.replace("-", "_"): None,
        opt.Language: None,
        opt.Version: "v20170312",
        opt.Region: "ap-guangzhou",
        "sts_cred_endpoint": None,
    }
    param.update(overrides)
    return param


def test_call_dispatches_json_and_octet(cli_home, patched_sdk):
    _write(cli_home, "unit", _cvm_conf())
    caller = GenericActionCaller("cvm", "DescribeRegions")
    caller({}, _globals())
    assert patched_sdk["created"][-1].json_calls

    _write(cli_home, "unit", {
        opt.SysParam: {opt.Region: "ap-guangzhou", opt.Output: "json"},
        "cls": {opt.Endpoint: "cls.tencentcloudapi.com", opt.Version: "2020-10-16"},
    })
    octet = GenericActionCaller("cls", "UploadLog")
    stdin_patch = "sys.stdin.read" if six.PY2 else "sys.stdin.buffer.read"
    stdin_body = "body" if six.PY2 else b"body"
    with mock.patch("sys.stdin.isatty", return_value=False), \
            mock.patch(stdin_patch, return_value=stdin_body):
        octet({"TopicId": "topic"}, _globals())
    assert patched_sdk["created"][-1].octet_calls


def test_parse_global_arg_profile_env_and_files(cli_home, monkeypatch):
    _write(cli_home, "from-env", _cvm_conf(extra_sys={opt.RequestClient: "from-conf"}),
           cred={"role-arn": "cred-arn", "role-session-name": "cred-sess", "token": "t"})
    monkeypatch.setenv("TCCLI_PROFILE", "from-env")
    monkeypatch.setenv(opt.ENV_SECRET_ID, "env-id")
    monkeypatch.setenv(opt.ENV_SECRET_KEY, "env-key")
    monkeypatch.setenv(opt.ENV_TOKEN, "env-token")
    monkeypatch.setenv(opt.ENV_REGION, "ap-shanghai")
    monkeypatch.setenv(opt.ENV_ROLE_ARN, "env-arn")
    monkeypatch.setenv(opt.ENV_ROLE_SESSION_NAME, "env-sess")
    parsed = _globals(profile=None, secretId=None, secretKey=None, region=None, output=None)
    g = GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(parsed)
    assert g["profile"] == "from-env"
    assert g[opt.SecretId] == "env-id"
    assert g[opt.Region] == "ap-shanghai"
    assert g[opt.RoleArn.replace("-", "_")] == "env-arn"
    assert g[opt.RequestClient.replace("-", "_")] == "from-conf"
    assert g[opt.Version] == "v20170312"
    assert g[opt.Endpoint] == "cvm.tencentcloudapi.com"


def test_parse_global_arg_cvm_role_and_service_version(cli_home):
    _write(cli_home, "unit", _cvm_conf(), cred={"type": "cvm-role"})
    parsed = _globals(secretId=None, secretKey=None, service_version="2017-03-12", endpoint="preset.example.com")
    g = GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(parsed)
    assert g[opt.UseCVMRole.replace("-", "_")] is True
    assert g[opt.Version] == "v20170312"
    assert g[opt.Endpoint] == "preset.example.com"


def test_parse_global_arg_missing_region_and_broken_service_section(cli_home):
    _write(cli_home, "unit", {opt.SysParam: {opt.Output: "json"}})
    with pytest.raises(ConfigurationError):
        GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(_globals(region=None))

    _write(cli_home, "unit", {opt.SysParam: {opt.Region: "ap-guangzhou", opt.Output: "json"}})
    with pytest.raises(ConfigurationError) as exc:
        GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(_globals())
    assert "config file" in str(exc.value)


def test_parse_global_arg_encodes_unicode_on_py2(cli_home):
    _write(cli_home, "unit", _cvm_conf())
    caller = GenericActionCaller("cvm", "DescribeRegions")
    with mock.patch("tccli.action_caller.six.PY2", True):
        g = caller.parse_global_arg(_globals())
    assert isinstance(g[opt.SecretId], bytes)


def test_parse_global_arg_rejects_bad_config(cli_home):
    _write(cli_home, "unit", [])
    with pytest.raises(ConfigurationError):
        GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(_globals())

    _write(cli_home, "unit", {opt.SysParam: {opt.Region: "ap-guangzhou", opt.Output: "json"}})
    with pytest.raises(ConfigurationError):
        GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(
            _globals(secretId=None, secretKey=None))

    _write(cli_home, "unit", _cvm_conf())
    with pytest.raises(Exception) as exc:
        GenericActionCaller("cvm", "DescribeRegions").parse_global_arg(
            _globals(service_version="1999-01-01"))
    assert "available versions" in str(exc.value)


def test_parse_global_arg_waiter_defaults_and_errors(cli_home):
    _write(cli_home, "unit", _cvm_conf(extra_sys={}))
    conf_path = cli_home / "unit.configure"
    conf = json.loads(conf_path.read_text())
    conf["waiter"] = {"timeout": 9, "interval": 4}
    conf_path.write_text(_as_text(conf))

    caller = GenericActionCaller("cvm", "DescribeRegions")
    g = caller.parse_global_arg(_globals(waiter='{"expr":"Status","to":"OK"}'))
    info = g["OptionsDefine.WaiterInfo"]
    assert info["timeout"] == 9
    assert info["interval"] == 4

    g = caller.parse_global_arg(_globals(waiter='{"expr":"Status","to":"OK","timeout":2,"interval":9}'))
    assert g["OptionsDefine.WaiterInfo"]["interval"] == 2

    _write(cli_home, "unit", _cvm_conf())
    with pytest.raises(Exception):
        caller.parse_global_arg(_globals(waiter="not-json"))
    with pytest.raises(Exception):
        caller.parse_global_arg(_globals(waiter='{"to":"OK"}'))
    with pytest.raises(Exception):
        caller.parse_global_arg(_globals(waiter='{"expr":"Status"}'))

    g = caller.parse_global_arg(_globals(waiter='{"expr":"Status","to":"OK"}'))
    assert g["OptionsDefine.WaiterInfo"]["timeout"] == 180
    assert g["OptionsDefine.WaiterInfo"]["interval"] == 5


def test_plugin_add_command_uses_common_client(capsys):
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
    from tccli.plugins.test.add import add_command

    with mock.patch("tccli.plugins.test.add.credential.Credential") as cred, \
            mock.patch("tccli.plugins.test.add.CommonClient") as client:
        client.return_value.call.return_value = {"TotalCount": 0}
        add_command(
            {"number1": 1, "number2": 2},
            {"secretId": "id", "secretKey": "key", "token": None, "region": None},
        )
        cred.assert_called_once()
        client.return_value.call.assert_called_once_with("DescribeInstances", {"Limit": 10})
        client.return_value.call.side_effect = TencentCloudSDKException("code", "msg")
        add_command(
            {"number1": 1, "number2": 2},
            {"secretId": "id", "secretKey": "key", "token": None, "region": "ap-guangzhou"},
        )
    out = capsys.readouterr().out
    assert "1 + 2 = 3" in out
    assert "TotalCount" in out
