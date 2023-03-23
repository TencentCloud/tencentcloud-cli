**Example 1: 获取凭据明文信息**

获取凭据明文信息

Input: 

```
tccli ssm GetSecretValue --cli-unfold-argument  \
    --VersionId v1.0 \
    --SecretName test_secret
```

Output: 
```
{
    "Response": {
        "RequestId": "b8e6b67f-3ca7-4341-b4fa-a372bdf4e11c",
        "SecretName": "test_secret",
        "VersionId": "v1.0",
        "SecretBinary": "",
        "SecretString": "test"
    }
}
```

