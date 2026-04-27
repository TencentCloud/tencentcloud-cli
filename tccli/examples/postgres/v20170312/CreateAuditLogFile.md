**Example 1: 创建审计日志文件**

创建审计日志文件

Input: 

```
tccli postgres CreateAuditLogFile --cli-unfold-argument  \
    --InstanceId postgres-nqg1hcnj \
    --StartTime 2026-03-25 00:00:00 \
    --EndTime 2026-03-25 01:00:00 \
    --Product postgres
```

Output: 
```
{
    "Response": {
        "RequestId": "56707f2b-f311-4448-97bf-8c6323072aef"
    }
}
```

