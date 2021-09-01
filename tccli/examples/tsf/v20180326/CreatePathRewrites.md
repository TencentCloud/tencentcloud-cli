**Example 1: 创建路径重写**



Input: 

```
tccli tsf CreatePathRewrites --cli-unfold-argument  \
    --PathRewrites.Regex xx \
    --PathRewrites.GatewayGroupId xx \
    --PathRewrites.Blocked xx \
    --PathRewrites.Order 0 \
    --PathRewrites.Replacement xx
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

