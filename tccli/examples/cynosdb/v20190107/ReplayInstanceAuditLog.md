**Example 1: 回放实例审计日志**

回放实例审计日志

Input: 

```
tccli cynosdb ReplayInstanceAuditLog --cli-unfold-argument  \
    --StartTime 2025-06-26 14:00:00 \
    --EndTime 2025-06-26 16:00:00 \
    --SourceClusterId cynosdbmysql-8j1jtwkv \
    --SourceInstanceId cynosdbmysql-ins-2fbftt98 \
    --TargetClusterId cynosdbmysql-kwoft68f \
    --TargetInstanceId cynosdbmysql-ins-431w3zh0 \
    --TargetUserName root \
    --TargetPassword Calebzhao123.
```

Output: 
```
{
    "Response": {
        "RequestId": "y7rtl807j00d80oid44s34c100ros3iy",
        "TaskId": 678
    }
}
```

