**Example 1: 获取MFA临时证书**



Input: 

```
tccli sts GetSessionToken --cli-unfold-argument  \
    --SerialNumber qcs::cam:uin/10001::mfa/softToken \
    --TokenCode 102342
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "da1e***",
            "TmpSecretId": "AKID***",
            "TmpSecretKey": "q95K***"
        },
        "ExpiredTime": 1744271441,
        "Expiration": "2025-04-10T07:50:41Z",
        "RequestId": "4rkgc443-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

