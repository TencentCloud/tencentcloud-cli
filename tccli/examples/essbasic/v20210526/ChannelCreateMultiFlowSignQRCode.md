**Example 1: ChannelCreateMultiFlowSignQRCode**



Input: 

```
tccli essbasic ChannelCreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName xx \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx \
    --FlowEffectiveDay 0 \
    --TemplateId xx \
    --MaxFlowNum 0 \
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

