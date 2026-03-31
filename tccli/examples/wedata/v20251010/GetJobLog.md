**Example 1: 获取任务日志**



Input: 

```
tccli wedata GetJobLog --cli-unfold-argument  \
    --JobId 12 \
    --Offset 1 \
    --Limit 10 \
    --WorkspaceId None \
    --SubJobId None
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobLogs": [
                "2025-05-10 10:00:00 [INFO] Job started",
                "2025-05-10 10:00:01 [INFO] Job finished",
                "2025-05-10 10:00:02 [ERROR] Job failed",
                "2025-05-10 10:00:03 [WARN] Job warning",
                "2025-05-10 10:00:04 [DEBUG] Job debug"
            ],
            "JumpInfos": [
                {
                    "JumpTag": "log_detail",
                    "JumpUrl": "https://log-detail.example.com/jobs/12/logs",
                    "Name": "查看完整日志详情"
                }
            ],
            "NextOffset": 6
        },
        "RequestId": "29a6bb0a-7809-43db-8bf5-939cd1c82816"
    }
}
```

