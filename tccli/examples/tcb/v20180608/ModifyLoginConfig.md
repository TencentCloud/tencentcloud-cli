**Example 1: 修改环境登录配置**

使用默认云开发短信包发送登录短信

Input: 

```
tccli tcb ModifyLoginConfig --cli-unfold-argument  \
    --EnvId env-123 \
    --PhoneNumberLogin True \
    --EmailLogin True \
    --UserNameLogin False \
    --AnonymousLogin False \
    --SmsVerificationConfig.Type default \
    --SmsVerificationConfig.SmsDayLimit 30 \
    --MfaConfig.On TRUE \
    --MfaConfig.Sms TRUE \
    --MfaConfig.Email FALSE \
    --MfaConfig.RequiredBindPhone TRUE \
    --PwdUpdateStrategy.FirstLoginUpdate True \
    --PwdUpdateStrategy.PeriodUpdate True \
    --PwdUpdateStrategy.PeriodValue 6 \
    --PwdUpdateStrategy.PeriodType MONTH
```

Output: 
```
{
    "Response": {
        "RequestId": "70b8908d-5c99-4a20-be23-f84aff0bfd37"
    }
}
```

**Example 2: 修改登录配置**

使用自定义apis发送登录短信

Input: 

```
tccli tcb ModifyLoginConfig --cli-unfold-argument  \
    --EnvId env-123 \
    --PhoneNumberLogin True \
    --EmailLogin True \
    --UserNameLogin False \
    --AnonymousLogin False \
    --SmsVerificationConfig.Type apis \
    --SmsVerificationConfig.Name method_53978f9f96a35 \
    --SmsVerificationConfig.Method SendVerificationCode \
    --SmsVerificationConfig.SmsDayLimit 20 \
    --MfaConfig.On TRUE \
    --MfaConfig.Sms TRUE \
    --MfaConfig.Email FALSE \
    --MfaConfig.RequiredBindPhone TRUE \
    --PwdUpdateStrategy.FirstLoginUpdate True \
    --PwdUpdateStrategy.PeriodUpdate True \
    --PwdUpdateStrategy.PeriodValue 6 \
    --PwdUpdateStrategy.PeriodType MONTH
```

Output: 
```
{
    "Response": {
        "RequestId": "26d3461b-b116-4862-bbaf-6233d2922aca"
    }
}
```

