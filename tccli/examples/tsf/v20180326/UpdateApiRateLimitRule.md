**Example 1: 更新API限流规则**



Input: 

```
tccli tsf UpdateApiRateLimitRule --cli-unfold-argument  \
    --RuleId rule-8qlpdumd \
    --UsableStatus enabled \
    --MaxQps 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "ebba8f15-b795-4bdc-b881-049e33ef3fcb",
        "Result": true
    }
}
```

