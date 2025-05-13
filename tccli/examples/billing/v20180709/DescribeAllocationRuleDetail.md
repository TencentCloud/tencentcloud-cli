**Example 1: 查询公摊规则详情**



Input: 

```
tccli billing DescribeAllocationRuleDetail --cli-unfold-argument  \
    --Month 202210 \
    --RuleId 24
```

Output: 
```
{
    "Response": {
        "Id": 24,
        "Uin": "909619400",
        "Name": "test_allocation2",
        "Type": 1,
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
        "RatioDetail": [
            {
                "NodeId": 6,
                "Ratio": 40
            },
            {
                "NodeId": 7,
                "Ratio": 60
            }
        ],
        "RequestId": "b9fd53c2-d5d3-4f49-8a6d-dd0b2e9c02bf"
    }
}
```

