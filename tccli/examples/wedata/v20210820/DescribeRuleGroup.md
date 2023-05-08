**Example 1: 查询规则组详情接口**



Input: 

```
tccli wedata DescribeRuleGroup --cli-unfold-argument  \
    --ProjectId xx \
    --DatabaseId xx \
    --TableId xx \
    --DatasourceId xx \
    --RuleGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "UpdateTime": "xx",
            "DatasourceName": "xx",
            "TableOwnerName": "xx",
            "RuleGroupId": 1,
            "DatasourceType": 1,
            "TableName": "xx",
            "DatabaseId": "xx",
            "TableId": "xx",
            "DatabaseName": "xx",
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
            "DatasourceId": "xx",
            "Subscription": {
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
        },
        "RequestId": "xx"
    }
}
```

