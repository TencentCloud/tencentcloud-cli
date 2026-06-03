**Example 1: 分批查询计费信息**



Input: 

```
tccli tcb DescribeBillingInfo --cli-unfold-argument  \
    --Limit 1000 \
    --Offset 30
```

Output: 
```
{
    "Response": {
        "EnvBillingInfoList": [
            {
                "CreateTime": "2021-01-20 21:18:09",
                "EnableOverrun": false,
                "EnvActivated": "no",
                "EnvCharged": "yes",
                "EnvId": "carol-test-sms-6g7zpok6eb41cdfe",
                "ExpireTime": "0000-00-00 00:00:00",
                "ExtPackageType": "",
                "FreeQuota": "free",
                "IsAlwaysFree": false,
                "IsAutoRenew": false,
                "IsolatedTime": "2022-10-25 15:42:53",
                "OrderInfo": {
                    "CreateTime": "2021-01-20 21:17:53",
                    "ExtensionId": "",
                    "Flag": "",
                    "PackageId": "",
                    "PayMode": "POSTPAID",
                    "ReqBody": "",
                    "ResourceReady": "",
                    "TranId": "20210120789001256921351",
                    "TranStatus": "4",
                    "TranType": "5",
                    "UpdateTime": "2021-01-20 21:19:40"
                },
                "PackageId": "",
                "PayMode": "POSTPAID",
                "PaymentChannel": "qcloud",
                "Status": "ISOLATE",
                "UpdateTime": "2022-10-25 15:42:53"
            }
        ],
        "Total": 10000,
        "RequestId": "cf7490af-821b-4d33-94a2-0337a67f5910"
    }
}
```

**Example 2: 查询环境列表的计费信息**



Input: 

```
tccli tcb DescribeBillingInfo --cli-unfold-argument  \
    --EnvIds stress10new0059998or-d3aa7adb44f
```

Output: 
```
{
    "Response": {
        "EnvBillingInfoList": [
            {
                "CreateTime": "2026-05-15 15:56:43",
                "EnableOverrun": false,
                "EnvActivated": "no",
                "EnvCharged": "yes",
                "EnvId": "stress10new0059998or-d3aa7adb44f",
                "ExpireTime": "2026-11-15 23:59:59",
                "ExtPackageType": "baas",
                "FreeQuota": "",
                "IsAlwaysFree": false,
                "IsAutoRenew": false,
                "IsolatedTime": "0000-00-00 00:00:00",
                "OrderInfo": {
                    "CreateTime": "",
                    "ExtensionId": "",
                    "Flag": "",
                    "PackageId": "",
                    "PayMode": "",
                    "ReqBody": "",
                    "ResourceReady": "",
                    "TranId": "",
                    "TranStatus": "",
                    "TranType": "",
                    "UpdateTime": ""
                },
                "PackageId": "baas_trial",
                "PayMode": "PREPAYMENT",
                "PaymentChannel": "miniapp",
                "Status": "NORMAL",
                "UpdateTime": "2026-05-15 15:56:43"
            }
        ],
        "Total": 10000,
        "RequestId": "68c26a28-5c00-4730-b701-5a7bc1981eae"
    }
}
```

