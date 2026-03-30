**Example 1: 查询access类型凭证详情**



Input: 

```
tccli csip DescribeKeySandboxCredential --cli-unfold-argument  \
    --CredentialId cred-abc12345
```

Output: 
```
{
    "Response": {
        "CredentialId": "cred-abc12345",
        "CredentialName": "腾讯云-生产环境密钥",
        "CredentialType": "access",
        "CredentialEffectScope": {
            "Exclude": 1,
            "Instances": []
        },
        "Access": [
            {
                "Key": "SecretId",
                "Value": "AKI***abcd"
            },
            {
                "Key": "SecretKey",
                "Value": "abc***wxyz"
            }
        ],
        "CreateTime": "2026-01-15T08:30:00Z",
        "UpdateTime": "2026-03-10T14:29:03Z",
        "RequestId": "c368eae2-8739-4cc2-b4f8-8f4284a93b41"
    }
}
```

**Example 2: 查询sts类型凭证详情**



Input: 

```
tccli csip DescribeKeySandboxCredential --cli-unfold-argument  \
    --CredentialId cred-sts56789
```

Output: 
```
{
    "Response": {
        "CredentialId": "cred-sts56789",
        "CredentialName": "STS临时密钥-测试环境",
        "CredentialType": "sts",
        "CredentialEffectScope": {
            "Exclude": 1,
            "Instances": [
                "ins-abc12345",
                "ins-def67890"
            ]
        },
        "STS": {
            "System": "tencentCam",
            "SecretID": "AKI***efgh",
            "SecretKey": "abc***wxyz"
        },
        "CreateTime": "2026-02-20T10:00:00Z",
        "UpdateTime": "2026-03-09T10:15:00Z",
        "RequestId": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
    }
}
```

