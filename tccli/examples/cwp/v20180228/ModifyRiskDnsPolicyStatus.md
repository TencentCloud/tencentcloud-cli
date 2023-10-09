**Example 1: 更改恶意请求策略状态**



Input: 

```
tccli cwp ModifyRiskDnsPolicyStatus --cli-unfold-argument  \
    --PolicyId 500001 \
    --IsEnabled 0
```

Output: 
```
{
    "Response": {
        "RequestId": "130e109f-a922-4d16-827d-b17a366125a2"
    }
}
```

