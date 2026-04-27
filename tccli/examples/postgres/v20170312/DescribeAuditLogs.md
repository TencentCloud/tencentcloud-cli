**Example 1: 查询日志**

查询日志

Input: 

```
tccli postgres DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId postgres-loe5jryf \
    --StartTime 2026-04-15 22:42:59 \
    --EndTime 2026-04-15 23:42:59 \
    --Limit 1 \
    --Product postgres
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "49ad95cb-26ed-451a-94ea-7b0f06c1817a"
    }
}
```

