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
            "TotalCount": 0,
            "Content": [
                {
                    "RuleId": "abc",
                    "RuleName": "abc",
                    "Priority": 0,
                    "Remark": "abc",
                    "RuleTagList": [
                        {
                            "TagId": "abc",
                            "TagName": "abc",
                            "TagOperator": "abc",
                            "TagValue": "abc",
                            "LaneRuleId": "abc",
                            "CreateTime": 0,
                            "UpdateTime": 0
                        }
                    ],
                    "RuleTagRelationship": "abc",
                    "LaneId": "abc",
                    "Enable": true,
                    "CreateTime": 0,
                    "UpdateTime": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

