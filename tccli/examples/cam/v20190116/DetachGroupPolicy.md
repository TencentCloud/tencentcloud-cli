**Example 1: 解除绑定到用户组的策略**

解除绑定到组ID为3449的策略524497

Input: 

```
tccli cam DetachGroupPolicy --cli-unfold-argument  \
    --PolicyId 524497 \
    --DetachGroupId 3449
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

