**Example 1: 查询实例配置**



Input: 

```
tccli cdb DescribeAuditConfig --cli-unfold-argument  \
    --InstanceId cdbro-6zpy4ei1
```

Output: 
```
{
    "Response": {
        "RequestId": "507f6863-2827-4c2c-9c3b-fbbcc32e1ed4",
        "CreateTime": "2025-04-11 15:13:07",
        "IsClosing": "false",
        "IsOpening": "false",
        "LogExpireDay": 90,
        "LogType": "storage"
    }
}
```

