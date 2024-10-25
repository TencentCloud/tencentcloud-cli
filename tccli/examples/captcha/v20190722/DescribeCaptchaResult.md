**Example 1: 请求和返回示例**

票据校验

Input: 

```
tccli captcha DescribeCaptchaResult --cli-unfold-argument  \
    --CaptchaAppId 199999164 \
    --CaptchaType 9 \
    --NeedGetCaptchaTime 1 \
    --Randstr @Vki \
    --UserIp 127.0.0.1 \
    --Ticket tr03XaCUZPAlPdIMqv17yvcfdXCzkqvLE09AbCA4ghlWfD8hkySfbU2TZVCyoOCjNI84pAYEMopKv7Uh8XwQDSE9DC0xJpXVC7kmlPENlbFINs_N937qkoEmU6Pl8e-9EkFQzvrrwsZOTKQ* \
    --AppSecretKey E4kwK9AcXQMHkktiItyMEyQPn
```

Output: 
```
{
    "Response": {
        "CaptchaCode": 0,
        "CaptchaMsg": "not valid",
        "EvilLevel": 0,
        "GetCaptchaTime": 1729583235,
        "SubmitCaptchaTime": 1729583239,
        "EvilBitmap": 0,
        "RequestId": "7c370964-7deb-4008-8b29-47e87e60c1e0"
    },
    "retcode": 0,
    "retmsg": "success"
}
```

