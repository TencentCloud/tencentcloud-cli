**Example 1: 申请扮演角色临时访问凭证**

申请扮演角色临时访问凭证

Input: 

```
tccli sts AssumeRole --cli-unfold-argument  \
    --RoleArn qcs::cam::uin/100015158414:roleName/readOnlyRole \
    --RoleSessionName cts
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
        "ExpiredTime": 1543914376,
        "Expiration": "2018-12-04T09:06:16Z",
        "RequestId": "4daec797-9cd2-4f09-9e7a-7d4c43b2a74c"
    }
}
```

