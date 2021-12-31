**Example 1: 查询云硬盘折扣信息**



Input: 

```
tccli lighthouse DescribeDiskDiscount --cli-unfold-argument  \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 50
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
                "TotalCost": 15.0,
                "RealTotalCost": 15.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 2,
                "TimeUnit": "m",
                "TotalCost": 30.0,
                "RealTotalCost": 30.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 3,
                "TimeUnit": "m",
                "TotalCost": 45.0,
                "RealTotalCost": 45.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 4,
                "TimeUnit": "m",
                "TotalCost": 60.0,
                "RealTotalCost": 60.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 5,
                "TimeUnit": "m",
                "TotalCost": 75.0,
                "RealTotalCost": 75.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 6,
                "TimeUnit": "m",
                "TotalCost": 90.0,
                "RealTotalCost": 90.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 7,
                "TimeUnit": "m",
                "TotalCost": 105.0,
                "RealTotalCost": 105.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 8,
                "TimeUnit": "m",
                "TotalCost": 120.0,
                "RealTotalCost": 120.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 9,
                "TimeUnit": "m",
                "TotalCost": 135.0,
                "RealTotalCost": 135.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 10,
                "TimeUnit": "m",
                "TotalCost": 150.0,
                "RealTotalCost": 150.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 11,
                "TimeUnit": "m",
                "TotalCost": 165.0,
                "RealTotalCost": 165.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 12,
                "TimeUnit": "m",
                "TotalCost": 180.0,
                "RealTotalCost": 180.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 24,
                "TimeUnit": "m",
                "TotalCost": 360.0,
                "RealTotalCost": 360.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 36,
                "TimeUnit": "m",
                "TotalCost": 540.0,
                "RealTotalCost": 540.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 48,
                "TimeUnit": "m",
                "TotalCost": 720.0,
                "RealTotalCost": 720.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            },
            {
                "TimeSpan": 60,
                "TimeUnit": "m",
                "TotalCost": 900.0,
                "RealTotalCost": 900.0,
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "FinalDiscount": 100
                }
            }
        ],
        "RequestId": "0b8d268d-be74-4b91-b624-7a29d70cabb0"
    }
}
```

