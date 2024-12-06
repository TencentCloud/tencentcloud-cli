**Example 1: 申请OIDC角色临时访问凭证**

申请OIDC角色临时访问凭证

Input: 

```
tccli sts AssumeRoleWithWebIdentity --cli-unfold-argument  \
    --DurationSeconds 1800 \
    --RoleSessionName test_OIDC \
    --WebIdentityToken eyJraWQiOiJkT**********CNOQ \
    --RoleArn qcs::cam::uin/7989***:roleName/OneLogin-Role \
    --ProviderId OIDC
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "Credentials": {
            "Token": "1siMD***",
            "TmpSecretId": "AKID***",
            "TmpSecretKey": "q95K***"
        },
        "RequestId": "f6e7cbcb-add1-47bd-9097-d08cf8f3a919"
    }
}
```

