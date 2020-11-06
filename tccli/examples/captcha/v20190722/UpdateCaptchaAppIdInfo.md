**Example 1: 请求和返回示例**



Input: 

```
tccli captcha UpdateCaptchaAppIdInfo --cli-unfold-argument  \
    --CaptchaAppId 2054955025 \
    --AppName 111 \
    --DomainLimit 111.com \
    --SceneType 1 \
    --CapType 14 \
    --EvilInterceptGrade 100 \
    --SmartVerify 0 \
    --SmartEngine 0 \
    --SchemeColor #1a79ff \
    --CaptchaLanguage 2052 \
    --MailAlarm null \
    --TopFullScreen 0 \
    --TrafficThreshold 0
```

Output: 
```
{
    "Response": {
        "RequestId": "80115345-6be7-48c9-bbdf-b9c6c9b1e111",
        "CaptchaCode": 0,
        "CaptchaMsg": "OK"
    }
}
```

