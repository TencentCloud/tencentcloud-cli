# -*- coding: utf-8 -*-
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def list_object(args, parsed_globals):
    secret_id = parsed_globals["secretId"]
    secret_key = parsed_globals["secretKey"]
    token = parsed_globals["token"]
    region = parsed_globals["region"] or "ap-guangzhou"
    endpoint = parsed_globals["endpoint"]

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Endpoint=endpoint)
    client = CosS3Client(config)

    response = client.list_objects(Bucket=args["bucket"])
    if 'Contents' in response:
        for content in response['Contents']:
            print(content['Key'])
