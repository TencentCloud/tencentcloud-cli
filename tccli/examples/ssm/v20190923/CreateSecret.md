**Example 1: 创建新的凭据信息**



Input: 

```
tccli ssm CreateSecret --cli-unfold-argument  \
    --SecretName test_secret \
    --VersionId v1.0 \
    --Description 'test create secret' \
    --SecretString test
```

Output: 
```
{
    "Response": {
        "RequestId": "9debf284-eff9-465a-97b7-163a8b1cccaf",
        "SecretName": "test_secret",
        "VersionId": "v1.0"
    }
}
```

