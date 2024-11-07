**Example 1: 获取指定凭据下的版本列表信息**



Input: 

```
tccli ssm ListSecretVersionIds --cli-unfold-argument  \
    --SecretName test3-secret
```

Output: 
```
{
    "Response": {
        "RequestId": "9877a5cc-208d-4ec0-b4bb-4e62990de2aa",
        "SecretName": "test3-secret",
        "Versions": [
            {
                "CreateTime": 1730278717,
                "VersionId": "v1"
            },
            {
                "CreateTime": 1730278706,
                "VersionId": "v2"
            },
            {
                "CreateTime": 1730271414,
                "VersionId": "v3"
            }
        ]
    }
}
```

