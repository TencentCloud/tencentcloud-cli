**Example 1: 查询云硬盘折扣信息**

查询云硬盘折扣信息

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
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "ActivityDiscount": null,
                    "FinalDiscount": 100,
                    "DiscountType": null
                },
                "TotalCost": 50,
                "RealTotalCost": 50
            },
            {
                "TimeSpan": 2,
                "TimeUnit": "m",
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "ActivityDiscount": null,
                    "FinalDiscount": 100,
                    "DiscountType": null
                },
                "TotalCost": 100,
                "RealTotalCost": 100
            },
            {
                "TimeSpan": 3,
                "TimeUnit": "m",
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "ActivityDiscount": null,
                    "FinalDiscount": 100,
                    "DiscountType": null
                },
                "TotalCost": 150,
                "RealTotalCost": 150
            },
            {
                "TimeSpan": 4,
                "TimeUnit": "m",
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "ActivityDiscount": null,
                    "FinalDiscount": 100,
                    "DiscountType": null
                },
                "TotalCost": 200,
                "RealTotalCost": 200
            },
            {
                "TimeSpan": 5,
                "TimeUnit": "m",
                "Discount": 100,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 100,
                    "ActivityDiscount": null,
                    "FinalDiscount": 100,
                    "DiscountType": null
                },
                "TotalCost": 250,
                "RealTotalCost": 250
            },
            {
                "TimeSpan": 6,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 300,
                "RealTotalCost": 264
            },
            {
                "TimeSpan": 7,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 350,
                "RealTotalCost": 308
            },
            {
                "TimeSpan": 8,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 400,
                "RealTotalCost": 352
            },
            {
                "TimeSpan": 9,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 450,
                "RealTotalCost": 396
            },
            {
                "TimeSpan": 10,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 500,
                "RealTotalCost": 440
            },
            {
                "TimeSpan": 11,
                "TimeUnit": "m",
                "Discount": 88,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 88,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 88,
                    "DiscountType": "common"
                },
                "TotalCost": 550,
                "RealTotalCost": 484
            },
            {
                "TimeSpan": 12,
                "TimeUnit": "m",
                "Discount": 83,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 83,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 83,
                    "DiscountType": "common"
                },
                "TotalCost": 600,
                "RealTotalCost": 498
            },
            {
                "TimeSpan": 24,
                "TimeUnit": "m",
                "Discount": 70,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 70,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 70,
                    "DiscountType": "common"
                },
                "TotalCost": 1200,
                "RealTotalCost": 840
            },
            {
                "TimeSpan": 36,
                "TimeUnit": "m",
                "Discount": 50,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 50,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 50,
                    "DiscountType": "common"
                },
                "TotalCost": 1800,
                "RealTotalCost": 900
            },
            {
                "TimeSpan": 48,
                "TimeUnit": "m",
                "Discount": 50,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 50,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 50,
                    "DiscountType": "common"
                },
                "TotalCost": 2400,
                "RealTotalCost": 1200
            },
            {
                "TimeSpan": 60,
                "TimeUnit": "m",
                "Discount": 50,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 50,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 50,
                    "DiscountType": "common"
                },
                "TotalCost": 3000,
                "RealTotalCost": 1500
            }
        ],
        "RequestId": "250d48df-ded8-4ce0-92f5-10c13e673d06"
    }
}
```

