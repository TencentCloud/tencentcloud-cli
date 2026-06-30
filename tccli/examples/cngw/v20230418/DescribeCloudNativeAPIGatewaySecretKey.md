**Example 1: 查询密钥详情**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --SecretKeyId secret-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "8edcd3b9-68fd-42a9-bba3-d38e17ee4777",
        "Result": {
            "BindCount": 0,
            "CreateTime": "2025-11-19 10:39:44",
            "Description": "密钥描述",
            "GenerateType": "System",
            "KmsKeyName": "",
            "KmsKeyVersion": "",
            "ModifyTime": "2025-11-19 16:04:39",
            "Name": "密钥11",
            "ResourceType": "Consumer",
            "SecretKeyId": "secret-xxxx",
            "SecretType": "ApiKey",
            "SecretValue": "sk-****ptz",
            "Status": "Enable"
        }
    }
}
```

