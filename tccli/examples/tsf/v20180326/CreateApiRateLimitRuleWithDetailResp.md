**Example 1: 创建新 API 分组限流规则**

创建新的 API 分组限流规则

Input: 

```
tccli tsf CreateApiRateLimitRuleWithDetailResp --cli-unfold-argument  \
    --ApiId api-xxxxxxx \
    --UsableStatus enable \
    --MaxQps 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "RuleId": "ruleId-xxxx",
            "ApiId": "abc",
            "RuleName": "null",
            "MaxQps": 1,
            "UsableStatus": "enable",
            "RuleContent": "xxx",
            "TsfRuleId": "tsfRuleId-xxx",
            "Description": "null",
            "CreatedTime": "xxxx-xx-xx",
            "UpdatedTime": "xxxx-xx-xx"
        },
        "RequestId": "xxxxxxxxxxx"
    }
}
```

