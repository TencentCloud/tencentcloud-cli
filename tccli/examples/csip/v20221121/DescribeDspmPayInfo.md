**Example 1: 获取dspm购买信息**



Input: 

```
tccli csip DescribeDspmPayInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppID": 251237296,
        "AssetNum": 9,
        "AutoRenew": 0,
        "BeginTime": "2025-11-27 16:09:30",
        "BetaEndTime": "",
        "EndTime": "2025-12-27 16:09:30",
        "InquireData": [
            {
                "Name": "sv_soccloud_dspm_exp_1in",
                "Value": 6
            },
            {
                "Name": "sv_soccloud_dspm_exp_1t",
                "Value": 2
            },
            {
                "Name": "sv_soccloud_dspm_package_pro",
                "Value": 1
            }
        ],
        "IsSelfBuy": 1,
        "IsShareToOther": 0,
        "LogStorage": 3.1,
        "NickName": "",
        "OrderStatus": 1,
        "PayMode": 1,
        "RequestId": "61d76fce-c5ed-4e41-9c49-aa33cadb19e2",
        "ResourceId": "dspm-99643271",
        "TimeNow": "2025-12-01 10:43:45",
        "TimeSpan": 1,
        "TimeUnit": "m",
        "Uin": "700000579945",
        "UsedAssetNum": 0,
        "UsedLogStorage": 0
    }
}
```

**Example 2: 计费项信息**



Input: 

```
tccli csip DescribeDspmPayInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppID": 251237296,
        "AssetNum": 9,
        "AutoRenew": 0,
        "BeginTime": "2025-11-27 16:09:30",
        "BetaEndTime": "",
        "EndTime": "2025-12-27 16:09:30",
        "InquireData": [
            {
                "Name": "sv_soccloud_dspm_exp_1in",
                "Value": 6
            },
            {
                "Name": "sv_soccloud_dspm_exp_1t",
                "Value": 2
            },
            {
                "Name": "sv_soccloud_dspm_package_pro",
                "Value": 1
            }
        ],
        "IsSelfBuy": 1,
        "IsShareToOther": 0,
        "LogStorage": 3.1,
        "NickName": "",
        "OrderStatus": 1,
        "PayMode": 1,
        "RequestId": "61d76fce-c5ed-4e41-9c49-aa33cadb19e2",
        "ResourceId": "dspm-99643271",
        "TimeNow": "2025-12-01 10:43:45",
        "TimeSpan": 1,
        "TimeUnit": "m",
        "Uin": "700000579945",
        "UsedAssetNum": 0,
        "UsedLogStorage": 0
    }
}
```

