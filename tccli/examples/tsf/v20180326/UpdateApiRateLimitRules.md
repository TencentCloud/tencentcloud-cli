**Example 1: 批量更新API限流规则**



Input: 

```
tccli tsf UpdateApiRateLimitRules --cli-unfold-argument  \
    --ApiIds api-b1sd366q \
    --UsableStatus enabled \
    --MaxQps 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "94bddd45-fd4c-4192-aea2-5eeb5b74d5b6",
        "Result": true
    }
}
```

