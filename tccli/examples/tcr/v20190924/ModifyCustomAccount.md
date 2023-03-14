**Example 1: 更新自定义账户**

更新自定义账户

Input: 

```
tccli tcr ModifyCustomAccount --cli-unfold-argument  \
    --RegistryId tcr-12345 \
    --Name robot \
    --Description desc \
    --ExpiresAt 1676897989 \
    --Disable False \
    --Permissions.0.Resource library \
    --Permissions.0.Actions tcr:PushRepository tcr:PullRepository
```

Output: 
```
{
    "Response": {
        "RequestId": "reqId"
    }
}
```

