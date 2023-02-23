**Example 1: CreateMultiFlowSignQRCode**

创建一码多扫流程签署二维码

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName xx \
    --MaxFlowNum 0 \
    --FlowEffectiveDay 0 \
    --Operator.UserId xx \
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

