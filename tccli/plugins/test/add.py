# coding: utf-8
import json
import logging

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models


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
    cli = cvm_client.CvmClient(cred, region)

    req = models.DescribeInstancesRequest()
    try:
        resp = cli.DescribeInstances(req)
        print(resp.to_json_string(indent=2))
    except TencentCloudSDKException as e:
        logging.exception(e)
