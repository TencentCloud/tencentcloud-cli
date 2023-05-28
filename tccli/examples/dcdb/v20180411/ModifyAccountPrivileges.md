**Example 1: 修改云数据库实例账号的权限信息**

修改云数据库实例账号的权限信息

Input: 

```
tccli dcdb ModifyAccountPrivileges --cli-unfold-argument  \
    --InstanceId tdsqlshard-f35wr6wj \
    --Accounts.0.User ajnnw \
    --GlobalPrivileges SELECT \
    --Accounts.0.Host 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "FlowId": 145623
    }
}
```

