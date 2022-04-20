**Example 1: 验证用户账号权限**



Input: 

```
tccli dbbrain VerifyUserAccount --cli-unfold-argument  \
    --InstanceId cdb-test \
    --User root \
    --Password t123456
```

Output: 
```
{
    "Response": {
        "SessionToken": "QCth1234567890",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

