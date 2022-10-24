**Example 1: 查询规则列表概况**



Input: 

```
tccli cfw DescribeRuleOverview --cli-unfold-argument  \
    --Direction 0
```

Output: 
```
{
    "Response": {
        "AllTotal": 100,
        "StrategyNum": 70,
        "StartRuleNum": 70,
        "StopRuleNum": 30,
        "RemainingNum": 30,
        "RequestId": "cd0e1fdf-157d-438c-9bc8-75925e5d4e20"
    }
}
```

