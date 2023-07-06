**Example 1: ChannelCreateMultiFlowSignQRCode**

ChannelCreateMultiFlowSignQRCode

Input: 

```
tccli essbasic ChannelCreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test \
    --FlowEffectiveDay 0 \
    --TemplateId test \
    --MaxFlowNum 0 \
    --QrEffectiveDay 0 \
    --CallbackUrl test
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "QrCodeUrl": "test",
            "ExpiredTime": 5,
            "QrCodeId": "test"
        },
        "SignUrls": {
            "EffectiveTime": "test",
            "HttpSignUrl": "test",
            "AppSignUrl": "test"
        },
        "RequestId": "test"
    }
}
```

