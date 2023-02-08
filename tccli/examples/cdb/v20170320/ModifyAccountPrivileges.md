**Example 1: 修改云数据库实例账号的权限**



Input: 

```
tccli cdb ModifyAccountPrivileges --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --Accounts.0.Host 127.0.0.1 \
    --Accounts.0.User ajnnw \
    --GlobalPrivileges SELECT
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "256117ed-efa08b54-61784d44-91781bbd"
    }
}
```

