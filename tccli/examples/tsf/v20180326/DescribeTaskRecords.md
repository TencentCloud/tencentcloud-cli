**Example 1: 查询任务列表**



Input: 

```
tccli tsf DescribeTaskRecords --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "RetryInterval": 0,
                    "BelongFlowIds": [
                        "xx"
                    ],
                    "TriggerType": "xx",
                    "TimeOut": 3000,
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
                    "TaskLogId": "xx"
                }
            ],
            "TotalCount": 7
        },
        "RequestId": "xx"
    }
}
```

