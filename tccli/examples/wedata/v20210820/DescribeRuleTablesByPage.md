**Example 1: 获取表列表**

获取表列表

Input: 

```
tccli wedata DescribeRuleTablesByPage --cli-unfold-argument  \
    --ProjectId xx \
    --PageNumber 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 1 \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx
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
                    "TableOwnerName": "xx",
                    "Permission": true,
                    "DatasourceType": 1,
                    "RuleGroupId": 1,
                    "TableName": "xx",
                    "DatabaseId": "xx",
                    "TableId": "xx",
                    "DatabaseName": "xx",
                    "MonitorType": 1,
                    "RuleCount": 1,
                    "ExecStrategy": {
                        "Tasks": [
                            {
                                "TaskName": "xx",
                                "WorkflowId": "xx",
                                "TaskId": "xx"
                            }
                        ],
                        "DelayTime": 1,
                        "ExecQueue": "xx",
                        "RuleGroupId": 1,
                        "TaskAction": "xx",
                        "CycleType": "xx",
                        "ExecutorGroupName": "xx",
                        "StartTime": "xx",
                        "MonitorType": 1,
                        "EndTime": "xx",
                        "ExecutorGroupId": "xx",
                        "CycleStep": 1
                    },
                    "MonitorStatus": true,
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
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

