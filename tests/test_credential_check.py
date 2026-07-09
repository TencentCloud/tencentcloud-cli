# -*- coding:utf-8 -*-
import json
import os
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tccli.action_caller import _nonempty, GenericActionCaller
from tccli.exceptions import NoCredentialsError
import tccli.options_define as options_define
from utils import recover_profile


# ─────────────────────────────────────────────
# 任务7：单元测试 _nonempty
# ─────────────────────────────────────────────

def test_nonempty_none():
    assert _nonempty(None) is False


def test_nonempty_empty_string():
    assert _nonempty("") is False


def test_nonempty_string_none():
    assert _nonempty("None") is False


def test_nonempty_whitespace():
    assert _nonempty("   ") is False


def test_nonempty_valid_akid():
    assert _nonempty("AKIDxxx") is True


# ─────────────────────────────────────────────
# 任务8：单元测试 _ensure_credential
# ─────────────────────────────────────────────

def _make_g_param(secret_id=None, secret_key=None, language=None,
                  use_cvm_role=False):
    """构造最小化的 g_param 字典用于单元测试"""
    return {
        options_define.SecretId: secret_id,
        options_define.SecretKey: secret_key,
        options_define.Language: language,
        options_define.UseCVMRole.replace('-', '_'): use_cvm_role,
    }


def test_ensure_credential_no_cred_zh():
    """无凭证 + 默认语言 → 抛 NoCredentialsError，含中文引导与三种方式"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param()
    with pytest.raises(NoCredentialsError) as exc_info:
        caller._ensure_credential(g_param)
    msg = str(exc_info.value)
    assert "未检测到有效的 secretId/secretKey" in msg
    assert "tccli configure" in msg
    assert "TENCENTCLOUD_SECRET_ID" in msg
    assert "--secretId" in msg


def test_ensure_credential_no_cred_zh_cn():
    """无凭证 + zh-CN → 抛 NoCredentialsError，含中文引导"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(language="zh-CN")
    with pytest.raises(NoCredentialsError) as exc_info:
        caller._ensure_credential(g_param)
    assert "未检测到有效的 secretId/secretKey" in str(exc_info.value)


def test_ensure_credential_no_cred_en():
    """无凭证 + en-US → 抛 NoCredentialsError，含英文引导"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(language="en-US")
    with pytest.raises(NoCredentialsError) as exc_info:
        caller._ensure_credential(g_param)
    msg = str(exc_info.value)
    assert "secretId/secretKey not found or empty" in msg
    assert "tccli configure" in msg
    assert "TENCENTCLOUD_SECRET_ID" in msg
    assert "--secretId" in msg


def test_ensure_credential_cvm_role_passthrough():
    """cvm-role 模式 → 不抛错"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(use_cvm_role=True)
    caller._ensure_credential(g_param)  # 不应抛出异常


def test_ensure_credential_tke_oidc_passthrough(monkeypatch):
    """TKE OIDC 环境变量存在 → 不抛错"""
    monkeypatch.setenv(options_define.ENV_TKE_ROLE_ARN, "arn:xxx")
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param()
    caller._ensure_credential(g_param)  # 不应抛出异常


def test_ensure_credential_valid_aksk_passthrough():
    """有效 AK/SK → 不抛错"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(secret_id="AKIDxxx", secret_key="SKEYyyy")
    caller._ensure_credential(g_param)  # 不应抛出异常


def test_ensure_credential_string_none_aksk():
    """AK/SK 值为字符串 'None' → 判空 → 抛错"""
    caller = GenericActionCaller("cvm", "DescribeRegions")
    g_param = _make_g_param(secret_id="None", secret_key="None")
    with pytest.raises(NoCredentialsError):
        caller._ensure_credential(g_param)


# ─────────────────────────────────────────────
# 任务9：集成测试（空凭证场景）
# ─────────────────────────────────────────────

def _find_tccli():
    """查找可用的 tccli 可执行文件路径"""
    candidates = [
        os.path.expanduser("~/.pyenv/versions/3.8.18/bin/tccli"),
        "/usr/local/bin/tccli",
        "/usr/bin/tccli",
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return "tccli"


_TCCLI = _find_tccli()

_TCCLI_REPO = os.path.join(os.path.dirname(__file__), '..')
_TCCLI_RUNNER = (
    "/usr/bin/python3 -c \""
    "import sys; sys.path.insert(0, '{repo}'); "
    "from tccli.main import main; sys.exit(main())"
    "\"".format(repo=os.path.abspath(_TCCLI_REPO))
)


def _shell_with_stderr(cmd):
    """执行命令，返回 (stdout, stderr, returncode)"""
    cmd = cmd.replace("tccli ", _TCCLI_RUNNER + " ", 1)
    env = os.environ.copy()
    env.pop("TENCENTCLOUD_SECRET_ID", None)
    env.pop("TENCENTCLOUD_SECRET_KEY", None)
    env.pop("TENCENTCLOUD_SECRET_TOKEN", None)
    p = subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=env
    )
    stdout, stderr = p.communicate()
    if sys.version_info.major >= 3:
        return stdout.decode("utf-8"), stderr.decode("utf-8"), p.returncode
    return stdout, stderr, p.returncode


@recover_profile()
def test_empty_credential_integration():
    """清空 profile 且无环境变量 → 输出含中文引导，退出码 255，不含超长 usage"""
    cred_path = os.path.expanduser("~/.tccli/default.credential")
    os.makedirs(os.path.dirname(cred_path), exist_ok=True)
    with open(cred_path, "w") as f:
        json.dump({"secretId": "", "secretKey": ""}, f)

    stdout, stderr, rc = _shell_with_stderr("tccli cvm DescribeRegions")
    combined = stdout + stderr
    assert "未检测到有效的 secretId/secretKey" in combined
    assert rc == 255
    assert "usage:" not in combined.lower() or len(combined) < 2000


# ─────────────────────────────────────────────
# 任务10：回归测试
# ─────────────────────────────────────────────

def test_cvm_help_not_affected():
    """tccli cvm help 不受凭证校验影响"""
    stdout, stderr, rc = _shell_with_stderr("tccli cvm help")
    combined = stdout + stderr
    assert "未检测到有效的 secretId/secretKey" not in combined
    assert "secretId/secretKey not found" not in combined


def test_generate_cli_skeleton_not_affected():
    """--generate-cli-skeleton 不受凭证校验影响"""
    stdout, stderr, rc = _shell_with_stderr(
        "tccli cvm DescribeRegions --generate-cli-skeleton"
    )
    combined = stdout + stderr
    assert "未检测到有效的 secretId/secretKey" not in combined
    assert "secretId/secretKey not found" not in combined
