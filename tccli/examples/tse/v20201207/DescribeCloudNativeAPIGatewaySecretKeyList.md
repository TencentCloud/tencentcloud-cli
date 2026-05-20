**Example 1: 查询密钥列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewaySecretKeyList --cli-unfold-argument  \
    --GatewayId gateway-c7fb18e4 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b9b49623-c235-4839-b1d6-1f6f23ae8dcd",
        "Result": {
            "SecretKeys": [
                {
                    "BindCount": 0,
                    "CreateTime": "2025-11-19 12:35:50",
                    "Description": "密钥",
                    "GenerateType": "System",
                    "KmsKeyName": "",
                    "KmsKeyVersion": "",
                    "ModifyTime": "2025-11-19 12:35:50",
                    "Name": "测试系统密钥",
                    "ResourceType": "Consumer",
                    "SecretKeyId": "secret-wefawwe",
                    "SecretType": "ApiKey",
                    "SecretValue": "sk-****wdk",
                    "Status": "Enable"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

