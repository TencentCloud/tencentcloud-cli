**Example 1: 获取凭据明文信息**

获取凭据明文信息

Input: 

```
tccli ssm GetSecretValue --cli-unfold-argument  \
    --SecretName test3-secret \
    --VersionId v3
```

Output: 
```
{
    "Response": {
        "RequestId": "91cec765-5604-4287-89b1-634357cfcd29",
        "SecretBinary": "5Yet5o2udmFsdWUyCg==",
        "SecretName": "test3-secret",
        "SecretString": "凭据value3",
        "VersionId": "v3"
    }
}
```

