**Example 1: 查询套餐折扣-成功返回**

查询套餐折扣

Input: 

```
tccli lighthouse DescribeBundleDiscount --cli-unfold-argument  \
    --BundleId bundle2022_gen_01
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
                "Discount": 85,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 85,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 85,
                    "DiscountType": "common"
                },
                "TotalCost": 600,
                "RealTotalCost": 510
            },
            {
                "TimeSpan": 24,
                "TimeUnit": "m",
                "Discount": 85,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 85,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 85,
                    "DiscountType": "common"
                },
                "TotalCost": 1200,
                "RealTotalCost": 1020
            },
            {
                "TimeSpan": 36,
                "TimeUnit": "m",
                "Discount": 85,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 85,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 85,
                    "DiscountType": "common"
                },
                "TotalCost": 1800,
                "RealTotalCost": 1530
            },
            {
                "TimeSpan": 48,
                "TimeUnit": "m",
                "Discount": 85,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 85,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 85,
                    "DiscountType": "common"
                },
                "TotalCost": 2400,
                "RealTotalCost": 2040
            },
            {
                "TimeSpan": 60,
                "TimeUnit": "m",
                "Discount": 85,
                "PolicyDetail": {
                    "UserDiscount": 100,
                    "CommonDiscount": 85,
                    "ActivityDiscount": 100,
                    "FinalDiscount": 85,
                    "DiscountType": "common"
                },
                "TotalCost": 3000,
                "RealTotalCost": 2550
            }
        ],
        "RequestId": "859918e4-78c9-4aa5-a2fc-c2e00fea4d33"
    }
}
```

