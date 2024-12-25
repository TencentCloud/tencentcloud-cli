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
                        "flow-6a79x94v"
                    ],
                    "TriggerType": "auto",
                    "TimeOut": 3000,
                    "TaskRule": {
                        "RepeatInterval": 1,
                        "RuleType": "unicast",
                        "Expression": "* 30 * * * *"
                    },
                    "TaskState": "Running",
                    "SuccessRatio": 0,
                    "TaskContent": "this is desc",
                    "TaskArgument": "1,1,1",
                    "AdvanceSettings": {
                        "SubTaskConcurrency": 0
                    },
                    "RetryCount": 0,
                    "SuccessOperator": "null",
                    "TaskId": "task-6a79x94v",
                    "TaskType": "unicast",
                    "ShardCount": 0,
                    "ExecuteType": "unicast",
                    "TaskName": "task-name",
                    "ShardArguments": [
                        {
                            "ShardValue": "1",
                            "ShardKey": 1
                        }
                    ],
                    "GroupId": "group-6a79x94v",
                    "TaskLogId": "tlog-6a79x94v"
                }
            ],
            "TotalCount": 7
        },
        "RequestId": "sj28sk-m2ia2-k2901-9sjwj"
    }
}
```

