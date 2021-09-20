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
        "RequestId": "req-566234234",
        "RuleTopList": [
            {
                "RuleName": "检测项名1",
                "Level": 1,
                "EventCount": 4000
            },
            {
                "RuleName": "检测项名2",
                "Level": 2,
                "EventCount": 4000
            }
        ]
    }
}
```

