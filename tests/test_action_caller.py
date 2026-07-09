# -*- coding: utf-8 -*-
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tccli.action_caller import _nonempty, GenericActionCaller
from tccli.exceptions import NoCredentialsError
import tccli.options_define as options_define
from utils import recover_profile, shell_with_stderr


# ── _nonempty ──────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("value,expected", [
    (None,    False),
    ("",      False),
    ("None",  False),
    ("   ",   False),
    ("AKIDxxx", True),
    ("0",     True),
])
def test_nonempty(value, expected):
    assert _nonempty(value) is expected


# ── _ensure_credential ────────────────────────────────────────────────────────

def _make_g_param(secret_id=None, secret_key=None, language=None, use_cvm_role=False):
    return {
        options_define.SecretId: secret_id,
        options_define.SecretKey: secret_key,
        options_define.Language: language,
        options_define.UseCVMRole.replace('-', '_'): use_cvm_role,
    }


@pytest.mark.parametrize("language,zh_keyword,en_keyword", [
    (None,    "未检测到有效的 secretId/secretKey", None),
    ("zh-CN", "未检测到有效的 secretId/secretKey", None),
    ("en-US", None, "secretId/secretKey not found or empty"),
])
def test_ensure_credential_no_cred_raises(language, zh_keyword, en_keyword):
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(language=language)
    with pytest.raises(NoCredentialsError) as exc_info:
        caller._ensure_credential(g_param)
    msg = str(exc_info.value)
    if zh_keyword:
        assert zh_keyword in msg
    if en_keyword:
        assert en_keyword in msg
    assert "tccli configure" in msg
    assert "TENCENTCLOUD_SECRET_ID" in msg
    assert "--secretId" in msg


@pytest.mark.parametrize("secret_id,secret_key", [
    ("None", "None"),
    ("",     ""),
    ("   ",  "   "),
])
def test_ensure_credential_falsy_aksk_raises(secret_id, secret_key):
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(secret_id=secret_id, secret_key=secret_key)
    with pytest.raises(NoCredentialsError):
        caller._ensure_credential(g_param)


def test_ensure_credential_cvm_role_passthrough():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(use_cvm_role=True)
    caller._ensure_credential(g_param)


def test_ensure_credential_tke_oidc_passthrough(monkeypatch):
    monkeypatch.setenv(options_define.ENV_TKE_ROLE_ARN, "arn:xxx")
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param()
    caller._ensure_credential(g_param)


def test_ensure_credential_valid_aksk_passthrough():
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(secret_id="AKIDxxx", secret_key="SKEYyyy")
    caller._ensure_credential(g_param)


# ── convert_version_str ───────────────────────────────────────────────────────

@pytest.mark.parametrize("ver_input,expected", [
    ("v20170312", "2017-03-12"),
    ("v20230101", "2023-01-01"),
])
def test_convert_version_str(ver_input, expected):
    assert GenericActionCaller.convert_version_str(ver_input) == expected


# ── 集成测试：空凭证场景 ────────────────────────────────────────────────────────

@recover_profile()
def test_empty_credential_outputs_friendly_message():
    """空 AK/SK + 无环境变量 → stderr 含中文引导，退出码 255"""
    cred_path = os.path.expanduser("~/.tccli/default.credential")
    os.makedirs(os.path.dirname(cred_path), exist_ok=True)
    with open(cred_path, "w") as f:
        json.dump({"secretId": "", "secretKey": ""}, f)

    stdout, stderr, rc = shell_with_stderr("tccli cvm DescribeRegions", clean_cred_env=True)
    combined = stdout + stderr
    assert "未检测到有效的 secretId/secretKey" in combined
    assert rc == 255


# ── 回归测试：help / skeleton 不受凭证校验影响 ────────────────────────────────

@pytest.mark.parametrize("cmd", [
    "tccli cvm help",
    "tccli cvm DescribeRegions --generate-cli-skeleton",
])
def test_no_cred_error_in_non_api_commands(cmd):
    stdout, stderr, rc = shell_with_stderr(cmd)
    combined = stdout + stderr
    assert "未检测到有效的 secretId/secretKey" not in combined
    assert "secretId/secretKey not found" not in combined
