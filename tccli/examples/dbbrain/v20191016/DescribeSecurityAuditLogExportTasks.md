**Example 1: 查询安全审计日志导出任务列表**

查询安全审计日志导出任务列表。

Input: 

```
tccli dbbrain DescribeSecurityAuditLogExportTasks --cli-unfold-argument  \
    --SecAuditGroupId sag-01z37k3f \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Tasks": [
            {
                "Status": "finished",
                "LogStartTime": "2021-01-21 00:00:00",
                "Progress": 100,
                "AsyncRequestId": 1,
                "DangerLevels": [
                    1,
                    2,
                    3
                ],
                "EndTime": "2021-01-22 08:39:22",
                "CreateTime": "2021-01-22 08:39:21",
                "StartTime": "2021-01-22 08:39:22",
                "LogEndTime": "2021-01-21 23:59:59",
                "TotalSize": 1
            }
        ],
        "RequestId": "5fdab910-5c9e-11eb-a610-8717ee1b1000"
    }
}
```

