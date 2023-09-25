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

**Example 2: 创建指定了签署方签名方式的签署二维码**

1.使用B2C模板 yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ 创建了一个签署二维码。
2.指定RecipientId 为 yDRscUUgyg3zr9vfUyJ8QKwCN7z9YcOh 的签署人在签名时可以手写（HANDWRITE） 或者使用系统签名 (SYSTEM_ESIGN)。
3.指定RecipientId 为 yDwJNUUckpkojrmqUxTFHk0yndh70CpW 的签署人在签名时只能使用AI智能识别手写签名（OCR_ESIGN）。

Input: 

```
tccli essbasic ChannelCreateMultiFlowSignQRCode --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId proxy-operator-openid \
    --Agent.ProxyOrganizationOpenId proxy-org-openid \
    --Agent.AppId yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ \
    --TemplateId yDRvzUUgygqj42ouUuO4zjEueBrK5MeV \
    --FlowName 通过签署二维码创建的实力合同 \
    --FlowEffectiveDay 5 \
    --QrEffectiveDay 7 \
    --MaxFlowNum 100 \
    --ApproverComponentLimitTypes.0.RecipientId yDRscUUgyg3zr9vfUyJ8QKwCN7z9YcOh \
    --ApproverComponentLimitTypes.0.Values HANDWRITE SYSTEM_ESIGN \
    --ApproverComponentLimitTypes.1.RecipientId yDwJNUUckpkojrmqUxTFHk0yndh70CpW \
    --ApproverComponentLimitTypes.1.Values OCR_ESIGN
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "ExpiredTime": 1695783727,
            "QrCodeId": "yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR",
            "QrCodeUrl": "https://dyn.test.ess.tencent.cn/imgs/multiSignQrCodes/QrCode/yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR.png"
        },
        "RequestId": "s1695178926924585393",
        "SignUrls": {
            "AppSignUrl": "pages/guide?from=default&where=mini&autoJumpBack=true&to=CHANNEL_CONTRACT_COVER&qrCodeId=yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR&expiredTime=1695783727",
            "EffectiveTime": "",
            "HttpSignUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?where=mini&from=MSG&to=CHANNEL_CONTRACT_COVER&qrCodeId=yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR&expiredTime=1695783727"
        }
    }
}
```

