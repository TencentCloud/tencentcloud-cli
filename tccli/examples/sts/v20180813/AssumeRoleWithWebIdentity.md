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
            "Token": "1siMD5r0tPAq9xpR******6a1ad76f09a0069002923def8aFw7tUMd2nH",
            "TmpSecretId": "AKID65zyIP0mp****qt2SlWIQVMn1umNH58",
            "TmpSecretKey": "q95K84wrzuE****y39zg52boxvp71yoh"
        },
        "RequestId": "f6e7cbcb-add1-47bd-9097-d08cf8f3a919"
    }
}
```

