**Example 1: 批量更新API限流规则**



Input: 

```
tccli tsf UpdateApiRateLimitRules --cli-unfold-argument  \
    --ApiIds api-d5970cd api-d5971cd \
    --UsableStatus enabled \
    --MaxQps 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e5507e42d5970cd2e25ed5267a",
        "Result": true
    }
}
```

