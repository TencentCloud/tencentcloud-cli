**Example 1: 使用腾讯云短信发送登录短信**



Input: 

```
tccli tcb ModifyLoginConfig --cli-unfold-argument  \
    --EnvId **w**d***************1b7 \
    --PhoneNumberLogin True \
    --EmailLogin False \
    --UserNameLogin True \
    --AnonymousLogin True \
    --SmsVerificationConfig.Type template \
    --SmsVerificationConfig.SmsDayLimit 30 \
    --SmsVerificationConfig.TemplateProvider.Vendor TENCENT_CN \
    --SmsVerificationConfig.TemplateProvider.TemplateId *****45 \
    --SmsVerificationConfig.TemplateProvider.SdkAppId 1********7 \
    --SmsVerificationConfig.TemplateProvider.SecretId ************************************ \
    --SmsVerificationConfig.TemplateProvider.SecretKey ********************************
```

Output: 
```
{
    "Response": {
        "RequestId": "2437d6bd-5fea-442c-bcac-b23416c2b0e2"
    }
}
```

