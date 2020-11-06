**Example 1: 解除绑定到用户的策略**

解除绑定到用户3449203261的策略16313162

Input: 

```
tccli cam DetachUserPolicy --cli-unfold-argument  \
    --PolicyId 16313162 \
    --DetachUin 3449203261
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

