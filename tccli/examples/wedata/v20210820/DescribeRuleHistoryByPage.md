**Example 1: 分页查询规则操作记录接口**



Input: 

```
tccli wedata DescribeRuleHistoryByPage --cli-unfold-argument  \
    --ProjectId 1 \
    --PageNumber 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "AlterTime": "xx",
                    "AlterContent": "xx",
                    "OperatorUserId": 1,
                    "OperatorName": "xx",
                    "RuleId": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

