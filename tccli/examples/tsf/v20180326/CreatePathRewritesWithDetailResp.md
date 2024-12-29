**Example 1: 批量创建路径重写**

创建路径重写规则

Input: 

```
tccli tsf CreatePathRewritesWithDetailResp --cli-unfold-argument  \
    --PathRewrites.0.GatewayGroupId group-ldap5yok \
    --PathRewrites.0.Regex /consumer \
    --PathRewrites.0.Replacement /provider \
    --PathRewrites.0.Blocked N \
    --PathRewrites.0.Order 1
```

Output: 
```
{
    "Response": {
        "RequestId": "29e9b18a-2886-4582-bc14-fdb56aa49c8c",
        "Result": [
            "rewrite-py5r7b6v"
        ]
    }
}
```

