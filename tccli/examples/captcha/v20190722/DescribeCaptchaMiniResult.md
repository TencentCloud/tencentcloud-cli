**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniResult --cli-unfold-argument  \
    --UserIp 127.0.0.1 \
    --CaptchaAppId 199999164 \
    --Ticket tr03z8JQftDQ5ZMteDlvkg6GbucZQTiG8dq53boJY8xJoq6PanrsicK9NOQcK6G2aXSjReWIxVvXt1Y6TXnaWvBy3k2hp_gRSwpi_ZEu3j8BUY2vuuyg-c1tZc3c8GfLdVlqJbOQ5JdAFos* \
    --AppSecretKey E4kwK9AcXQMHkktiItyMEyQPn \
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

