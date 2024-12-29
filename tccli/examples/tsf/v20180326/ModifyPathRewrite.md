**Example 1: 修改路径重写顺序**



Input: 

```
tccli tsf ModifyPathRewrite --cli-unfold-argument  \
    --PathRewriteId rewrite-ba22pbpa \
    --Regex /consumer \
    --Replacement /provider \
    --Blocked N \
    --Order 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6b194892-2c0a-41d3-93e1-e4b293b0fde8",
        "Result": true
    }
}
```

