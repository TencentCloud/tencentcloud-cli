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
    sec_id = "xxx"
    sec_key = "yyy"

    shell("tccli configure set secretId %s" % sec_id)
    shell("tccli configure set secretKey %s" % sec_key)

    output = shell("tccli configure get secretId").strip()
    sec_id2 = output[len("secretId = "):]

    output = shell("tccli configure get secretKey").strip()
    sec_key2 = output[len("secretKey = "):]

    assert sec_id == sec_id2
    assert sec_key == sec_key2


@recover_profile("user2")
def test_configure_profile():
    shell("tccli configure --profile user2 set region ap-shanghai")

    assert "region = ap-shanghai\n" == shell("tccli configure --profile user2 get region")

    assert "region = ap-shanghai\n" == shell("TCCLI_PROFILE=user2 tccli configure get region")
