**Example 1: 创建API限流规则**



Input: 

```
tccli tsf CreateApiRateLimitRule --cli-unfold-argument  \
    --ApiId api-uk1098lc1 \
    --MaxQps 100
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

