**Example 1: 请求和返回示例**



Input: 

```
tccli captcha DescribeCaptchaMiniRiskResult --cli-unfold-argument  \
    --CaptchaAppId 201111111 \
    --CaptchaType 9 \
    --WeChatOpenId xxxxxx \
    --SceneCode 1 \
    --UserIp 127.0.0.1 \
    --Ticket xxxx \
    --AppSecretKey xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "c02af4b4-f858-4fe0-6f88-ebac4b49d13d",
        "CaptchaCode": 1,
        "CaptchaMsg": "ticket verification succeeded",
        "ManageMarketingRiskValue": {
            "UserId": "xxxxxxxxxxxxxxxxxxxxxxxx",
            "PostTime": 1606977595,
            "AssociateAccount": "",
            "UserIp": "127.0.0.1",
            "RiskLevel": "pass",
            "RiskType": []
        }
    }
}
```

