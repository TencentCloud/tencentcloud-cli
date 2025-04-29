**Example 1: 创建 Cos 临时密钥示例**



Input: 

```
tccli gs CreateCosCredential --cli-unfold-argument  \
    --CosType Mobile
```

Output: 
```
{
    "Response": {
        "SecretID": "secret-id",
        "SecretKey": "secret-key",
        "SessionToken": "session-token",
        "CosBucket": "bucket-name",
        "CosRegion": "cos-region",
        "Path": "/test/",
        "StartTime": 1500000,
        "ExpiredTime": 1500000,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

