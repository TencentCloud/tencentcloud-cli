**Example 1: 例子**



Input: 

```
tccli wedata DescribeExecStrategy --cli-unfold-argument  \
    --RuleGroupId 1 \
    --ProjectId 5678976547
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupId": 1,
            "MonitorType": 1,
            "ExecQueue": "test",
            "ExecutorGroupId": "5678987567",
            "ExecutorGroupName": "执行队列",
            "Tasks": [
                {
                    "TaskId": "56777777777767tgy676tgy",
                    "TaskName": "任务名",
                    "WorkflowId": "67tyg9h87yhun80o7yuh"
                }
            ],
            "StartTime": "2023-10-01",
            "EndTime": "2023-10-01",
            "CycleType": "abc",
            "DelayTime": 1,
            "CycleStep": 1,
            "TaskAction": "2",
            "ExecEngineType": "HIVE",
            "ExecPlan": "2024-03-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
            "RuleId": 1,
            "RuleName": "规则1"
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

