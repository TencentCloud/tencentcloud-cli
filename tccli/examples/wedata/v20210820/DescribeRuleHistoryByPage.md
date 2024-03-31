**Example 1: 分页查询规则操作记录接口**



Input: 

```
tccli wedata DescribeRuleHistoryByPage --cli-unfold-argument  \
    --ProjectId abc \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name tableId \
    --Filters.0.Values 968tygoiuhb087yefg
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleId": 1,
                    "AlterTime": "2023-10-01",
                    "AlterContent": "content",
                    "OperatorUserId": 1,
                    "OperatorName": ">"
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

