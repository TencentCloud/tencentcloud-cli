**Example 1: 重置postgres-lnp6j6172的账户密码，失败**



Input: 

```
tccli postgres ResetAccountPassword --cli-unfold-argument  \
    --UserName test \
    --Password 1234qwer() \
    --DBInstanceId postgres-lnp6j6172
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "Error": {
            "Message": "admin unmatch|oss return failed, code:3, message:admin unmatch",
            "Code": "FailedOperation.OssOperationFailed"
        }
    }
}
```

**Example 2: 重置postgres-lnp6j6172的账户密码，成功**



Input: 

```
tccli postgres ResetAccountPassword --cli-unfold-argument  \
    --UserName test \
    --Password 1234qwer() \
    --DBInstanceId postgres-lnp6j6172
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

