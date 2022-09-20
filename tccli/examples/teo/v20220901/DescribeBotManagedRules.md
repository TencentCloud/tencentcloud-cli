**Example 1: 查询bot规则库**



Input: 

```
tccli teo DescribeBotManagedRules --cli-unfold-argument  \
    --RuleType  \
    --Offset 2 \
    --Entity a.eotest.com \
    --Limit 1 \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "RequestId": "c1e7056d-ed79-4b24-b791-aaa3ccadc6ee",
        "Count": 2,
        "BotManagedRuleDetails": [
            {
                "Description": "Uncategorised",
                "RuleId": 1000,
                "RuleTypeName": "uabot",
                "Status": "block"
            },
            {
                "Description": "Feed checker",
                "RuleId": 1001,
                "RuleTypeName": "uabot",
                "Status": "block"
            }
        ],
        "Total": 1500
    }
}
```

