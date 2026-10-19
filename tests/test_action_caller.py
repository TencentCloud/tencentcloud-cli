# -*- coding: utf-8 -*-
import json
import os

import pytest
import six

try:
    from unittest import mock
except ImportError:
    import mock

import tccli.action_caller as action_caller
import tccli.options_define as options_define
from tccli.action_caller import get_skip_sign_action_caller
from tccli.action_caller import GenericActionCaller
from tccli.exceptions import ClientError, ConfigurationError, ParamError


def _build_globals(profile="default"):
    return {
        options_define.SecretId: None,
        options_define.SecretKey: None,
        options_define.Token: None,
        options_define.RoleArn.replace("-", "_"): None,
        options_define.RoleSessionName.replace("-", "_"): None,
        options_define.UseCVMRole.replace("-", "_"): False,
        options_define.Profile: profile,
        options_define.Region: "ap-guangzhou",
        options_define.Endpoint: None,
        options_define.Output: "json",
        options_define.Filter: None,
        options_define.Language: None,
        options_define.Timeout: None,
        options_define.HttpsProxy.replace("-", "_"): None,
        options_define.RequestClient.replace("-", "_"): None,
        options_define.Waiter: None,
        options_define.Version: None,
        options_define.ServiceVersion: "2018-08-13",
    }


def _action_model(action, skip_sign=True):
    return {
        "input": action + "Request",
        "output": action + "Response",
        "name": action,
        "skip_sign": skip_sign,
    }


_ISOLATED_ENV = (
    "TCCLI_PROFILE",
    options_define.ENV_SECRET_ID,
    options_define.ENV_SECRET_KEY,
    options_define.ENV_TOKEN,
    options_define.ENV_ROLE_ARN,
    options_define.ENV_ROLE_SESSION_NAME,
    options_define.ENV_REGION,
    options_define.ENV_TKE_REGION,
    options_define.ENV_TKE_PROVIDER_ID,
    options_define.ENV_TKE_WEB_IDENTITY_TOKEN_FILE,
    options_define.ENV_TKE_ROLE_ARN,
)


@pytest.fixture(autouse=True)
def _isolate_credential_env(monkeypatch):
    for name in _ISOLATED_ENV:
        monkeypatch.delenv(name, raising=False)


def _configure(region="ap-shanghai", output="json", language="en-US",
               request_client="profile-client", endpoint="sts.test.tencentcloudapi.com",
               version="2018-08-13", module="sts"):
    sys_param = {}
    if region is not None:
        sys_param["region"] = region
    if output is not None:
        sys_param["output"] = output
    if language is not None:
        sys_param["language"] = language
    if request_client is not None:
        sys_param["request-client"] = request_client
    return {
        options_define.SysParam: sys_param,
        module: {
            "endpoint": endpoint,
            "version": version,
        },
    }


def _write_profile(tmpdir, profile, configure, credential=None):
    tccli_dir = tmpdir.join(".tccli")
    if not tccli_dir.check():
        tccli_dir = tmpdir.mkdir(".tccli")
    if not isinstance(configure, six.string_types):
        configure = json.dumps(configure)
    tccli_dir.join(profile + ".configure").write(configure)
    if credential is not None:
        if not isinstance(credential, six.string_types):
            credential = json.dumps(credential)
        tccli_dir.join(profile + ".credential").write(credential)


def _parse(caller, g_param, tmpdir):
    with mock.patch.object(os.path, "expanduser", return_value=str(tmpdir)):
        return caller.parse_global_arg(g_param)


def test_skip_sign_true_creates_action_caller():
    action = "AssumeRoleWithSAML"
    caller = get_skip_sign_action_caller(
        "sts", "2018-08-13", action, _action_model(action))
    assert isinstance(caller, GenericActionCaller)
    assert caller.skip_credential_refresh is True


@pytest.mark.parametrize("action_model", [
    {"skip_sign": False},
    {},
])
def test_skip_sign_false_or_missing_uses_original_caller(action_model):
    assert get_skip_sign_action_caller(
        "sts", "2018-08-13", "GetCallerIdentity", action_model) is None


@pytest.mark.parametrize("skip_sign", ["true", 1, None, [], {}])
def test_skip_sign_rejects_non_boolean_values(skip_sign):
    with pytest.raises(ConfigurationError):
        get_skip_sign_action_caller(
            "sts", "2018-08-13", "AssumeRoleWithSAML",
            {"skip_sign": skip_sign})


def test_skip_sign_rejects_non_object_action_model():
    with pytest.raises(ConfigurationError):
        get_skip_sign_action_caller(
            "sts", "2018-08-13", "AssumeRoleWithSAML", [])


def test_create_client_uses_no_credential_and_preserves_profile_options():
    captured = {}

    class FakeCommonClient(object):
        def __init__(self, service, version, credential, region, profile):
            captured.update({
                "service": service,
                "version": version,
                "credential": credential,
                "region": region,
                "profile": profile,
            })
            self._sdkVersion = "SDK"

    g_param = _build_globals()
    g_param[options_define.Endpoint] = "sts.test.tencentcloudapi.com"
    g_param[options_define.Version] = "v20180813"
    g_param[options_define.Timeout] = "12"
    g_param[options_define.HttpsProxy.replace("-", "_")] = "http://proxy.example"
    g_param[options_define.Language] = "zh-CN"
    g_param[options_define.RequestClient.replace("-", "_")] = "unit-test"

    caller = GenericActionCaller(
        "sts", "AssumeRoleWithSAML", skip_sign=True)
    with mock.patch.object(action_caller, "CommonClient", FakeCommonClient):
        client = caller._create_client(g_param)

    assert captured["service"] == "sts"
    assert captured["version"] == "2018-08-13"
    assert captured["credential"] is None
    assert captured["region"] == "ap-guangzhou"
    assert captured["profile"].httpProfile.endpoint == "sts.test.tencentcloudapi.com"
    assert captured["profile"].httpProfile.reqTimeout == 12
    assert captured["profile"].httpProfile.proxy == "http://proxy.example"
    assert captured["profile"].language == "zh-CN"
    assert captured["profile"].request_client.endswith("; unit-test")
    assert client is not None


def test_call_json_passes_skip_sign_filters_response_and_outputs():
    class FakeClient(object):
        def __init__(self):
            self.calls = []

        def call_json(self, action, args, options=None):
            self.calls.append((action, args, options))
            return {
                "Response": {
                    "Credentials": {
                        "Token": "token",
                        "TmpSecretId": "id",
                        "TmpSecretKey": "key",
                        "InternalCredentialField": "drop",
                    },
                    "ExpiredTime": 1,
                    "Expiration": "time",
                    "RequestId": "request-id",
                    "InternalTopLevelField": "drop",
                }
            }

    client = FakeClient()
    caller = GenericActionCaller(
        "sts", "AssumeRoleWithWebIdentity", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Version] = "v20180813"
    output = []

    with mock.patch.object(action_caller.format_output, "output",
                           side_effect=lambda *args: output.append(args)):
        caller._call_json({"WebIdentityToken": "oidc-token"}, g_param, client)

    assert client.calls == [(
        "AssumeRoleWithWebIdentity",
        {"WebIdentityToken": "oidc-token"},
        {"SkipSign": True},
    )]
    assert output[0][0] == "action"
    assert output[0][1] == {
        "Credentials": {
            "Token": "token",
            "TmpSecretId": "id",
            "TmpSecretKey": "key",
        },
        "ExpiredTime": 1,
        "Expiration": "time",
        "RequestId": "request-id",
    }


def test_filter_response_returns_original_when_response_model_missing():
    caller = GenericActionCaller(
        "sts", "AssumeRoleWithSAML", skip_sign=True)
    data = {"InternalField": "value"}
    with mock.patch.object(action_caller.Loader, "get_service_model",
                           return_value={"objects": {}}):
        assert caller._filter_response(data, "v20180813") == data


def test_parse_global_arg_ignores_credential_file(tmpdir):
    tccli_dir = tmpdir.mkdir(".tccli")
    configure = {
        options_define.SysParam: {
            "region": "ap-shanghai",
            "output": "json",
            "language": "en-US",
            "request-client": "profile-client",
        },
        "sts": {
            "endpoint": "sts.test.tencentcloudapi.com",
            "version": "2018-08-13",
        },
    }
    tccli_dir.join("default.configure").write(json.dumps(configure))
    tccli_dir.join("default.credential").write("not valid json")

    caller = GenericActionCaller(
        "sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals(profile="default")
    g_param[options_define.Region] = None
    g_param[options_define.Output] = None

    with mock.patch.object(os.path, "expanduser", return_value=str(tmpdir)):
        parsed = caller.parse_global_arg(g_param)

    assert parsed[options_define.Region] == "ap-shanghai"
    assert parsed[options_define.Output] == "json"
    assert parsed[options_define.Endpoint] == "sts.test.tencentcloudapi.com"
    assert parsed[options_define.RequestClient.replace("-", "_")] == "profile-client"


def test_parse_global_arg_builds_waiter_defaults(tmpdir):
    tccli_dir = tmpdir.mkdir(".tccli")
    configure = {
        options_define.SysParam: {
            "region": "ap-guangzhou",
            "output": "json",
        },
        "sts": {
            "endpoint": "sts.test.tencentcloudapi.com",
            "version": "2018-08-13",
        },
    }
    tccli_dir.join("default.configure").write(json.dumps(configure))

    caller = GenericActionCaller(
        "sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals(profile="default")
    g_param[options_define.Waiter] = \
        '{"expr":"Status","to":"READY"}'

    with mock.patch.object(os.path, "expanduser", return_value=str(tmpdir)):
        parsed = caller.parse_global_arg(g_param)

    assert parsed["OptionsDefine.WaiterInfo"] == {
        "expr": "Status",
        "to": "READY",
        "timeout": 180,
        "interval": 5,
    }

    with mock.patch.object(os.path, "expanduser", return_value=str(tmpdir)):
        for waiter in ("not-json", '{"to":"READY"}', '{"expr":"Status"}'):
            invalid = _build_globals(profile="default")
            invalid[options_define.Waiter] = waiter
            with pytest.raises(Exception):
                caller.parse_global_arg(invalid)


@pytest.mark.parametrize("version,expected", [
    ("v20180813", "2018-08-13"),
    ("v20201016", "2020-10-16"),
])
def test_convert_version_str(version, expected):
    assert GenericActionCaller.convert_version_str(version) == expected


def test_available_versions_lists_caches_and_rejects_unknown_service():
    caller = GenericActionCaller("sts", "GetCallerIdentity")
    versions = caller.available_versions()
    assert "v20180813" in versions

    with mock.patch.object(os, "listdir",
                           side_effect=AssertionError("versions were not cached")):
        assert caller.available_versions() == versions

    with pytest.raises(ConfigurationError):
        GenericActionCaller(
            "service-that-does-not-exist", "Action").available_versions()


def test_call_dispatches_json_and_octet_stream_requests():
    json_caller = GenericActionCaller("sts", "GetCallerIdentity")
    json_globals = {options_define.Version: "v20180813"}
    json_client = object()
    with mock.patch.object(json_caller, "parse_global_arg",
                           return_value=json_globals), \
            mock.patch.object(json_caller, "_create_client",
                              return_value=json_client), \
            mock.patch.object(json_caller, "_call_json") as call_json:
        json_caller({"Limit": 1}, {})
    call_json.assert_called_once_with({"Limit": 1}, json_globals, json_client)

    octet_caller = GenericActionCaller("CLS", "UploadLog")
    octet_globals = {options_define.Version: "v20201016"}
    octet_client = object()
    with mock.patch.object(octet_caller, "parse_global_arg",
                           return_value=octet_globals), \
            mock.patch.object(octet_caller, "_create_client",
                              return_value=octet_client), \
            mock.patch.object(octet_caller, "_call_octet_stream") as call_octet:
        octet_caller({"TopicId": "topic"}, {})
    traits = octet_caller._ACTION_TRAITS[
        ("cls", "v20201016", "UploadLog")]
    call_octet.assert_called_once_with(
        {"TopicId": "topic"}, octet_globals, octet_client, traits)


def test_octet_stream_header_validation():
    traits = GenericActionCaller._ACTION_TRAITS[
        ("cls", "v20201016", "UploadLog")]
    assert GenericActionCaller._build_octet_stream_headers({
        "TopicId": "topic",
        "HashKey": None,
        "CompressType": "gzip",
        "Ignored": "value",
    }, traits) == {
        "X-CLS-TopicId": "topic",
        "X-CLS-CompressType": "gzip",
    }

    with pytest.raises(ParamError):
        GenericActionCaller._build_octet_stream_headers([], traits)
    with pytest.raises(ParamError):
        GenericActionCaller._build_octet_stream_headers(
            {"TopicId": 123}, traits)
    with pytest.raises(ParamError):
        GenericActionCaller._build_octet_stream_headers(
            {"TopicId": "topic\r\ninjected"}, traits)


def test_read_binary_stdin_handles_redirects_and_tty():
    tty_stdin = mock.Mock()
    tty_stdin.isatty.return_value = True
    with mock.patch.object(action_caller.sys, "stdin", tty_stdin):
        with pytest.raises(ParamError):
            GenericActionCaller._read_binary_stdin()

    if not six.PY2:
        redirected_stdin = mock.Mock()
        redirected_stdin.isatty.return_value = False
        redirected_stdin.buffer.read.return_value = b"payload"
        with mock.patch.object(
                action_caller.sys, "stdin", redirected_stdin):
            assert GenericActionCaller._read_binary_stdin() == b"payload"

    py2_stdin = mock.Mock()
    py2_stdin.isatty.return_value = False
    py2_stdin.read.return_value = "py2-payload"
    with mock.patch.object(action_caller.six, "PY2", True), \
            mock.patch.object(action_caller.sys, "stdin", py2_stdin):
        assert GenericActionCaller._read_binary_stdin() == "py2-payload"


class _FakeJsonClient(object):
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def call_json(self, action, args, options=None):
        self.calls.append((action, args, options))
        return self.responses.pop(0)


def _waiter_globals(timeout=10, interval=0):
    return {
        options_define.Waiter: "{}",
        options_define.Version: "v20180813",
        options_define.Output: "json",
        options_define.Filter: None,
        "OptionsDefine.WaiterInfo": {
            "expr": "Status",
            "to": "READY",
            "timeout": timeout,
            "interval": interval,
        },
    }


def test_call_json_waits_until_target_state(capsys):
    caller = GenericActionCaller("sts", "GetCallerIdentity")
    client = _FakeJsonClient([
        {"Response": {"Status": "PENDING"}},
        {"Response": {"Status": "READY"}},
    ])

    with mock.patch.object(caller, "_filter_response",
                           side_effect=lambda data, version: data), \
            mock.patch.object(action_caller.time, "sleep") as sleep, \
            mock.patch.object(action_caller.format_output, "output") as output:
        caller._call_json({}, _waiter_globals(), client)

    assert len(client.calls) == 2
    assert "Inquiry result is PENDING." in capsys.readouterr().out
    sleep.assert_called_once_with(0)
    output.assert_called_once_with(
        "action", {"Status": "READY"}, "json", None)


def test_call_json_waiter_timeout():
    caller = GenericActionCaller("sts", "GetCallerIdentity")
    client = _FakeJsonClient([{"Response": {"Status": "PENDING"}}])

    with mock.patch.object(caller, "_filter_response",
                           side_effect=lambda data, version: data), \
            mock.patch.object(action_caller.time, "time",
                              side_effect=[1, 2]):
        with pytest.raises(ClientError):
            caller._call_json({}, _waiter_globals(timeout=0), client)


class _FakeOctetClient(object):
    def __init__(self):
        self.calls = []

    def call_octet_stream(self, action, headers, body):
        self.calls.append((action, headers, body))
        return {"Response": {"RequestId": "request-id"}}


def test_call_octet_stream_rejects_waiter_and_sends_input():
    caller = GenericActionCaller("cls", "UploadLog")
    traits = caller._ACTION_TRAITS[("cls", "v20201016", "UploadLog")]
    client = _FakeOctetClient()

    with pytest.raises(ParamError):
        caller._call_octet_stream(
            {}, {options_define.Waiter: "{}"}, client, traits)

    g_param = {
        options_define.Waiter: None,
        options_define.Version: "v20201016",
        options_define.Output: "json",
        options_define.Filter: None,
    }
    with mock.patch.object(caller, "_read_binary_stdin",
                           return_value=b"binary-log"), \
            mock.patch.object(caller, "_filter_response",
                              side_effect=lambda data, version: data), \
            mock.patch.object(action_caller.format_output, "output") as output:
        caller._call_octet_stream(
            {"TopicId": "topic"}, g_param, client, traits)

    assert client.calls == [(
        "UploadLog",
        {"X-CLS-TopicId": "topic"},
        b"binary-log",
    )]
    output.assert_called_once_with(
        "action", {"RequestId": "request-id"}, "json", None)


def test_filter_response_projects_nested_schema_and_handles_loader_error():
    caller = GenericActionCaller("test", "DescribeItems")
    objects = {
        "DescribeItemsResponse": {
            "members": [
                {"name": "Items", "type": "list", "member": "Item"},
                {"name": "Tags", "type": "list", "member": "string"},
                {"name": "Child", "type": "object", "member": "Item"},
                {"name": "BadItems", "type": "list", "member": "Item"},
                {"name": "Missing", "type": "string", "member": "string"},
            ],
        },
        "Item": {
            "members": [
                {"name": "Id", "type": "string", "member": "string"},
            ],
        },
    }
    data = {
        "Items": [{"Id": "1", "Internal": "drop"}],
        "Tags": ["tag"],
        "Child": {"Id": "2", "Internal": "drop"},
        "BadItems": "not-a-list",
        "Internal": "drop",
    }
    with mock.patch.object(
            action_caller.Loader, "get_service_model",
            return_value={"objects": objects}):
        assert caller._filter_response(data, "v20200101") == {
            "Items": [{"Id": "1"}],
            "Tags": ["tag"],
            "Child": {"Id": "2"},
            "BadItems": "not-a-list",
        }

    assert caller._filter_by_schema("not-a-dict", [], {}) == "not-a-dict"
    with mock.patch.object(
            action_caller.Loader, "get_service_model",
            side_effect=RuntimeError("broken model")):
        assert caller._filter_response(data, "v20200101") == data


def _signed_client_globals(**overrides):
    g_param = _build_globals()
    g_param.update({
        options_define.SecretId: "secret-id",
        options_define.SecretKey: "secret-key",
        options_define.Token: "token",
        options_define.Endpoint: "sts.test.tencentcloudapi.com",
        options_define.Version: "v20180813",
        "sts_cred_endpoint": "sts.internal.test",
    })
    g_param.update(overrides)
    return g_param


def test_create_client_supports_signed_credential_modes(monkeypatch):
    credentials = []
    for key in (
            options_define.ENV_TKE_REGION,
            options_define.ENV_TKE_PROVIDER_ID,
            options_define.ENV_TKE_WEB_IDENTITY_TOKEN_FILE,
            options_define.ENV_TKE_ROLE_ARN):
        monkeypatch.delenv(key, raising=False)

    class FakeCommonClient(object):
        def __init__(self, service, version, cred, region, profile):
            credentials.append(cred)
            self._sdkVersion = "SDK"

    caller = GenericActionCaller("sts", "GetCallerIdentity")
    with mock.patch.object(action_caller, "CommonClient", FakeCommonClient), \
            mock.patch.object(action_caller.credential, "Credential",
                              return_value="normal-credential"), \
            mock.patch.object(action_caller.credential, "CVMRoleCredential",
                              return_value="cvm-credential"), \
            mock.patch.object(
                action_caller.credential, "STSAssumeRoleCredential",
                return_value="sts-credential"), \
            mock.patch.object(
                action_caller.credential,
                "DefaultTkeOIDCRoleArnProvider") as tke_provider:
        tke_provider.return_value.get_credentials.return_value = \
            "tke-credential"

        caller._create_client(_signed_client_globals())
        caller._create_client(_signed_client_globals(
            use_cvm_role=True))
        caller._create_client(_signed_client_globals(
            role_arn="role-arn", role_session_name="session"))

        for key, value in (
                (options_define.ENV_TKE_REGION, "ap-guangzhou"),
                (options_define.ENV_TKE_PROVIDER_ID, "provider"),
                (options_define.ENV_TKE_WEB_IDENTITY_TOKEN_FILE, "/tmp/token"),
                (options_define.ENV_TKE_ROLE_ARN, "role-arn")):
            monkeypatch.setenv(key, value)
        caller._create_client(_signed_client_globals())

    assert credentials == [
        "normal-credential",
        "cvm-credential",
        "sts-credential",
        "tke-credential",
    ]


def test_create_client_rejects_multiline_request_client():
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=True)
    with pytest.raises(ParamError):
        caller._create_client(_signed_client_globals(
            request_client="bad\nrequest-client"))
    with pytest.raises(ParamError):
        caller._create_client(_signed_client_globals(
            request_client="bad\rrequest-client"))


def test_parse_global_arg_reads_version_and_credentials_from_files(tmpdir):
    _write_profile(
        tmpdir,
        "default",
        _configure(version="2018-08-13", endpoint="from-file.example"),
        {
            "secretId": "sid",
            "secretKey": "skey",
            "token": "tok",
            "role-arn": "arn",
            "role-session-name": "sess",
        },
    )
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals()
    g_param[options_define.ServiceVersion] = None
    g_param[options_define.Endpoint] = None
    g_param[options_define.Region] = None
    g_param[options_define.Output] = None
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.Version] == "v20180813"
    assert parsed[options_define.Endpoint] == "from-file.example"
    assert parsed["sts_cred_endpoint"] == "from-file.example"
    assert parsed[options_define.SecretId] == "sid"
    assert parsed[options_define.SecretKey] == "skey"
    assert parsed[options_define.Token] == "tok"
    assert parsed["role_arn"] == "arn"
    assert parsed["role_session_name"] == "sess"
    assert parsed[options_define.Region] == "ap-shanghai"
    assert parsed[options_define.UseCVMRole.replace("-", "_")] is False


def test_parse_global_arg_enables_cvm_role_without_secrets(tmpdir):
    _write_profile(tmpdir, "default", _configure(), {"type": "cvm-role"})
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals()
    g_param[options_define.Endpoint] = "keep.example"
    g_param[options_define.Region] = "ap-guangzhou"
    g_param[options_define.Output] = "json"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.UseCVMRole.replace("-", "_")] is True
    assert parsed[options_define.SecretId] is None
    assert parsed[options_define.SecretKey] is None
    assert parsed[options_define.Token] is None
    assert parsed[options_define.Endpoint] == "keep.example"


def test_parse_global_arg_explicit_secret_skips_cvm_role(tmpdir):
    _write_profile(tmpdir, "default", _configure(), {
        "type": "cvm-role",
        "secretKey": "file-key",
        "token": "file-token",
    })
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals()
    g_param[options_define.SecretId] = "explicit-id"
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.UseCVMRole.replace("-", "_")] is False
    assert parsed[options_define.SecretId] == "explicit-id"
    assert parsed[options_define.SecretKey] == "file-key"
    assert parsed[options_define.Token] == "file-token"


def test_parse_global_arg_rejects_missing_secret(tmpdir):
    _write_profile(tmpdir, "default", _configure())
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    with pytest.raises(ConfigurationError, match="is invalid"):
        _parse(caller, _build_globals(), tmpdir)


def test_parse_global_arg_tke_env_allows_missing_secret(tmpdir, monkeypatch):
    monkeypatch.setenv(options_define.ENV_TKE_ROLE_ARN, "arn:tke")
    _write_profile(tmpdir, "default", _configure(), {})
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals()
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.SecretId] is None
    assert parsed[options_define.UseCVMRole.replace("-", "_")] is False


def test_parse_global_arg_applies_env_when_profile_omitted(tmpdir, monkeypatch):
    monkeypatch.setenv("TCCLI_PROFILE", "fromenv")
    monkeypatch.setenv(options_define.ENV_SECRET_ID, "env-id")
    monkeypatch.setenv(options_define.ENV_SECRET_KEY, "env-key")
    monkeypatch.setenv(options_define.ENV_TOKEN, "env-token")
    monkeypatch.setenv(options_define.ENV_REGION, "ap-beijing")
    monkeypatch.setenv(options_define.ENV_ROLE_ARN, "env-arn")
    monkeypatch.setenv(options_define.ENV_ROLE_SESSION_NAME, "env-sess")
    _write_profile(tmpdir, "fromenv", _configure(region="ap-shanghai"), {
        "secretId": "file-id",
        "secretKey": "file-key",
        "token": "file-token",
        "type": "cvm-role",
    })
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals(profile="")
    g_param[options_define.Region] = None
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["profile"] == "fromenv"
    assert parsed[options_define.SecretId] == "env-id"
    assert parsed[options_define.SecretKey] == "env-key"
    assert parsed[options_define.Token] == "env-token"
    assert parsed["role_arn"] == "env-arn"
    assert parsed["role_session_name"] == "env-sess"
    assert parsed[options_define.Region] == "ap-beijing"
    assert parsed[options_define.UseCVMRole.replace("-", "_")] is False


def test_parse_global_arg_blank_profile_uses_file_secrets(tmpdir, monkeypatch):
    monkeypatch.setenv(options_define.ENV_REGION, "na-toronto")
    _write_profile(tmpdir, "default", _configure(region="ap-shanghai"), {
        "secretId": "sid",
        "secretKey": "skey",
        "token": "tok",
        "role-arn": "arn",
    })
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals(profile=None)
    g_param[options_define.Region] = None
    g_param[options_define.Endpoint] = None
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["profile"] == "default"
    assert parsed[options_define.Region] == "na-toronto"
    assert parsed[options_define.SecretId] == "sid"
    assert parsed[options_define.Endpoint] == "sts.test.tencentcloudapi.com"
    assert parsed["role_arn"] == "arn"
    assert parsed["role_session_name"] is None


def test_parse_global_arg_skip_sign_ignores_env_credentials(tmpdir, monkeypatch):
    monkeypatch.setenv("TCCLI_PROFILE", "custom")
    monkeypatch.setenv(options_define.ENV_SECRET_ID, "env-id")
    monkeypatch.setenv(options_define.ENV_SECRET_KEY, "env-key")
    monkeypatch.setenv(options_define.ENV_ROLE_ARN, "env-arn")
    monkeypatch.setenv(options_define.ENV_ROLE_SESSION_NAME, "env-sess")
    _write_profile(tmpdir, "custom", _configure(region="ap-shanghai"))
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals(profile="")
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["profile"] == "custom"
    assert parsed[options_define.SecretId] is None
    assert parsed[options_define.SecretKey] is None
    assert parsed["role_arn"] is None
    assert parsed[options_define.Region] == "ap-guangzhou"


def test_parse_global_arg_allows_missing_sts_endpoint(tmpdir):
    _write_profile(tmpdir, "default", {
        options_define.SysParam: {
            "region": "ap-guangzhou",
            "output": "json",
        },
    }, {
        "secretId": "sid",
        "secretKey": "skey",
        "token": "tok",
    })
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    g_param = _build_globals()
    g_param[options_define.Endpoint] = "keep.example"
    g_param[options_define.Region] = "ap-guangzhou"
    g_param[options_define.Output] = "json"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["sts_cred_endpoint"] is None
    assert parsed[options_define.Endpoint] == "keep.example"
    assert parsed[options_define.SecretId] == "sid"


def test_parse_global_arg_works_without_configure_file(tmpdir):
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Region] = "ap-guangzhou"
    g_param[options_define.Output] = "json"
    g_param[options_define.Language] = "en-US"
    g_param[options_define.RequestClient.replace("-", "_")] = "cli"
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.Version] == "v20180813"
    assert parsed[options_define.Endpoint] == "keep.example"


def test_parse_global_arg_rejects_missing_region(tmpdir):
    _write_profile(tmpdir, "default", _configure(region=None))
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Region] = None
    g_param[options_define.Output] = "json"
    g_param[options_define.Language] = "en-US"
    g_param[options_define.Endpoint] = "keep.example"
    with pytest.raises(ConfigurationError, match="region is invalid"):
        _parse(caller, g_param, tmpdir)


def test_parse_global_arg_rejects_broken_config(tmpdir):
    _write_profile(tmpdir, "default", {
        options_define.SysParam: {
            "region": "ap-guangzhou",
            "output": "json",
        },
    })
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.ServiceVersion] = None
    g_param[options_define.Region] = "ap-guangzhou"
    g_param[options_define.Output] = "json"
    g_param[options_define.Language] = "en-US"
    g_param[options_define.Endpoint] = "keep.example"
    with pytest.raises(ConfigurationError, match="config file"):
        _parse(caller, g_param, tmpdir)


def test_parse_global_arg_rejects_unknown_version(tmpdir):
    _write_profile(tmpdir, "default", _configure())
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.ServiceVersion] = "1999-01-01"
    g_param[options_define.Endpoint] = "keep.example"
    with pytest.raises(Exception, match="available versions"):
        _parse(caller, g_param, tmpdir)


@pytest.mark.parametrize("configure, credential", [
    ("[]", "{}"),
    ("{}", "[]"),
])
def test_parse_global_arg_rejects_non_object_files(tmpdir, configure, credential):
    _write_profile(tmpdir, "default", configure, credential)
    caller = GenericActionCaller("sts", "GetCallerIdentity", skip_sign=False)
    with pytest.raises(ConfigurationError, match="not json format"):
        _parse(caller, _build_globals(), tmpdir)


def test_parse_global_arg_waiter_uses_config_defaults(tmpdir):
    conf = _configure()
    conf["waiter"] = {"timeout": 20, "interval": 3}
    _write_profile(tmpdir, "default", conf)
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Waiter] = '{"expr":"Status","to":"READY"}'
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["OptionsDefine.WaiterInfo"]["timeout"] == 20
    assert parsed["OptionsDefine.WaiterInfo"]["interval"] == 3


def test_parse_global_arg_waiter_keeps_explicit_timing(tmpdir):
    conf = _configure()
    conf["waiter"] = {"timeout": 99, "interval": 8}
    _write_profile(tmpdir, "default", conf)
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Waiter] = \
        '{"expr":"Status","to":"READY","timeout":2,"interval":9}'
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["OptionsDefine.WaiterInfo"]["timeout"] == 2
    assert parsed["OptionsDefine.WaiterInfo"]["interval"] == 2


def test_parse_global_arg_waiter_fills_partial_config(tmpdir):
    conf = _configure()
    conf["waiter"] = {"interval": 8}
    _write_profile(tmpdir, "default", conf)
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Waiter] = '{"expr":"Status","to":"READY","timeout":4}'
    g_param[options_define.Endpoint] = "keep.example"
    parsed = _parse(caller, g_param, tmpdir)

    assert parsed["OptionsDefine.WaiterInfo"]["timeout"] == 4
    assert parsed["OptionsDefine.WaiterInfo"]["interval"] == 4


def test_parse_global_arg_encodes_text_when_py2(tmpdir):
    _write_profile(tmpdir, "default", _configure())
    caller = GenericActionCaller("sts", "AssumeRoleWithSAML", skip_sign=True)
    g_param = _build_globals()
    g_param[options_define.Region] = u"ap-guangzhou"
    g_param[options_define.Endpoint] = u"keep.example"
    g_param[options_define.Output] = "json"
    with mock.patch.object(action_caller.six, "PY2", True):
        parsed = _parse(caller, g_param, tmpdir)

    assert parsed[options_define.Region] == b"ap-guangzhou"
    assert parsed[options_define.UseCVMRole.replace("-", "_")] is False
