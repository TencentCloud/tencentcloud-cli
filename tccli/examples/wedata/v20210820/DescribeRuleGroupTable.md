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
                "TableId": "896rtfyogbasd",
                "TableName": "teste",
                "InstanceId": "5679t8yihub",
                "DatasourceId": "6789",
                "DatasourceName": "hive-uij97ug",
                "DatasourceType": 0,
                "DatabaseId": "7tyg89i8yuh",
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
                    "CycleType": "D",
                    "CycleStep": 1,
                    "CycleDesc": "3",
                    "TaskAction": "1",
                    "DelayTime": 0,
                    "CycleTaskId": "20240307109",
                    "AssociateTaskIds": [
                        "2024007195414609"
                    ]
                }
            ],
            "Subscriptions": [
                {
                    "RuleGroupId": 1,
                    "Receivers": [
                        {
                            "ReceiverUserId": 12738273899,
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
        "RequestId": "0ff4e8ae-ec4b68e69"
    }
}
```

