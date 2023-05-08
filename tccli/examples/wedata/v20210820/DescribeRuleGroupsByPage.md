**Example 1: 分页查询规则组接口**



Input: 

```
tccli wedata DescribeRuleGroupsByPage --cli-unfold-argument  \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --PageNumber 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
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
                    "UpdateTime": "xx",
                    "DatasourceName": "xx",
                    "RuleGroupId": 1,
                    "DatasourceType": 1,
                    "TableName": "xx",
                    "TableId": 1,
                    "TableOwnerName": "xx",
                    "MonitorType": 1,
                    "ExecStrategy": {
                        "Tasks": [
                            {
                                "TaskName": "xx",
                                "TaskId": 1
                            }
                        ],
                        "ExecQueue": "xx",
                        "RuleGroupId": 1,
                        "ExecutorGroupName": "xx",
                        "MonitorType": 1,
                        "ExecutorGroupId": 1
                    },
                    "DatasourceId": 1,
                    "Subscription": {
                        "Receivers": [
                            {
                                "ReceiverName": "xx"
                            }
                        ],
                        "SubscribeType": [
                            1
                        ],
                        "RuleGroupId": 1
                    }
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

