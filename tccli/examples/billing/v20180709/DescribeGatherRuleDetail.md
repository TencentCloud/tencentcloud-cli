**Example 1: 查询归集规则详情**



Input: 

```
tccli billing DescribeGatherRuleDetail --cli-unfold-argument  \
    --Id 17 \
    --Month 2022-11
```

Output: 
```
{
    "Response": {
        "Id": 17,
        "Uin": "909619400",
        "UpdateTime": "2022-10-21 17:44:22",
        "RuleDetail": {
            "Connectors": "and",
            "Children": [
                {
                    "RuleKey": "businessCode",
                    "Operator": "=",
                    "RuleValue": [
                        "p_cvm"
                    ]
                },
                {
                    "RuleKey": "regionId",
                    "Operator": "=",
                    "RuleValue": [
                        "9"
                    ]
                },
                {
                    "Connectors": "and",
                    "Children": [
                        {
                            "RuleKey": "projectId",
                            "Operator": "=",
                            "RuleValue": [
                                "1270522"
                            ]
                        }
                    ]
                }
            ]
        },
        "RequestId": "fcbfb5c0-9589-4c78-a01b-481ab01cbf76"
    }
}
```

