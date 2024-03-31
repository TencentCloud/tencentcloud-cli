**Example 1: 查询规则组详情接口**



Input: 

```
tccli wedata DescribeRuleGroup --cli-unfold-argument  \
    --ProjectId 5678987645 \
    --DatabaseId 5rtfygfty6767tyug \
    --TableId 56tdryfccfyrt556t \
    --DatasourceId 44567 \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupId": 1,
            "DatasourceId": "567897",
            "DatasourceName": "hive-yihjkjui098",
            "DatasourceType": 1,
            "MonitorType": 1,
            "UpdateTime": "2023-10-01",
            "TableName": "test",
            "TableId": "abc",
            "TableOwnerName": "zhangsan",
            "ExecStrategy": {
                "RuleGroupId": 1,
                "MonitorType": 1,
                "ExecQueue": "test",
                "ExecutorGroupId": "5678uhjb",
                "ExecutorGroupName": "执行队列",
                "Tasks": [
                    {
                        "TaskId": "56t7yguy7878yu",
                        "TaskName": "任务1",
                        "WorkflowId": "789uijbihu78uy"
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
            "DatabaseId": "678yughvjgy7guh",
            "DatabaseName": "dbName",
            "Permission": true,
            "RuleCount": 1,
            "MonitorStatus": true,
            "TableOwnerUserId": 1,
            "InstanceId": "56789yu7ihg",
            "CreateTime": "2023-10-01",
            "StrategyConfig": true,
            "SubscribeConfig": true
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

