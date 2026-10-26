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

**Example 2: 查询密钥详情并返回创建来源信息**

示例仅展示相关字段；实际返回保留原有字段。省略 IncludeCreationInfo 或传 false 时不增加三个创建来源字段。示例 ID 不是实际资源。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewaySecretKey --cli-unfold-argument  \
    --GatewayId gateway-example \
    --SecretKeyId secret-example \
    --IncludeCreationInfo True
```

Output: 
```
{
    "Response": {
        "Result": {
            "SecretKeyId": "secret-example",
            "Name": "auto-team-a1B2",
            "ResourceType": "Consumer",
            "SecretType": "ApiKey",
            "GenerateType": "System",
            "Status": "Enable",
            "SecretValue": "sk-****123",
            "CreateTime": "2026-09-28 16:00:00",
            "ModifyTime": "2026-09-28 16:00:00",
            "CredentialGenerateType": "System",
            "CreationSource": "Batch",
            "BatchId": "keybatch-example"
        },
        "RequestId": "req-example"
    }
}
```

