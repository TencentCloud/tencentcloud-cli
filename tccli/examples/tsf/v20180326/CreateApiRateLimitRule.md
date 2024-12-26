**Example 1: 创建API限流规则**



Input: 

```
tccli tsf CreateApiRateLimitRule --cli-unfold-argument  \
    --ApiId api-8c7538te \
    --UsableStatus enabled \
    --MaxQps 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "af8bda56-e2f3-440f-a05c-25d63bdc397e",
        "Result": true
    }
}
```

