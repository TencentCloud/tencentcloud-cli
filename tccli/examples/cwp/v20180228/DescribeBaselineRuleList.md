**Example 1: 规则列表**



Input: 

```
tccli cwp DescribeBaselineRuleList --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Values test \
    --Filters.0.Name RuleName \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RuleName": "test111",
                "CategoryId": -1,
                "RuleDesc": "test111",
                "Items": [
                    {
                        "ItemId": 1000
                    }
                ],
                "RuleId": 35184372088862,
                "RuleType": 1,
                "HostCount": 0
            }
        ],
        "RequestId": "8d445426-dfea-459c-9a13-1c1a3141353d",
        "Total": 1
    }
}
```

