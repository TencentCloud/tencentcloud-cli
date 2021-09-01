**Example 1: 查询审计服务配置**



Input: 

```
tccli cdb DescribeAuditConfig --cli-unfold-argument  \
    --InstanceId cdb-txcniupi
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "LogExpireDay": 365,
        "LogType": "storage",
        "IsClosing": "false",
        "CreateTime": "2021-07-13 11:34:35"
    }
}
```

