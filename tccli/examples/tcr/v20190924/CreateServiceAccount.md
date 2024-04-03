**Example 1: 创建服务级账号**

创建服务级账号

Input: 

```
tccli tcr CreateServiceAccount --cli-unfold-argument  \
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
        "Name": "tcr$abc",
        "Password": "abc",
        "ExpiresAt": 0,
        "CreateTime": "2020-09-22T00:00:00+00:00",
        "RequestId": "abc"
    }
}
```

**Example 2: 使用Duration创建ServiceAccount**

使用Duration创建ServiceAccount

Input: 

```
tccli tcr CreateServiceAccount --cli-unfold-argument  \
    --RegistryId tcr-45uu7ras \
    --Name test \
    --Description for test \
    --Duration 10 \
    --Permissions.0.Resource test \
    --Permissions.0.Actions tcr:PullRepository tcr:PushRepository tcr:CreateRepository
```

Output: 
```
{
    "Response": {
        "CreateTime": "2023-03-28T15:48:31+08:00",
        "ExpiresAt": 1680853711137,
        "Name": "tcr$test",
        "Password": "oNKUtqrB5Eb68JufkVanSwuhmC4Ergn7",
        "RequestId": "20b67612-28a0-4c51-8efb-0fe14bc23a64"
    }
}
```

