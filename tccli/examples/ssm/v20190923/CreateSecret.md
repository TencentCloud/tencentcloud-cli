**Example 1: 创建新的凭据信息**

创建自定义凭据。

Input: 

```
tccli ssm CreateSecret --cli-unfold-argument  \
    --VersionId v1.0 \
    --SecretString test \
    --Description test create secret \
    --SecretName test_secret
```

Output: 
```
{
    "Response": {
        "RequestId": "9debf284-eff9-465a-97b7-163a8b1cccaf",
        "SecretName": "test_secret",
        "VersionId": "v1.0",
        "TagCode": 1,
        "TagMsg": "success"
    }
}
```

