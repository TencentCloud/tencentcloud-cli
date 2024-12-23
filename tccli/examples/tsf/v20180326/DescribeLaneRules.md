**Example 1: 查询泳道规则列表**



Input: 

```
tccli tsf DescribeLaneRules --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --SearchWord ruleName \
    --RuleId lane-r-v6ewp385 \
    --RuleIdList lane-r-v6ewp385
```

Output: 
```
{
    "Response": {
        "RequestId": "e4a47430-c0f8-4ebb-9a20-774e32936035",
        "Result": {
            "Content": [
                {
                    "CreateTime": 1725509095000,
                    "Enable": true,
                    "LaneId": "lane-ynmlnwm4",
                    "Priority": 1,
                    "Remark": "",
                    "RuleId": "lane-r-v6ewp385",
                    "RuleName": "rule_app",
                    "RuleTagList": null,
                    "RuleTagRelationship": "RELEATION_AND",
                    "UpdateTime": 1727167548000
                }
            ],
            "TotalCount": 1
        }
    }
}
```

