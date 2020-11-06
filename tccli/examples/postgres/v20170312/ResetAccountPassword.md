**Example 1: Resetting account password for postgres-lnp6j6172 (failure)**



Input: 

```
tccli postgres ResetAccountPassword --cli-unfold-argument  \
    --DBInstanceId postgres-lnp6j6172 \
    --UserName test \
    --Password 1234qwer()
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

**Example 2: Resetting account password for postgres-lnp6j6172 (success)**



Input: 

```
tccli postgres ResetAccountPassword --cli-unfold-argument  \
    --DBInstanceId postgres-lnp6j6172 \
    --UserName test \
    --Password 1234qwer()
```

Output: 
```
{
    "Response": {
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d"
    }
}
```

