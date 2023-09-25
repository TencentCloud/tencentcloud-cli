**Example 1: 创建指合同流程签署二维码失败-模板不支持**

如果模板不符合以下以下任意一个条件
1. 模板中配置的签署顺序是无序
2. B端企业的签署方式是静默签署
3. B端企业是非首位签署
则创建二维码失败，返回错误信息

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName 测试合同 \
    --MaxFlowNum 100 \
    --QrEffectiveDay 7 \
    --FlowEffectiveDay 7 \
    --Operator.UserId yDRCLUU******wg0vjoimj \
    --TemplateId yDRS4U******xmzsIAR
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

**Example 2: 创建指定用户的的合同流程签署二维码**

创建一码多扫流程签署二维码，指定固定的用户才能扫码签署。

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.UserId yDRCLUU******wg0vjoimj \
    --FlowName 测试合同 \
    --TemplateId yDRS4U******TmzsIAR \
    --Restrictions.0.Name 张三 \
    --Restrictions.0.Mobile 188******** \
    --Restrictions.1.Name 李四 \
    --Restrictions.1.Mobile 189********
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "QrCodeUrl": "https://res.ess.tencent.cn/mp-gate/release/CHANNEL_CONTRACT_COVER/xxx",
            "ExpiredTime": 1693814798,
            "QrCodeId": "yDRS****jEuBzwyiofZ"
        },
        "SignUrls": {
            "EffectiveTime": "2022-08-05 15:55:01",
            "HttpSignUrl": "https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?where=mini&from=MSG&to=CHANNEL_CONTRACT_COVER&xxx",
            "AppSignUrl": "pages/guide?from=default&where=mini&autoJumpBack=true&to=CHANNEL_CONTRACT_COVER&xxx"
        },
        "RequestId": "s198*****111"
    }
}
```

**Example 3: 创建有数量或时间限制的合同流程签署二维码**

创建一码多扫流程签署二维码，设置该二维码在7天内有效，并将最大合同流程签署数量限制为100份。
设定签署合同的有效期为7天。

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --FlowName 测试合同 \
    --MaxFlowNum 100 \
    --QrEffectiveDay 7 \
    --FlowEffectiveDay 7 \
    --Operator.UserId yDRCLUU******wg0vjoimj \
    --TemplateId yDRS4U******TmzsIAR
```

Output: 
```
{
    "Response": {
        "QrCode": {
            "QrCodeUrl": "https://res.ess.tencent.cn/mp-gate/release/CHANNEL_CONTRACT_COVER/xxx",
            "ExpiredTime": 1693814798,
            "QrCodeId": "yDRS****jEuBzwyiofZ"
        },
        "SignUrls": {
            "EffectiveTime": "2022-08-05 15:55:01",
            "HttpSignUrl": "https://res.ess.tencent.cn/cdn/h5-activity/jump-mp.html?where=mini&from=MSG&to=CHANNEL_CONTRACT_COVER&xxx",
            "AppSignUrl": "pages/guide?from=default&where=mini&autoJumpBack=true&to=CHANNEL_CONTRACT_COVER&xxx"
        },
        "RequestId": "s198*****111"
    }
}
```

**Example 4: 创建指定了签署方签名方式的签署二维码**

1. 使用B2C模板 yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ 创建了一个签署二维码。

2.指定RecipientId 为 yDRscUUgyg3zr9vfUyJ8QKwCN7z9YcOh 的签署人在签名时可以手写（HANDWRITE） 或者使用系统签名 (SYSTEM_ESIGN)。

3.指定RecipientId 为 yDwJNUUckpkojrmqUxTFHk0yndh70CpW 的签署人在签名时只能使用AI智能识别手写签名（OCR_ESIGN）。

Input: 

```
tccli ess CreateMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowEffectiveDay 7 \
    --QrEffectiveDay 7 \
    --MaxFlowNum 5 \
    --TemplateId yDRscUUgyg1zr7wnUyJ8QMwwnHc4OOcQ \
    --FlowName 示例合同-通过二维码发起 \
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
            "QrCodeId": "yDwJNUUckpkoj9mdUIJN2kC7XWFFaSuR",
            "QrCodeUrl": "https://dyn.test.ess.tencent.cn/imgs/multiSignQrCodes/QrCode/yDwJNUUckpkoj9mdUIJN2kC7XWFFaSuR.png"
        },
        "RequestId": "s1695178926924585393",
        "SignUrls": {
            "AppSignUrl": "pages/guide?from=default&where=mini&autoJumpBack=true&to=CHANNEL_CONTRACT_COVER&qrCodeId=yDwJNUUckpkoj9mdUIJN2kC7XWFFaSuR&expiredTime=1695783727",
            "EffectiveTime": "",
            "HttpSignUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?where=mini&from=MSG&to=CHANNEL_CONTRACT_COVER&qrCodeId=yDwJNUUckpkoj9mdUIJN2kC7XWFFaSuR&expiredTime=1695783727"
        }
    }
}
```

