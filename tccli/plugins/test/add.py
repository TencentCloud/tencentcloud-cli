# coding: utf-8
import json
import logging

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.common_client import CommonClient


def add_command(args, parsed_globals):
    # get arguments from args
    number1 = args["number1"]
    number2 = args["number2"]
    print("%d + %d = %d\n" % (number1, number2, number1 + number2))

    # get secret key from parsed_globals
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"

    # do api call with secret key
    cred = credential.Credential(secret_id, secret_key, token)
    cli = CommonClient("cvm", "2017-03-12", cred, region)

    try:
        resp = cli.call("DescribeInstances", {"Limit": 10})
        print(json.dumps(resp))
    except TencentCloudSDKException as e:
        logging.exception(e)
