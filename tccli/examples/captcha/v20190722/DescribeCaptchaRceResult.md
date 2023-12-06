**Example 1: 成功结果示例**



Input: 

```
tccli captcha DescribeCaptchaRceResult --cli-unfold-argument  \
    --CaptchaType 1 \
    --Ticket abc \
    --UserIp abc \
    --BusinessId 1 \
    --SceneId 1 \
    --MacAddress abc \
    --Imei abc \
    --Randstr abc \
    --CaptchaAppId 1 \
    --AppSecretKey abc \
    --NeedGetCaptchaTime 0
```

Output: 
```
{
    "Response": {
        "CaptchaCode": 0,
        "CaptchaMsg": "abc",
        "EvilLevel": 0,
        "GetCaptchaTime": 0,
        "EvilBitmap": 0,
        "SubmitCaptchaTime": 0,
        "RceResult": {
            "UserId": "abc",
            "PostTime": 0,
            "AssociateAccount": "abc",
            "UserIp": "abc",
            "RiskLevel": "abc",
            "RiskType": [
                0
            ],
            "ConstId": "abc",
            "RiskInformation": "abc"
        },
        "RequestId": "abc"
    }
}
```

