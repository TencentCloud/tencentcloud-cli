**Example 1: CreateMultiFlowSignQRCode**

创建一码多扫流程签署二维码

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName 测试合同 \
    --MaxFlowNum 0 \
    --FlowEffectiveDay 0 \
    --Operator.UserId userId \
    --TemplateId templateid \
    --QrEffectiveDay 0 \
    --CallbackUrl 
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "QrCodeUrl": "http://www.qrcode.com/url/qrcode",
            "ExpiredTime": 5,
            "QrCodeId": "qr_code_id"
        },
        "SignUrls": {
            "EffectiveTime": "",
            "HttpSignUrl": "http://www.qrcode.com/url/HttpSignUrl",
            "AppSignUrl": "/Pages/xxxxxx"
        },
        "RequestId": "s19873636434111"
    }
}
```

