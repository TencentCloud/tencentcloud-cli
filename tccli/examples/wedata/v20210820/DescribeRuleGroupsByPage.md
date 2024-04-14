**Example 1: 分页查询规则组接口**



Input: 

```
tccli wedata DescribeRuleGroupsByPage --cli-unfold-argument  \
    --OrderFields.0.Direction ASC \
    --OrderFields.0.Name id \
    --PageNumber 1 \
    --Filters.0.Values 78yguhbu78yguh \
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
                    "DatasourceId": "IBw6DFI_pGVj1F73Q",
                    "DatasourceName": "hive-emr-asda",
                    "DatasourceType": 1,
                    "MonitorType": 1,
                    "UpdateTime": "2022-09-08",
                    "TableName": "table1",
                    "TableId": "IBw6DFI_pGVj1F73Q",
                    "TableOwnerName": "zhangsan",
                    "ExecStrategy": {
                        "RuleGroupId": 1,
                        "MonitorType": 1,
                        "ExecQueue": "default",
                        "ExecutorGroupId": "1",
                        "ExecutorGroupName": "default",
                        "Tasks": [
                            {
                                "WorkflowId": "workflow_dq_1008997",
                                "TaskId": "202403567999922",
                                "TaskName": "shell_test1",
                                "CycleType": 0
                            }
                        ],
                        "StartTime": "2023-09-07 09:09:09",
                        "EndTime": "2023-09-08 09:09:09",
                        "CycleType": "D",
                        "DelayTime": 1,
                        "CycleStep": 1,
                        "TaskAction": "",
                        "ExecEngineType": "HIVE",
                        "ExecPlan": "2024-04-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
                        "RuleId": 1,
                        "RuleName": "规则名称",
                        "TriggerTypes": [
                            "1"
                        ]
                    },
                    "Subscription": {
                        "RuleGroupId": 1,
                        "Receivers": [
                            {
                                "ReceiverUserId": 1078892223332,
                                "ReceiverName": "zhangsan"
                            }
                        ],
                        "SubscribeType": [
                            1
                        ],
                        "WebHooks": [
                            {
                                "HookType": "feishu",
                                "HookAddress": "http://aassdd.com"
                            }
                        ],
                        "RuleId": 1,
                        "RuleName": "规则名称"
                    },
                    "DatabaseId": "IBw6DFI_pGVj1F73Q",
                    "DatabaseName": "dq_test1",
                    "Permission": true,
                    "RuleCount": 1,
                    "MonitorStatus": true,
                    "TableOwnerUserId": 1,
                    "InstanceId": "emr-asda",
                    "CreateTime": "2022-09-08",
                    "StrategyConfig": true,
                    "SubscribeConfig": true,
                    "DsEnvType": 0
                }
            ]
        },
        "RequestId": "e06e90e7-40e0-4cf4--5566c"
    }
}
```

