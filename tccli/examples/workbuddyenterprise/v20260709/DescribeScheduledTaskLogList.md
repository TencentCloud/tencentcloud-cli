**Example 1: 查询定时任务执行日志列表**



Input: 

```
tccli workbuddyenterprise DescribeScheduledTaskLogList --cli-unfold-argument  \
    --TaskId 0 \
    --Offset 0 \
    --Limit 0 \
    --WithStats False
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ScheduledTaskLogSet": [
            {
                "LogId": 0,
                "TaskKey": "",
                "TriggerType": "",
                "Status": "",
                "StartTime": "",
                "EndTime": "",
                "DurationMs": 0,
                "DeliveryStatus": "",
                "SessionId": ""
            }
        ],
        "Stats": {
            "TotalCount": 0,
            "SuccessCount": 0,
            "FailedCount": 0,
            "AvgDurationMs": 0
        },
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

