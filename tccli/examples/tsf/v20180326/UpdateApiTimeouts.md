**Example 1: 批量更新API超时**



Input: 

```
tccli tsf UpdateApiTimeouts --cli-unfold-argument  \
    --ApiIds api-d5970cd api-d5971cd \
    --UsableStatus enabled \
    --Timeout 10000
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

