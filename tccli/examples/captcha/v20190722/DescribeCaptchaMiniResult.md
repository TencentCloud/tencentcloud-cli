**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniResult --cli-unfold-argument  \
    --UserIp 127.0.0.1 \
    --CaptchaAppId 201111111 \
    --Ticket xxxx \
    --AppSecretKey xxxxxx \
    --CaptchaType 9
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

