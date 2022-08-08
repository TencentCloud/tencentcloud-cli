**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaResult --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --CaptchaType 9 \
    --NeedGetCaptchaTime 1 \
    --Randstr xxx \
    --UserIp 127.0.0.1 \
    --Ticket xxxx \
    --AppSecretKey xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3b61a17b-cb38-470e-802c-b6242faf81ac",
        "CaptchaCode": 1,
        "CaptchaMsg": "OK",
        "EvilLevel": 0,
        "GetCaptchaTime": 1583749870
    },
    "retcode": 0,
    "retmsg": "success"
}
```

