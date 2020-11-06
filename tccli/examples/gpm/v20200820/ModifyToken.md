**Example 1: 更新匹配Token示例**



Input: 

```
tccli gpm ModifyToken --cli-unfold-argument  \
    --MatchCode match-58mnuqlz \
    --MatchToken mytoken \
    --CompatibleSpan 300
```

Output: 
```
{
    "Response": {
        "MatchToken": "mytoken",
        "CompatibleSpan": 180,
        "RequestId": "ab6ab15a-ab3a-495c-8818-e826084ea072"
    }
}
```

