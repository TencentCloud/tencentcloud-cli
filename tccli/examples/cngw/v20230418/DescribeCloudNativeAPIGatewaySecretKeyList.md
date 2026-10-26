**Example 1: 查询密钥列表**



Input: 

```
tccli cngw DescribeCloudNativeAPIGatewaySecretKeyList --cli-unfold-argument  \
    --GatewayId gateway-657ece23 \
    --Limit 20 \
    --Offset 0 \
    --ResourceType Consumer
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 8,
            "SecretKeys": [
                {
                    "Name": "yoyo",
                    "SecretKeyId": "secret-24de766980fe83",
                    "SecretValue": "yoy****est",
                    "Status": "Enable",
                    "SecretType": "ApiKey",
                    "ResourceType": "Consumer",
                    "SourceType": "Private",
                    "SyncedVersion": "v0",
                    "GenerateType": "Custom",
                    "Description": "",
                    "KmsKeyName": "",
                    "KmsKeyVersion": "",
                    "Provider": "",
                    "BindCount": 0,
                    "CreateTime": "2026-09-09 14:24:32",
                    "ModifyTime": "2026-09-09 14:24:32"
                }
            ]
        },
        "RequestId": "e16cd828-c7f0-4201-9630-8b3efa03c3f2"
    }
}
```

**Example 2: 查询批量密钥并返回创建来源信息**

示例仅展示相关字段；实际返回保留原有字段。省略 IncludeCreationInfo 或传 false 时不增加三个创建来源字段。示例 ID 不是实际资源。

Input: 

```
tccli cngw DescribeCloudNativeAPIGatewaySecretKeyList --cli-unfold-argument  \
    --GatewayId gateway-example \
    --ResourceType Consumer \
    --IncludeCreationInfo True \
    --Filters.0.Name CreationSource \
    --Filters.0.Values Batch \
    --Filters.1.Name CredentialGenerateType \
    --Filters.1.Values System \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "SecretKeys": [
                {
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
                }
            ]
        },
        "RequestId": "req-example"
    }
}
```

