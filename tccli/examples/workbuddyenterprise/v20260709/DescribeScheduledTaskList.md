**Example 1: 查询定时任务列表**



Input: 

```
tccli workbuddyenterprise DescribeScheduledTaskList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --Filters.0.Name  \
    --Filters.0.Values  \
    --Filters.0.ExactMatch False
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ScheduledTaskSet": [
            {
                "TaskId": 0,
                "TaskKey": "",
                "TaskName": "",
                "AgentId": "",
                "CronExpr": "",
                "Status": 0,
                "LastRunTime": "",
                "NextRunTime": "",
                "CreatedTime": "",
                "AgentConfig": {
                    "Prompt": ""
                }
            }
        ],
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

