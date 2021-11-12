**Example 1: 查询泳道规则列表**



Input: 

```
tccli tsf DescribeLaneRules --cli-unfold-argument  \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "Content": [
                {
                    "Remark": "xx",
                    "Enable": true,
                    "RuleTagList": [
                        {
                            "UpdateTime": 0,
                            "TagId": "xx",
                            "TagOperator": "xx",
                            "TagValue": "xx",
                            "TagName": "xx",
                            "LaneRuleId": "xx",
                            "CreateTime": 0
                        }
                    ],
                    "RuleId": "xx",
                    "RuleTagRelationship": "xx",
                    "UpdateTime": 0,
                    "Priority": 0,
                    "LaneId": "xx",
                    "RuleName": "xx",
                    "CreateTime": 0
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

