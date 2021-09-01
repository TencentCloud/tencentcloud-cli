**Example 1: 查询套餐折扣-成功返回**



Input: 

```
tccli lighthouse DescribeBundleDiscount --cli-unfold-argument  \
    --BundleId bundle_bw_small1_1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountDetail": [
            {
                "TimeSpan": 1,
                "TimeUnit": "m",
                "TotalCost": 60.0,
                "RealTotalCost": 39.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 2,
                "TimeUnit": "m",
                "TotalCost": 120.0,
                "RealTotalCost": 78.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 3,
                "TimeUnit": "m",
                "TotalCost": 180.0,
                "RealTotalCost": 117.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 4,
                "TimeUnit": "m",
                "TotalCost": 240.0,
                "RealTotalCost": 156.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 5,
                "TimeUnit": "m",
                "TotalCost": 300.0,
                "RealTotalCost": 195.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 6,
                "TimeUnit": "m",
                "TotalCost": 360.0,
                "RealTotalCost": 234.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 7,
                "TimeUnit": "m",
                "TotalCost": 420.0,
                "RealTotalCost": 273.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 8,
                "TimeUnit": "m",
                "TotalCost": 480.0,
                "RealTotalCost": 312.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 9,
                "TimeUnit": "m",
                "TotalCost": 540.0,
                "RealTotalCost": 351.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 10,
                "TimeUnit": "m",
                "TotalCost": 600.0,
                "RealTotalCost": 390.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 11,
                "TimeUnit": "m",
                "TotalCost": 660.0,
                "RealTotalCost": 429.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 12,
                "TimeUnit": "m",
                "TotalCost": 720.0,
                "RealTotalCost": 468.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 24,
                "TimeUnit": "m",
                "TotalCost": 1440.0,
                "RealTotalCost": 936.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 36,
                "TimeUnit": "m",
                "TotalCost": 2160.0,
                "RealTotalCost": 1404.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 48,
                "TimeUnit": "m",
                "TotalCost": 2880.0,
                "RealTotalCost": 1872.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            },
            {
                "TimeSpan": 60,
                "TimeUnit": "m",
                "TotalCost": 3600.0,
                "RealTotalCost": 2340.0,
                "Discount": 65,
                "PolicyDetail": {
                    "UserDiscount": 65,
                    "CommonDiscount": 100,
                    "FinalDiscount": 65
                }
            }
        ],
        "RequestId": "60b86db7-06ce-4ddd-95b2-6a94d5a894c0"
    }
}
```

