**Example 1: 创建路径重写**



Input: 

```
tccli tsf CreatePathRewrites --cli-unfold-argument  \
    --PathRewrites.GatewayGroupId group-yo476mrv \
    --PathRewrites.Regex /provider \
    --PathRewrites.Replacement /user \
    --PathRewrites.Blocked N \
    --PathRewrites.Order 1
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

