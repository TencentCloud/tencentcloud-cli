**Example 1: ManageMarketingRisk**



Input: 

```
tccli rce ManageMarketingRisk --cli-unfold-argument  \
    --BusinessSecurityData.PostTime 1 \
    --BusinessSecurityData.Account.QQAccount.QQOpenId xx \
    --BusinessSecurityData.Account.QQAccount.AppIdUser xx \
    --BusinessSecurityData.Account.QQAccount.DeviceId xx \
    --BusinessSecurityData.Account.QQAccount.MobilePhone xx \
    --BusinessSecurityData.Account.QQAccount.AssociateAccount xx \
    --BusinessSecurityData.Account.OtherAccount.DeviceId xx \
    --BusinessSecurityData.Account.OtherAccount.MobilePhone xx \
    --BusinessSecurityData.Account.OtherAccount.AccountId xx \
    --BusinessSecurityData.Account.WeChatAccount.MobilePhone xx \
    --BusinessSecurityData.Account.WeChatAccount.WeChatAccessToken xx \
    --BusinessSecurityData.Account.WeChatAccount.WeChatSubType 1 \
    --BusinessSecurityData.Account.WeChatAccount.DeviceId xx \
    --BusinessSecurityData.Account.WeChatAccount.AssociateAccount xx \
    --BusinessSecurityData.Account.WeChatAccount.WeChatOpenId xx \
    --BusinessSecurityData.Account.WeChatAccount.RandStr xx \
    --BusinessSecurityData.Account.AccountType 1 \
    --BusinessSecurityData.CookieHash xx \
    --BusinessSecurityData.BusinessId 1 \
    --BusinessSecurityData.DeviceType 0 \
    --BusinessSecurityData.XForwardedFor xx \
    --BusinessSecurityData.UserId xx \
    --BusinessSecurityData.CheckDevice 0 \
    --BusinessSecurityData.Details.0.FieldName xx \
    --BusinessSecurityData.Details.0.FieldValue xx \
    --BusinessSecurityData.MacAddress xx \
    --BusinessSecurityData.UserAgent xx \
    --BusinessSecurityData.EmailAddress xx \
    --BusinessSecurityData.VendorId xx \
    --BusinessSecurityData.SceneCode xx \
    --BusinessSecurityData.Sponsor.SponsorDeviceNumber xx \
    --BusinessSecurityData.Sponsor.SponsorIp xx \
    --BusinessSecurityData.Sponsor.CampaignUrl xx \
    --BusinessSecurityData.Sponsor.SponsorOpenId xx \
    --BusinessSecurityData.Sponsor.SponsorPhone xx \
    --BusinessSecurityData.UserIp xx \
    --BusinessSecurityData.Referer xx \
    --BusinessSecurityData.OnlineScam.ContentRiskLevel 0 \
    --BusinessSecurityData.OnlineScam.ContentLabel xx \
    --BusinessSecurityData.OnlineScam.ContentType 0 \
    --BusinessSecurityData.OnlineScam.FraudAccount xx \
    --BusinessSecurityData.OnlineScam.FraudType 0 \
    --BusinessSecurityData.Nickname xx \
    --BusinessSecurityData.DeviceToken xx \
    --BusinessSecurityData.DeviceBusinessId 0
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
                "RiskLevel": "reject",
                "RiskType": [
                    101,
                    1,
                    2,
                    105
                ]
            },
            "UUid": "***********************"
        },
        "RequestId": "a6227506-5f00-43cf-9a4c-66fe931cefc9"
    }
}
```

