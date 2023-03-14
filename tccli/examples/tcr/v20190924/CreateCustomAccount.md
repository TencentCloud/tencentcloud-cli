**Example 1: 创建自定义账户**

创建自定义账户

Input: 

```
tccli tcr CreateCustomAccount --cli-unfold-argument  \
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
        "Name": "tcr$robot",
        "Password": "kiHUaTAmF6a94mNzhZWDans3dYahHQNE",
        "ExpiresAt": 1676897989,
        "CreateTime": "2023-02-20T21:00:00+00:00",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

