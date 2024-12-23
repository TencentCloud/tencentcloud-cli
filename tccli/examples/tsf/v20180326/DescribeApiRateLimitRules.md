**Example 1: 查询API限流规则**



Input: 

```
tccli tsf DescribeApiRateLimitRules --cli-unfold-argument  \
    --ApiId api-9jw9mzhu
```

Output: 
```
{
    "Response": {
        "RequestId": "5a2cc367-a74e-49c0-a5ac-52902aa67535",
        "Result": [
            {
                "ApiId": "api-9jw9mzhu",
                "CreatedTime": "2024-12-23 14:38:26",
                "Description": null,
                "MaxQps": 10000,
                "RuleContent": null,
                "RuleId": "rule-gtqzfihy",
                "RuleName": "gateway-proxy-rule_grp-ptrhio2l_api-9jw9mzhu",
                "TsfRuleId": "rate-ab423r9v",
                "UpdatedTime": "2024-12-23 14:38:26",
                "UsableStatus": "enabled"
            }
        ]
    }
}
```

