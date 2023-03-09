**Example 1: 发送注册短信验证码**



Input: 

```
tccli account SendSmsVerifyCode --cli-unfold-argument  \
    --CountryCode 86 \
    --PhoneNumber 13211111111 \
    --ClientIP 192.168.1.1 \
    --Lang zh
```

Output: 
```
{
    "Response": {
        "RequestId": "131d2a2d-80b2-47f0-b7d4-673bf0ce22ac"
    }
}
```

