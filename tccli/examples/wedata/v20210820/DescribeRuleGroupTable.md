**Example 1: 查询表绑定执行规则组信息**



Input: 

```
tccli wedata DescribeRuleGroupTable --cli-unfold-argument  \
    --TableId 2389yuho80yhu
```

Output: 
```
{
    "Response": {
        "Data": {
            "TableInfo": {
                "TableId": "896rtfyoghuibasd",
                "TableName": "teste",
                "InstanceId": "5679t8ygihub",
                "DatasourceId": "6789",
                "DatasourceName": "hive-uibgj97ug",
                "DatasourceType": 0,
                "DatabaseId": "7tyg89i978yuh",
                "DatabaseName": "dbName",
                "ProjectId": 0,
                "UserId": 0
            },
            "RuleGroups": [
                {
                    "Id": 0,
                    "MonitorType": 0,
                    "StartTime": "2023-10-01",
                    "EndTime": "2023-10-01",
                    "CycleType": "10",
                    "CycleStep": 0,
                    "CycleDesc": "abc",
                    "TaskAction": "abc",
                    "DelayTime": 0,
                    "CycleTaskId": "abc",
                    "AssociateTaskIds": [
                        "abc"
                    ]
                }
            ],
            "Subscriptions": [
                {
                    "RuleGroupId": 1,
                    "Receivers": [
                        {
                            "ReceiverUserId": 1,
                            "ReceiverName": "zhangan"
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
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

