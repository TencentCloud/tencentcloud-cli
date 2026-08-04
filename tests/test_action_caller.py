# -*- coding: utf-8 -*-
import io
import os
import sys

import pytest

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tccli import action_caller
from tccli import options_define
from tccli.action_caller import GenericActionCaller
from tccli.command import ServiceCommand
from tccli.exceptions import ParamError


class BinaryStdin(object):
    def __init__(self, data, is_tty=False):
        self.buffer = io.BytesIO(data)
        self._is_tty = is_tty

    def isatty(self):
        return self._is_tty


def action_globals(version="v20201016", waiter=None):
    return {
        options_define.Version: version,
        options_define.Waiter: waiter,
        options_define.Output: "json",
        options_define.Filter: None,
    }


def client_globals(version="v20201016"):
    params = action_globals(version)
    params.update({
        options_define.UseCVMRole.replace('-', '_'): False,
        options_define.RoleArn.replace('-', '_'): None,
        options_define.RoleSessionName.replace('-', '_'): None,
        options_define.SecretId: "secret-id",
        options_define.SecretKey: "secret-key",
        options_define.Token: None,
        options_define.Timeout: None,
        options_define.Endpoint: "cls.tencentcloudapi.com",
        options_define.HttpsProxy.replace('-', '_'): None,
        options_define.Language: None,
        options_define.RequestClient.replace('-', '_'): None,
        options_define.Region: "ap-guangzhou",
        "sts_cred_endpoint": None,
    })
    return params


# ── convert_version_str ───────────────────────────────────────────────────────

@pytest.mark.parametrize("ver_input,expected", [
    ("v20170312", "2017-03-12"),
    ("v20230101", "2023-01-01"),
])
def test_convert_version_str(ver_input, expected):
    assert GenericActionCaller.convert_version_str(ver_input) == expected


def test_service_command_prefers_plugin_then_uses_generic_action_caller():
    plugin_caller = Mock()
    service_command = object.__new__(ServiceCommand)
    service_command._service_name = "cvm"
    service_command._version = "v20170312"
    service_command._get_service_model = Mock(return_value={
        "actions": {
            "PluginAction": {"action_caller": plugin_caller},
            "DescribeInstances": {},
        },
    })

    command_map = service_command._build_command_map()

    assert command_map["PluginAction"]._action_caller is plugin_caller
    caller = command_map["DescribeInstances"]._action_caller
    assert isinstance(caller, GenericActionCaller)
    assert caller._module == "cvm"
    assert caller._action == "DescribeInstances"


# ── Generic JSON request ──────────────────────────────────────────────────────

def test_generic_action_uses_tc3_profile(monkeypatch):
    caller = GenericActionCaller("cls", "DescribeTopics")
    params = client_globals()
    client = Mock()
    client._sdkVersion = "SDK"
    http_profile = Mock()

    monkeypatch.setattr(action_caller.os, "getenv", lambda name: None)
    with patch("tccli.action_caller.credential.Credential") as credential_mock, \
            patch("tccli.action_caller.HttpProfile", return_value=http_profile), \
            patch("tccli.action_caller.ClientProfile") as profile_mock, \
            patch("tccli.action_caller.Loader") as loader_mock, \
            patch("tccli.action_caller.CommonClient", return_value=client) as common_client_mock:
        loader_mock.return_value.get_service_model.return_value = {
            "metadata": {"serviceShortName": "cls"},
        }
        caller._create_client(params)

    credential_mock.assert_called_once_with("secret-id", "secret-key", None)
    profile_mock.assert_called_once_with(httpProfile=http_profile, signMethod="TC3-HMAC-SHA256")
    common_client_mock.assert_called_once_with(
        "cls", "2020-10-16", credential_mock.return_value, "ap-guangzhou", profile_mock.return_value
    )


def test_generic_action_uses_service_short_name_for_signing(monkeypatch):
    caller = GenericActionCaller("autoscaling", "DescribeScalingPolicies")
    params = client_globals(version="v20180419")
    params[options_define.Endpoint] = "as.tencentcloudapi.com"
    client = Mock()
    client._sdkVersion = "SDK"

    monkeypatch.setattr(action_caller.os, "getenv", lambda name: None)
    with patch("tccli.action_caller.Loader") as loader_mock, \
            patch("tccli.action_caller.CommonClient", return_value=client) as common_client_mock:
        loader_mock.return_value.get_service_model.return_value = {
            "metadata": {"serviceShortName": "as"},
        }
        caller._create_client(params)

    loader_mock.return_value.get_service_model.assert_called_once_with("autoscaling", "2018-04-19")
    assert common_client_mock.call_args[0][0] == "as"


def test_generic_action_calls_json(monkeypatch):
    caller = GenericActionCaller("cvm", "DescribeInstances")
    client = Mock()
    client.call_json.return_value = {"Response": {"RequestId": "request-id"}}
    caller.parse_global_arg = Mock(return_value=action_globals())
    caller._create_client = Mock(return_value=client)
    caller._filter_response = Mock(side_effect=lambda data, version: data)

    with patch("tccli.action_caller.format_output.output") as output_mock:
        caller({"Limit": 1}, {})

    client.call_json.assert_called_once_with("DescribeInstances", {"Limit": 1})
    assert client.call_octet_stream.call_count == 0
    output_mock.assert_called_once_with("action", {"RequestId": "request-id"}, "json", None)


# ── CLS UploadLog octet-stream request ─────────────────────────────────────────

def test_upload_log_reads_stdin_and_calls_octet_stream(monkeypatch):
    caller = GenericActionCaller("cls", "UploadLog")
    client = Mock()
    caller.parse_global_arg = Mock(return_value=action_globals())
    caller._create_client = Mock(return_value=client)
    caller._filter_response = Mock(side_effect=lambda data, version: data)
    client.call_octet_stream.return_value = {"Response": {"RequestId": "request-id"}}
    monkeypatch.setattr(action_caller.sys, "stdin", BinaryStdin(b"protobuf-data"))

    with patch("tccli.action_caller.format_output.output") as output_mock:
        caller({"TopicId": "topic-id", "CompressType": "lz4"}, {})

    client.call_octet_stream.assert_called_once_with(
        "UploadLog",
        {"X-CLS-TopicId": "topic-id", "X-CLS-CompressType": "lz4"},
        b"protobuf-data"
    )
    assert client.call_json.call_count == 0
    output_mock.assert_called_once_with("action", {"RequestId": "request-id"}, "json", None)


@pytest.mark.parametrize("args", [
    {"TopicId": "topic\r\ninjected"},
    {"TopicId": 1},
])
def test_upload_log_rejects_unsafe_headers(args):
    caller = GenericActionCaller("cls", "UploadLog")
    client = Mock()
    caller.parse_global_arg = Mock(return_value=action_globals())
    caller._create_client = Mock(return_value=client)

    with pytest.raises(ParamError):
        caller(args, {})

    assert client.call_octet_stream.call_count == 0


def test_upload_log_rejects_tty_input(monkeypatch):
    caller = GenericActionCaller("cls", "UploadLog")
    client = Mock()
    caller.parse_global_arg = Mock(return_value=action_globals())
    caller._create_client = Mock(return_value=client)
    monkeypatch.setattr(action_caller.sys, "stdin", BinaryStdin(b"", is_tty=True))

    with pytest.raises(ParamError):
        caller({"TopicId": "topic-id"}, {})

    assert client.call_octet_stream.call_count == 0


def test_upload_log_rejects_waiter_without_submitting():
    caller = GenericActionCaller("cls", "UploadLog")
    client = Mock()
    caller.parse_global_arg = Mock(return_value=action_globals(waiter="{}"))
    caller._create_client = Mock(return_value=client)

    with pytest.raises(ParamError):
        caller({"TopicId": "topic-id"}, {})

    assert client.call_octet_stream.call_count == 0
