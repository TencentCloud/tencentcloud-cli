**Example 1: 查询日志**



Input: 

```
tccli sqlserver DescribeLogs --cli-unfold-argument  \
    --InstanceId mssql-8lv5ti3v \
    --StartTime 2024-08-14 16:24:24 \
    --EndTime 2026-08-14 16:24:24 \
    --LogType auditLog
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "95e72033-4d5d-49f9-aa24-45adfafa2d09"
    }
}
```

