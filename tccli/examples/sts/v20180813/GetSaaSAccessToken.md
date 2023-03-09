**Example 1: SaaS应用登录token换临时证书**



Input: 

```
tccli sts GetSaaSAccessToken --cli-unfold-argument  \
    --SaaSToken Didfer*** \
    --Platform coding \
    --TokenUin 30000129 \
    --TokenOwnerUin 3000023 \
    --ClientIP 1.1.1.1 \
    --ClientUA chrome \
    --DurationSeconds 7200
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1594985702,
        "Expiration": "2020-07-17T11:35:02Z",
        "Credentials": {
            "Token": "v0YuJBgp8F***",
            "TmpSecretId": "AKIDjtBloQ***",
            "TmpSecretKey": "4Y7Sb3***"
        },
        "RequestId": "8623dd94-01f6-43f2-91ec-2b5fd27b20f1"
    }
}
```

