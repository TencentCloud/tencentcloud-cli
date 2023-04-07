**Example 1: 请求和返回示例**

票据校验

Input: 

```
tccli captcha DescribeCaptchaResult --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --CaptchaType 9 \
    --NeedGetCaptchaTime 1 \
    --Randstr 123 \
    --UserIp 127.0.0.1 \
    --Ticket 123 \
    --AppSecretKey 123
```

Output: 
```
{
    "Response": {
        "CaptchaCode": 0,
        "CaptchaMsg": "not valid",
        "EvilLevel": 0,
        "GetCaptchaTime": 0,
        "SubmitCaptchaTime": 0,
        "EvilBitmap": 0,
        "RequestId": "123"
    },
    "retcode": 0,
    "retmsg": "success"
}
```

