**Example 1: 查询拨测任务列表**

查询应用下未删除的拨测任务。

Input: 

```
tccli rum DescribeTDEMDialTasks --cli-unfold-argument  \
    --AppId 5
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "7",
                "TaskName": "android-after-dns",
                "Status": "active",
                "Type": "icmp",
                "ExecutionTime": "after_dns_slow",
                "WatchDomain": "postman-echo.com",
                "DialDomain": "ldns",
                "TimeoutMs": 3000,
                "PeriodMs": 200,
                "PackageCount": 3,
                "PackageSize": 64,
                "NeedMTR": 0,
                "SlowThresholdMs": 1,
                "CreatedBy": "700001860566",
                "CreatedAt": "2026-09-30 15:37:46",
                "UpdatedAt": "2026-09-30 15:59:37"
            }
        ],
        "RequestId": "bfb4b198-c80e-4564-b18e-1e1c59b4882a"
    }
}
```

