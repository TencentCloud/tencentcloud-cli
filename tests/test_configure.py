# -*- coding: utf-8 -*-
try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

import argparse

from tccli.configure import ConfigureListCommand
from tccli.utils import Utils


def test_configure_list_masks_secret_id_and_secret_key(tmpdir):
    cli_path = str(tmpdir)
    Utils.dump_json_msg(
        tmpdir.join("default.credential").strpath,
        {
            "secretId": "AKID1234567890SECRETID",
            "secretKey": "SECRETKEY1234567890VALUE",
            "token": "plain-token",
        }
    )
    Utils.dump_json_msg(
        tmpdir.join("default.configure").strpath,
        {
            "_sys_param": {
                "region": "ap-guangzhou",
                "output": "json",
            }
        }
    )

    stream = StringIO()
    command = ConfigureListCommand(stream=stream)
    command.cli_path = cli_path
    command._run_main(None, argparse.Namespace(profile="default"))

    output = stream.getvalue()
    assert "secretId = AKID**************ETID" in output
    assert "secretKey = SECR****************ALUE" in output
    assert "AKID1234567890SECRETID" not in output
    assert "SECRETKEY1234567890VALUE" not in output
    assert "token = plain-token" in output
    assert "region = ap-guangzhou" in output


def test_configure_list_fully_masks_short_secrets():
    assert ConfigureListCommand._mask_sensitive_credential("12345678") == "********"
    assert ConfigureListCommand._mask_sensitive_credential("1234567") == "*******"
