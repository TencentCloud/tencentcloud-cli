**Example 1: 更新服务级账号**

更新服务级账号

Input: 

```
tccli tcr ModifyServiceAccount --cli-unfold-argument  \
    --RegistryId abc \
    --Name abc \
    --Description abc \
    --Duration 0 \
    --ExpiresAt 0 \
    --Disable True \
    --Permissions.0.Resource abc \
    --Permissions.0.Actions abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

