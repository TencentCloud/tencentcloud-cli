**Example 1: 基线检测项TOP接口**

根据策略id基线检测项TOP查询基线检测项top

Input: 

```
tccli cwp DescribeBaselineTop --cli-unfold-argument  \
    --StrategyId 1 \
    --Top 5
```

Output: 
```
{
    "Response": {
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "RuleTopList": [
            {
                "RuleName": "检测项名1",
                "Level": 1,
                "EventCount": 4000,
                "RuleId": 1
            },
            {
                "RuleName": "检测项名2",
                "Level": 2,
                "EventCount": 4000,
                "RuleId": 2
            }
        ]
    }
}
```

