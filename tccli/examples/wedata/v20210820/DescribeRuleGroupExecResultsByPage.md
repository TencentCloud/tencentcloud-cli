**Example 1: 规则组执行结果分页查询接口**



Input: 

```
tccli wedata DescribeRuleGroupExecResultsByPage --cli-unfold-argument  \
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
                    "Status": 1,
                    "AlarmRuleCount": 1,
                    "RuleGroupId": 1,
                    "RuleGroupExecId": 1,
                    "TableName": "xx",
                    "ExecTime": "xx",
                    "TableId": 1,
                    "TableOwnerName": "xx",
                    "TriggerType": 1,
                    "TotalRuleCount": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

