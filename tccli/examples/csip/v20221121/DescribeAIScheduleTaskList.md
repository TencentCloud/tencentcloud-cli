**Example 1: 定时任务执行记录**



Input: 

```
tccli csip DescribeAIScheduleTaskList --cli-unfold-argument  \
    --ScheduleId sched-a1b2c3d4 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "CreateTime": 1775719256484,
                "EndTime": 1775719286484,
                "Result": "今日数据报告已生成，销售额环比增长12%",
                "ScheduleId": "sched-mock-001",
                "ScheduledTime": 1775719256484,
                "SessionId": "session-mock-001",
                "StartTime": 1775719256984,
                "Status": 3,
                "TaskId": "task-mock-001",
                "TriggerId": "trigger-mock-001",
                "UpdateTime": 1775719286484
            }
        ],
        "TotalCount": 2,
        "RequestId": "90a726f6-de57-4d6c-8ea5-edd0e195461e"
    }
}
```

