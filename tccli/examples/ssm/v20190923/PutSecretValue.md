**Example 1: 增加新版本凭据**



Input: 

```
tccli ssm PutSecretValue --cli-unfold-argument  \
    --SecretName lzctest \
    --VersionId v2.0 \
    --SecretString lzctestv2
```

Output: 
```
{
    "Response": {
        "RequestId": "6764f1f5-8229-4033-a831-46180aee30cf",
        "SecretName": "lzctest",
        "VersionId": "v2.0"
    }
}
```

