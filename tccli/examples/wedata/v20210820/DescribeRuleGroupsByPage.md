**Example 1: 分页查询规则组接口**



Input: 

```
tccli wedata DescribeRuleGroupsByPage --cli-unfold-argument  \
    --OrderFields.0.Direction ASC \
    --OrderFields.0.Name id \
    --PageNumber 1 \
    --Filters.0.Values 78yguhbjbju78yguh \
    --Filters.0.Name tableId \
    --PageSize 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleGroupId": 1,
                    "DatasourceId": "54任ftg678tyguh",
                    "DatasourceName": "dbName",
                    "DatasourceType": 1,
                    "MonitorType": 1,
                    "UpdateTime": "2023-10-01",
                    "TableName": "test",
                    "TableId": "78uyighbjuy787uy",
                    "TableOwnerName": "zhangsan",
                    "ExecStrategy": {
                        "RuleGroupId": 1,
                        "MonitorType": 1,
                        "ExecQueue": "789y7uihjb",
                        "ExecutorGroupId": "t678yughbjnjhyui77",
                        "ExecutorGroupName": "执行队列",
                        "Tasks": [
                            {
                                "TaskId": "78yughuy778uyihj",
                                "TaskName": "上游任务",
                                "WorkflowId": "786ytughhuy778uy"
                            }
                        ],
                        "StartTime": "2023-10-01",
                        "EndTime": "2023-10-01",
                        "CycleType": "abc",
                        "DelayTime": 1,
                        "CycleStep": 1,
                        "TaskAction": "abc",
                        "ExecEngineType": "abc",
                        "ExecPlan": "abc",
                        "RuleId": 1,
                        "RuleName": "规则1"
                    },
                    "Subscription": {
                        "RuleGroupId": 1,
                        "Receivers": [
                            {
                                "ReceiverUserId": 1,
                                "ReceiverName": "zhangsan"
                            }
                        ],
                        "SubscribeType": [
                            1
                        ],
                        "WebHooks": [
                            {
                                "HookType": "abc",
                                "HookAddress": "abc"
                            }
                        ],
                        "RuleId": 1,
                        "RuleName": "规则1"
                    },
                    "DatabaseId": "78yuhiguiy7878yui",
                    "DatabaseName": "dbName",
                    "Permission": true,
                    "RuleCount": 1,
                    "MonitorStatus": true,
                    "TableOwnerUserId": 1,
                    "InstanceId": "78yuhiuiy8",
                    "CreateTime": "2023-10-01",
                    "StrategyConfig": true,
                    "SubscribeConfig": true
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

