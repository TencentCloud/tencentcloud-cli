**Example 1: 请求示例DEMO**



Input: 

```
tccli mariadb ModifyAccountPrivileges --cli-unfold-argument  \
    --InstanceId tdsql-f35wr6wj \
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

