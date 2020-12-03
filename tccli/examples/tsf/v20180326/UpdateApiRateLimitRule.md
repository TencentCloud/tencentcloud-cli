**Example 1: 更新API限流规则**



Input: 

```
tccli tsf UpdateApiRateLimitRule --cli-unfold-argument  \
    --RuleId rule-d5970cd2 \
    --UsableStatus enabled \
    --MaxQps 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": false
    }
}
```

