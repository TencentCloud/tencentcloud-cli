**Example 1: 增加新版本凭据**



Input: 

```
tccli ssm PutSecretValue --cli-unfold-argument  \
    --SecretName test \
    --VersionId v2.0 \
    --SecretString 'test v2'
```

Output: 
```
{
    "Response": {
        "RequestId": "6764f1f5-8229-4033-a831-46180aee30cf",
        "SecretName": "test",
        "VersionId": "v2.0"
    }
}
```

