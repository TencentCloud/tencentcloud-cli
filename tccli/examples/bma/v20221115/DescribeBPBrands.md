**Example 1: 查询品牌列表**

查询品牌列表

Input: 

```
tccli bma DescribeBPBrands --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Brands": [
            {
                "Uin": "abc",
                "CompanyId": 0,
                "CompanyName": "abc",
                "BrandName": "abc",
                "Phone": "abc",
                "License": "abc",
                "LicenseStatus": 0,
                "LicenseNote": "abc",
                "Authorization": "abc",
                "AuthorizationStatus": 0,
                "AuthorizationNote": "abc",
                "Trademarks": [
                    {
                        "Trademark": "abc",
                        "TrademarkStatus": 0,
                        "TrademarkNote": "abc",
                        "TrademarkId": 0,
                        "Transfer": "abc",
                        "TransferStatus": 0,
                        "TransferNote": "abc",
                        "TrademarkName": "abc"
                    }
                ],
                "InsertTime": "abc",
                "Services": {
                    "ProtectURLCount": 0,
                    "ProtectURLExpireTime": "abc",
                    "ProtectAPPCount": 0,
                    "ProtectAPPExpireTime": "abc",
                    "ProtectOfficialAccountCount": 0,
                    "ProtectOfficialAccountExpireTime": "abc",
                    "ProtectMiniProgramCount": 0,
                    "ProtectMiniProgramExpireTime": "abc",
                    "OfflineCount": 0
                }
            }
        ],
        "NoticeStatus": 0,
        "RequestId": "abc"
    }
}
```

