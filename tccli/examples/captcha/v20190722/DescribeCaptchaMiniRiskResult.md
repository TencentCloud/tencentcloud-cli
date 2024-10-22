**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniRiskResult --cli-unfold-argument  \
    --CaptchaAppId 199999164 \
    --CaptchaType 9 \
    --WeChatOpenId  \
    --SceneCode 1 \
    --UserIp 127.0.0.1 \
    --Ticket tr03z8JQftDQ5ZMteDlvkg6GbucZQTiG8dq53boJY8xJoq6PanrsicK9NOQcK6G2aXSjReWIxVvXt1Y6TXnaWvBy3k2hp_gRSwpi_ZEu3j8BUY2vuuyg-c1tZc3c8GfLdVlqJbOQ5JdAFos* \
    --AppSecretKey E4kwK9AcXQMHkktiItyMEyQPn
```

Output: 
```
{
    "Response": {
        "RequestId": "c02af4b4-f858-4fe0-6f88-ebac4b49d13d",
        "CaptchaCode": 1,
        "CaptchaMsg": "ticket verification succeeded",
        "ManageMarketingRiskValue": {
            "UserId": "",
            "PostTime": 1606977595,
            "AssociateAccount": "",
            "UserIp": "127.0.0.1",
            "RiskLevel": "pass",
            "RiskType": []
        }
    }
}
```

