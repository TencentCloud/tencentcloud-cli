**Example 1: 获取子账户列表**



Input: 

```
tccli cam ListMaskedSubAccounts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalNum": 1,
        "UserInfo": [
            {
                "Uid": 12062472,
                "Uin": 100023162094,
                "Name": "test_seven",
                "Remark": "",
                "CanLogin": 1,
                "PhoneNum": "",
                "CountryCode": "86",
                "PhoneFlag": 0,
                "Email": "",
                "EmailFlag": 0,
                "UserType": 3,
                "CreateTime": "2022-01-03 10:38:26",
                "IsReceiverOwner": 0,
                "SystemType": "SubAccount",
                "NeedResetPassword": 1,
                "ConsoleLogin": 0,
                "WxzsStatus": 0,
                "PermType": [],
                "IsDeleted": 0,
                "IsSelected": null,
                "HasAPIKey": null,
                "BindWework": null
            }
        ],
        "OwnerInfo": [
            {
                "Uin": 100011742865,
                "UserName": "YB",
                "CheckStatus": 0
            }
        ],
        "GroupInfo": [],
        "RequestId": "50a36793-83c2-44b5-961f-2946bca09c69"
    }
}
```

