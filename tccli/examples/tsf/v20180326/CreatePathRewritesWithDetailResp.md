**Example 1: 批量创建路径重写**

创建路径重写规则

Input: 

```
tccli tsf CreatePathRewritesWithDetailResp --cli-unfold-argument  \
    --PathRewrites.0.GatewayGroupId abc \
    --PathRewrites.0.Regex abc \
    --PathRewrites.0.Replacement abc \
    --PathRewrites.0.Blocked abc \
    --PathRewrites.0.Order 0
```

Output: 
```
{
    "Response": {
        "Result": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

