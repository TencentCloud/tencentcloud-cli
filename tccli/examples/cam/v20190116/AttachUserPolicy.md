**Example 1: 绑定策略到用户**

绑定策略ID为524497的策略到用户3449203261

Input: 

```
tccli cam AttachUserPolicy --cli-unfold-argument  \
    --AttachUin 3449203261 \
    --PolicyId 524497
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

