**Example 1: 成功结果示例**



Input: 

```
tccli captcha DescribeCaptchaRceResult --cli-unfold-argument  \
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
        "CaptchaMsg": "success",
        "EvilLevel": 0,
        "GetCaptchaTime": 1729583235,
        "EvilBitmap": 0,
        "SubmitCaptchaTime": 1729583239,
        "RceResult": {
            "UserId": "700000888643",
            "PostTime": 0,
            "AssociateAccount": "",
            "UserIp": "127.0.0.1",
            "RiskLevel": "1",
            "RiskType": [
                0
            ],
            "ConstId": "1",
            "RiskInformation": ""
        },
        "RequestId": "75eabc9e-2aab-46fb-b4fc-44fc6abda074"
    }
}
```

