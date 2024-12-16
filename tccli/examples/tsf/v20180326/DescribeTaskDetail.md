**Example 1: 查询任务详情**



Input: 

```
tccli tsf DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-6a79x94v
```

Output: 
```
{
    "Response": {
        "Result": {
            "RetryInterval": 0,
            "TriggerType": "auto",
            "TimeOut": 0,
            "TaskRule": {
                "RepeatInterval": 1,
                "RuleType": "cron",
                "Expression": "* 30 * * * ? *"
            },
            "TaskState": "Running",
            "SuccessRatio": 0,
            "TaskContent": "1,2,3,4,5",
            "TaskArgument": "1,2,3,4,5",
            "AdvanceSettings": {
                "SubTaskConcurrency": 0
            },
            "RetryCount": 0,
            "SuccessOperator": "noop",
            "TaskId": "task-6a79x94v",
            "TaskType": "normal",
            "ShardCount": 0,
            "ExecuteType": "auto",
            "TaskName": "task-mock",
            "ShardArguments": [
                {
                    "ShardValue": "4",
                    "ShardKey": 1
                }
            ],
            "GroupId": "group-6a79x94v",
            "TaskLogId": "tlog-6a79x94v",
            "BelongFlowIds": [
                "flow-6a79x94v"
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

