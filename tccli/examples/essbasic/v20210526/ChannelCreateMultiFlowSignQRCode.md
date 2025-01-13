**Example 1: 创建一码多签签署码失败-模板不支持**

如果模板不符合以下以下任意一个条件 
1. 模板中配置的签署顺序是无序 
2. B端企业的签署方式是静默签署 
3. B端企业是非首位签署 则创建二维码失败，返回错误信息


Input: 

```
tccli essbasic ChannelCreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName 通过签署二维码创建的示例合同 \
    --Agent.ProxyOperator.OpenId proxy-operator-openid \
    --Agent.ProxyOrganizationOpenId proxy-org-openid \
    --Agent.AppId yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ \
    --FlowEffectiveDay 7 \
    --TemplateId yDRvzUUgygqj42ouUuO4zjEueBrK5MeV \
    --MaxFlowNum 100 \
    --QrEffectiveDay 7
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.QrCodeTemplateId",
            "Message": "二维码生成失败，模板未满足生成二维码"
        },
        "RequestId": "s169*****0872"
    }
}
```

**Example 2: 创建有数量或时间限制的一码多签签署码**

创建一码多扫流程签署二维码，设置该二维码在7天内有效，并将最大合同流程签署数量限制为100份。 设定签署合同的有效期为7天。


Input: 

```
tccli essbasic ChannelCreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName 通过签署二维码创建的示例合同 \
    --Agent.ProxyOperator.OpenId proxy-operator-openid \
    --Agent.ProxyOrganizationOpenId proxy-org-openid \
    --Agent.AppId yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ \
    --FlowEffectiveDay 7 \
    --TemplateId yDRvzUUgygqj42ouUuO4zjEueBrK5MeV \
    --MaxFlowNum 100 \
    --QrEffectiveDay 7
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "ExpiredTime": 1695783727,
            "QrCodeId": "yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR",
            "QrCodeUrl": "https://dyn.test.ess.tencent.cn/imgs/multiSignQrCodes/QrCode/yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR.png",
            "WeixinQrCodeUrl": "https://file.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=a976edda49eacc2b264c2df468c30fcd69023cd782421bdbedddf8a95c7859d4467844c38fb9ea20b47d4b2f89396717f8deac5dcb25f32d718f0c13b48f53a2f6f69096b3b301aad56de87d7a8499fe374e5e2891dd778bb0c82394640fe124be22c63ba4e022a046cbc298006d3341"
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

**Example 3: 创建指定了签署方签名方式的一码多签签署码**

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
    --FlowName 通过签署二维码创建的示例合同 \
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
            "QrCodeUrl": "https://dyn.test.ess.tencent.cn/imgs/multiSignQrCodes/QrCode/yDwJNUUckpkoj0mdUIJN2kC3XWFFaSuR.png",
            "WeixinQrCodeUrl": "https://file.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=a976edda49eacc2b264c2df468c30fcd69023cd782421bdbedddf8a95c7859d4467844c38fb9ea20b47d4b2f89396717f8deac5dcb25f32d718f0c13b48f53a2f6f69096b3b301aad56de87d7a8499fe374e5e2891dd778bb0c82394640fe124be22c63ba4e022a046cbc298006d3341"
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

