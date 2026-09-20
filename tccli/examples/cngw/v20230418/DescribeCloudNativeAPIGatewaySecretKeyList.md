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

