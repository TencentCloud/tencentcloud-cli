**Example 1: 活动防刷高级版**



Input: 

```
tccli aa QueryActivityAntiRushAdvanced --cli-unfold-argument  \
    --BusinessSecurityData.Account.AccountAccountType 2 \
    --BusinessSecurityData.Account.WeChatAccount.WeChatOpenId "oz5I2tz55hxIIFCDxIflGfVv****" \
    --BusinessSecurityData.OnlineScam.ContentLabel "Text" \
    --BusinessSecurityData.OnlineScam.ContentRiskLevel 1 \
    --BusinessSecurityData.OnlineScam.ContentType 1 \
    --BusinessSecurityData.OnlineScam.FraudType 2 \
    --BusinessSecurityData.OnlineScam.FraudAccount "55277****" \
    --BusinessSecurityData.PostTime 1590753783 \
    --BusinessSecurityData.UserIp "117.136.105.74"
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "UserId": "oz5I2tz55hxIIFCDxIflGfVv****",
                "UserIp": "117.136.105.74",
                "PostTime": 1590753783,
                "AssociateAccount": "",
                "Level": 4,
                "RiskType": [
                    101,
                    1,
                    2,
                    105
                ]
            }
        },
        "RequestId": "a6227506-5f00-43cf-9a4c-66fe931cefc9"
    }
}
```

