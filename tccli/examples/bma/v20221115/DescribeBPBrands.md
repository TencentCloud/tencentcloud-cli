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
                "CompanyId": 0,
                "CompanyName": "xx",
                "BrandName": "xx",
                "Phone": "xx",
                "License": "xx",
                "LicenseStatus": 0,
                "LicenseNote": "xx",
                "Authorization": "xx",
                "AuthorizationStatus": 0,
                "AuthorizationNote": "xx",
                "Trademarks": [
                    {
                        "Trademark": "xx",
                        "TrademarkStatus": 0,
                        "TrademarkNote": "xx",
                        "TrademarkId": 0,
                        "Transfer": "xx",
                        "TransferStatus": 0,
                        "TransferNote": "xx",
                        "TrademarkName": "xx"
                    }
                ],
                "InsertTime": "xx",
                "Services": {
                    "ProtectURLCount": 0,
                    "ProtectURLExpireTime": "xx",
                    "ProtectAPPCount": 0,
                    "ProtectAPPExpireTime": "xx",
                    "ProtectOfficialAccountCount": 0,
                    "ProtectOfficialAccountExpireTime": "xx",
                    "ProtectMiniProgramCount": 0,
                    "ProtectMiniProgramExpireTime": "xx",
                    "OfflineCount": 0
                }
            }
        ],
        "NoticeStatus": 0,
        "RequestId": "xx"
    }
}
```

