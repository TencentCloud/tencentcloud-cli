**Example 1: 查询表绑定执行规则组信息**



Input: 

```
tccli wedata DescribeRuleGroupTable --cli-unfold-argument  \
    --TableId 
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroups": [
                {
                    "CycleTaskId": "xx",
                    "EndTime": "xx",
                    "AssociateTaskIds": [
                        "xx"
                    ],
                    "CycleDesc": "xx",
                    "CycleType": "xx",
                    "DelayTime": 0,
                    "StartTime": "xx",
                    "Id": 0,
                    "MonitorType": 0,
                    "TaskAction": "xx",
                    "CycleStep": 0
                }
            ],
            "TableInfo": {
                "DatabaseId": "xx",
                "DatasourceName": "xx",
                "InstanceId": "xx",
                "TableName": "xx",
                "UserId": 0,
                "TableId": "xx",
                "DatabaseName": "xx",
                "ProjectId": 0,
                "DatasourceType": 0,
                "DatasourceId": "xx"
            },
            "Subscriptions": [
                {
                    "Receivers": [
                        {
                            "ReceiverUserId": 1,
                            "ReceiverName": "xx"
                        }
                    ],
                    "SubscribeType": [
                        1
                    ],
                    "RuleGroupId": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

