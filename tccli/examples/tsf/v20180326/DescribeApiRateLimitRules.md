**Example 1: 查询API限流规则**



Input: 

```
tccli tsf DescribeApiRateLimitRules --cli-unfold-argument  \
    --ApiId api-uk1098lc1
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "UpdatedTime": "xx",
                "MaxQps": 1,
                "Description": "xx",
                "RuleId": "xx",
                "ApiId": "xx",
                "TsfRuleId": "xx",
                "UsableStatus": "enabled",
                "RuleName": "xx",
                "CreatedTime": "xx",
                "RuleContent": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

