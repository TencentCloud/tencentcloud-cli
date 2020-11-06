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
    "RequestId": "2fc1e275-7cb3-41a7-a730-2f8576af3df2",
    "Result": {
        "TotalCount": 5,
        "Content": [
            {
                "RuleId": "lane-r-6a7gkd5a",
                "RuleName": "testlea",
                "Priority": 1,
                "Remark": "",
                "RuleTagList": null,
                "RuleTagRelationship": "RELEATION_OR",
                "LaneId": "lane-gyqkq9dy",
                "Enable": true,
                "CreateTime": 1586353671000,
                "UpdateTime": 1586353671000
            },
            {
                "RuleId": "lane-r-6ym2jmkv",
                "RuleName": "测试网关",
                "Priority": 2,
                "Remark": "",
                "RuleTagList": null,
                "RuleTagRelationship": "RELEATION_AND",
                "LaneId": "lane-jy9lp7zy",
                "Enable": true,
                "CreateTime": 1586353671000,
                "UpdateTime": 1586353671000
            },
            {
                "RuleId": "lane-r-ba2xk9jy",
                "RuleName": "sdfasf",
                "Priority": 3,
                "Remark": "",
                "RuleTagList": null,
                "RuleTagRelationship": "RELEATION_AND",
                "LaneId": "lane-5yrdkb8v",
                "Enable": false,
                "CreateTime": 1586353671000,
                "UpdateTime": 1586353671000
            },
            {
                "RuleId": "lane-r-byxnlxra",
                "RuleName": "1213123",
                "Priority": 4,
                "Remark": "23131212312",
                "RuleTagList": null,
                "RuleTagRelationship": "RELEATION_AND",
                "LaneId": "lane-5yrdkb8v",
                "Enable": false,
                "CreateTime": 1586353671000,
                "UpdateTime": 1586353671000
            },
            {
                "RuleId": "lane-r-nygd5xwy",
                "RuleName": "dsasd",
                "Priority": 5,
                "Remark": "",
                "RuleTagList": null,
                "RuleTagRelationship": "RELEATION_OR",
                "LaneId": "lane-5yrdkb8v",
                "Enable": true,
                "CreateTime": 1586353671000,
                "UpdateTime": 1586353671000
            }
        ]
    }
}
```

