**Example 1: 绑定策略到用户**

绑定策略ID为524497的策略到组ID为3449的用户组

Input: 

```
tccli cam AttachGroupPolicy --cli-unfold-argument  \
    --PolicyId 524497 \
    --AttachGroupId 3449
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

