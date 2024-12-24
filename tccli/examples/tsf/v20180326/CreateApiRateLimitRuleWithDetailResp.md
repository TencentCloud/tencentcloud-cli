**Example 1: 创建新 API 分组限流规则**

创建新的 API 分组限流规则

Input: 

```
tccli tsf CreateApiRateLimitRuleWithDetailResp --cli-unfold-argument  \
    --ApiId api-7h13jx9z \
    --MaxQps 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "ada294ab-6322-4262-982c-a8960085486b",
        "Result": {
            "ApiId": null,
            "CreatedTime": null,
            "Description": null,
            "MaxQps": null,
            "RuleContent": null,
            "RuleId": "rule-jwo9eexw",
            "RuleName": null,
            "TsfRuleId": null,
            "UpdatedTime": null,
            "UsableStatus": null
        }
    }
}
```

