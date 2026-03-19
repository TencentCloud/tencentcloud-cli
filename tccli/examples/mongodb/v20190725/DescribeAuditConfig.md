**Example 1: 查询审计服务配置**



Input: 

```
tccli mongodb DescribeAuditConfig --cli-unfold-argument  \
    --InstanceId cmgo-bfyv0sy7
```

Output: 
```
{
    "Response": {
        "AuditAll": true,
        "CreateTime": "2025-12-11 11:47:20",
        "InstanceId": "cmgo-bfyv****",
        "InstanceName": "cmgo-bfyv****",
        "IsClosing": "false",
        "IsOpening": "false",
        "LogExpireDay": 7,
        "LogType": "storage",
        "RequestId": "d94bc81b-3b76-4104-9270-0582d8227ebc"
    }
}
```

