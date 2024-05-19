**Example 1: 示例1**

示例1

Input: 

```
tccli csip DescribePayInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AutoRenew": 0,
        "CreateTime": "2023-08-03 14:46:52",
        "ExpireTime": "2023-09-03 14:46:52",
        "OrderInfoAll": [
            {
                "Key": "Order",
                "OrderInfo": {
                    "AutoRenew": 0,
                    "CreateTime": "2023-08-03 14:46:52",
                    "ExpireTime": "2023-09-03 14:46:52",
                    "PayMode": 1,
                    "QuotaList": [
                        {
                            "QuotaKey": "LogAnalyticalQuantity",
                            "QuotaNum": 10000,
                            "QuotaUsed": 0
                        },
                        {
                            "QuotaKey": "AssetScanNum",
                            "QuotaNum": 4800,
                            "QuotaUsed": 0
                        },
                        {
                            "QuotaKey": "OrganizationAccountNum",
                            "QuotaNum": 0,
                            "QuotaUsed": 0
                        },
                        {
                            "QuotaKey": "OrganizationAccountNumLimit",
                            "QuotaNum": 0,
                            "QuotaUsed": 0
                        },
                        {
                            "QuotaKey": "ScanTaskNum",
                            "QuotaNum": 50,
                            "QuotaUsed": 0
                        }
                    ],
                    "ResourceId": "csip-87628fb3-31c9-11ee-bc59-525400e30ac2",
                    "Status": 0,
                    "TimeSpan": 1,
                    "TimeUnit": "m",
                    "TrailNum": 0,
                    "TrailStatus": 0,
                    "UserLevel": 5,
                    "Version": "Ultimate"
                }
            }
        ],
        "PayMode": 0,
        "QuotaList": [
            {
                "QuotaKey": "LogAnalyticalQuantity",
                "QuotaNum": 10000,
                "QuotaUsed": 0
            },
            {
                "QuotaKey": "AssetScanNum",
                "QuotaNum": 4800,
                "QuotaUsed": 3699
            },
            {
                "QuotaKey": "OrganizationAccountNum",
                "QuotaNum": 0,
                "QuotaUsed": 0
            },
            {
                "QuotaKey": "OrganizationAccountNumLimit",
                "QuotaNum": 0,
                "QuotaUsed": 0
            },
            {
                "QuotaKey": "ScanTaskNum",
                "QuotaNum": 50,
                "QuotaUsed": 0
            }
        ],
        "RequestId": "dca73c22-5ae8-4d63-895d-fbbcbcb72fcb",
        "ResourceId": "",
        "Status": 0,
        "TimeSpan": 0,
        "TimeUnit": "",
        "TrailNum": 0,
        "TrailStatus": 0,
        "UserLevel": 5,
        "Version": "Ultimate"
    }
}
```

