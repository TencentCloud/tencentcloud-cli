**Example 1: 获取表列表**

获取表列表

Input: 

```
tccli wedata DescribeRuleTablesByPage --cli-unfold-argument  \
    --ProjectId abc \
    --PageSize 1 \
    --PageNumber 1 \
    --Filters.0.Name tableId \
    --Filters.0.Values 79tugijh97u0iq34ew \
    --OrderFields.0.Name id \
    --OrderFields.0.Direction asc
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
                    "DatasourceId": "567890",
                    "DatasourceName": "dbName",
                    "DatasourceType": 1,
                    "MonitorType": 1,
                    "UpdateTime": "2023-10-01",
                    "TableName": "test",
                    "TableId": "79ugyihb80yui34",
                    "TableOwnerName": "zhangsan",
                    "ExecStrategy": {
                        "RuleGroupId": 1,
                        "MonitorType": 1,
                        "ExecQueue": "test",
                        "ExecutorGroupId": "56789098675",
                        "ExecutorGroupName": "name",
                        "Tasks": [
                            {
                                "TaskId": "68790876",
                                "TaskName": "r任务名",
                                "WorkflowId": "89yuhojnfade8u80yihogsad324"
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
                                "HookType": "1",
                                "HookAddress": "zhangsan"
                            }
                        ],
                        "RuleId": 1,
                        "RuleName": "规则1"
                    },
                    "DatabaseId": "68yfihv79tugoijwdefc",
                    "DatabaseName": "dbName",
                    "Permission": true,
                    "RuleCount": 1,
                    "MonitorStatus": true,
                    "TableOwnerUserId": 1,
                    "InstanceId": "68tyfguv97tyug7t9yg",
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

