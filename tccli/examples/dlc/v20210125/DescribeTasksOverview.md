**Example 1: 查询任务概览情况**



Input: 

```
tccli dlc DescribeTasksOverview --cli-unfold-argument  \
    --StartTime 2022-08-23 00:00:00 \
    --EndTime 2022-08-30 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "923423423445",
        "TasksOverview": {
            "TaskQueuedCount": 0,
            "TaskInitCount": 0,
            "TaskRunningCount": 0,
            "TotalTaskCount": 0
        }
    }
}
```

