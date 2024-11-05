**Example 1: 规则列表**



Input: 

```
tccli cwp DescribeBaselineRuleList --cli-unfold-argument  \
    --Limit 10 \
    --Filters.0.Values auto_**** \
    --Filters.0.Name RuleName \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostIds": [
                    "d99a1b46-cc2d-4633-a11f-4a7663d25***"
                ],
                "HostIps": [
                    "176.1.1.**"
                ],
                "AssetType": "1",
                "RuleName": "ruleName01",
                "CategoryId": -1,
                "RuleDesc": "rule desc",
                "Items": [
                    {
                        "ItemName": "name***",
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

