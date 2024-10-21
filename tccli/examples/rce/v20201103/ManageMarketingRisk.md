**Example 1: ManageMarketingRisk**

使用手机号MD5请求方式

Input: 

```
tccli rce ManageMarketingRisk --cli-unfold-argument  \
    --BusinessSecurityData.Account.AccountType 10004 \
    --BusinessSecurityData.Account.OtherAccount.AccountId 3ac9aa********************526ed9 \
    --BusinessSecurityData.SceneCode e_activity_antirush \
    --BusinessSecurityData.UserIp 113.***.***.150 \
    --BusinessSecurityData.PostTime 1712841851 \
    --BusinessSecurityData.DataAuthorization.DataProviderName 某某有限公司 \
    --BusinessSecurityData.DataAuthorization.DataRecipientName 腾讯云计算（北京）有限责任公司 \
    --BusinessSecurityData.DataAuthorization.UserDataType 1 4 \
    --BusinessSecurityData.DataAuthorization.IsAuthorize 1 \
    --BusinessSecurityData.DataAuthorization.IsOrderHandling 1 \
    --BusinessSecurityData.DataAuthorization.AuthorizationTerm 1728714893 \
    --BusinessSecurityData.DataAuthorization.PrivacyPolicyLink https://www.*****.com/ \
    --BusinessSecurityData.DataAuthorization.IsPersonalData 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "UUid": "9a570741-****-****-****-****0b788232",
            "Value": {
                "AssociateAccount": "",
                "ConstId": "",
                "PostTime": 1712841851,
                "RiskInformation": null,
                "RiskLevel": "reject",
                "RiskType": [
                    201,
                    1,
                    21,
                    11,
                    2011
                ],
                "UserId": "3ac9aa********************526ed9",
                "UserIp": "113.***.***.150"
            }
        },
        "RequestId": "5d9e8c5d-****-****-****-1c0dca666edb"
    }
}
```

