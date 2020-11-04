**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniResult --cli-unfold-argument  \
    --CaptchaType 9\
    --Ticket xxxx\
    --UserIp 127.0.0.1\
    --CaptchaAppId 201111111\
    --AppSecretKey xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "a0b3a098-b8f6-4001-764b-47f3843249db",
        "CaptchaCode": 8,
        "CaptchaMsg": "ticket expired"
    }
}
```

