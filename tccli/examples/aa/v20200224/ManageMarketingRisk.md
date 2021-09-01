**Example 1: ManageMarketingRisk**



Input: 

```
tccli aa ManageMarketingRisk --cli-unfold-argument  \
    --BusinessSecurityData.Account.AccountType 2 \
    --BusinessSecurityData.Account.WeChatAccount.WeChatOpenId oz5I********************GfVv \
    --BusinessSecurityData.PostTime 1590753783 \
    --BusinessSecurityData.UserIp 127.0.0.1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": {
                "UserId": "oz5I********************GfVv",
                "UserIp": "127.0.0.1",
                "PostTime": 1590753783,
                "AssociateAccount": "",
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

