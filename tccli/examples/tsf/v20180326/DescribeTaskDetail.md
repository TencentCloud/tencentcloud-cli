**Example 1: 查询任务详情**



Input: 

```
tccli tsf DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "RetryInterval": 0,
            "TriggerType": "xx",
            "TimeOut": 0,
            "TaskRule": {
                "RepeatInterval": 1,
                "RuleType": "xx",
                "Expression": "xx"
            },
            "TaskState": "xx",
            "SuccessRatio": 0,
            "TaskContent": "xx",
            "TaskArgument": "xx",
            "AdvanceSettings": {
                "SubTaskConcurrency": 0
            },
            "RetryCount": 0,
            "SuccessOperator": "xx",
            "TaskId": "xx",
            "TaskType": "xx",
            "ShardCount": 0,
            "ExecuteType": "xx",
            "TaskName": "xx",
            "ShardArguments": [
                {
                    "ShardValue": "xx",
                    "ShardKey": 1
                }
            ],
            "GroupId": "xx",
            "TaskLogId": "xx",
            "BelongFlowIds": [
                "xx"
            ]
        },
        "RequestId": "xx"
    }
}
```

