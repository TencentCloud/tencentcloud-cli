**Example 1: 云边界规则列表**



Input: 

```
tccli csip DescribeExposeRules --cli-unfold-argument  \
    --Filters.0.Name RuleType \
    --Filters.0.Values netscan_vul
```

Output: 
```
{
    "Response": {
        "ExposeRuleList": [
            {
                "FixAdvice": "u70b9u51fbu201cu8be6u60c5u201duff0cu67e5u770bu6f0fu6d1eu5e76u5b8cu6210u4feeu590du3002",
                "RuleType": "netscan_vul",
                "Severity": "high",
                "Title": "u7f51u7edcu626bu63cfu53d1u73b0u6f0fu6d1e"
            }
        ],
        "RequestId": "66995654-7c56-4b5d-b9ef-b6d2c6fcd96a"
    }
}
```

