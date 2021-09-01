**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaAppIdInfo --cli-unfold-argument  \
    --CaptchaAppId 211111111
```

Output: 
```
{
    "Response": {
        "SchemeColor": "#1a79ff",
        "SceneType": 1,
        "EvilInterceptGrade": 0,
        "SmartVerify": 0,
        "SmartEngine": 1,
        "CapType": 13,
        "AppName": "小程序短信验证",
        "DomainLimit": "",
        "TrafficThreshold": 0,
        "TopFullScreen": 0,
        "RequestId": "956f01e4-86e3-4b12-a1cd-1f668f71a121",
        "CaptchaCode": 0,
        "CaptchaMsg": "",
        "Language": 2052,
        "MailAlarm": null,
        "EncryptKey": "*******"
    }
}
```

