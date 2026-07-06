# -*- coding:utf8 -*-
import json
import pytest

from utils import shell, recover_profile


def test_configure_list():
    cmd = 'tccli configure list'
    output = shell(cmd)
    assert "credential:" in output
    assert "configure:" in output
    assert "cvm.version =" in output
    assert "cvm.endpoint =" in output


@recover_profile()
def test_configure_get_set():
    shell("tccli configure set region ap-guangzhou")

    assert "region = ap-guangzhou" in shell("tccli configure get region")


@recover_profile()
def test_configure_output_json():
    shell("tccli configure set output json")

    assert "output = json" in shell("tccli configure get output")

    assert json.loads(shell("tccli cvm DescribeInstances"))


@recover_profile()
def test_configure_output_text():
    shell("tccli configure set output text")

    assert "output = text" in shell("tccli configure get output")

    try:
        json.loads(shell("tccli cvm DescribeInstances"))
        pytest.fail("should be decode error in text output")
    except Exception:
        pass


@recover_profile()
def test_configure_output_table():
    shell("tccli configure set output table")

    assert "output = table" in shell("tccli configure get output")

    try:
        json.loads(shell("tccli cvm DescribeInstances"))
        pytest.fail("should be decode error in table output")
    except Exception:
        pass


@recover_profile()
def test_configure_credential():
    sec_id = "AKIDabcdefghijklmn1234"
    sec_key = "SKabcdefghijklmnopqrst5678"

    shell("tccli configure set secretId %s" % sec_id)
    shell("tccli configure set secretKey %s" % sec_key)

    # configure get 会对敏感字段脱敏输出（末 4 位保留，其余替换为 *）
    output = shell("tccli configure get secretId").strip()
    masked_id = output[len("secretId = "):]
    assert masked_id.endswith(sec_id[-4:])
    assert "*" in masked_id
    assert sec_id not in output

    output = shell("tccli configure get secretKey").strip()
    masked_key = output[len("secretKey = "):]
    assert masked_key.endswith(sec_key[-4:])
    assert "*" in masked_key
    assert sec_key not in output


@recover_profile("user2")
def test_configure_profile():
    shell("tccli configure --profile user2 set region ap-shanghai")

    assert "region = ap-shanghai\n" == shell("tccli configure --profile user2 get region")

    assert "region = ap-shanghai\n" == shell("TCCLI_PROFILE=user2 tccli configure get region")
