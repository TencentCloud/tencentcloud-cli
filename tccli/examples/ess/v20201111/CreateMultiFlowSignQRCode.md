**Example 1: CreateMultiFlowSignQRCode**



Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName xx \
    --MaxFlowNum 0 \
    --FlowEffectiveDay 0 \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.UserId xx \
    --Operator.Channel xx \
    --Operator.ProxyIp xx \
    --TemplateId xx \
    --QrEffectiveDay 0 \
    --CallbackUrl xx
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "QrCodeUrl": "xx",
            "ExpiredTime": 5,
            "QrCodeId": "xx"
        },
        "SignUrls": {
            "EffectiveTime": "xx",
            "HttpSignUrl": "xx",
            "AppSignUrl": "xx"
        },
        "RequestId": "xx"
    }
}
```

