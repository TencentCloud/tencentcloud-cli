**Example 1: 续费实例询价-成功返回**

续费实例询价

Input: 

```
tccli lighthouse InquirePriceRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds lhins-iqrj7783
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "Currency": "CNY",
                "OriginalBundlePrice": 50,
                "OriginalPrice": 50,
                "Discount": 40,
                "DiscountPrice": 20
            }
        },
        "DataDiskPriceSet": [],
        "InstancePriceDetailSet": [
            {
                "InstanceId": "lhins-iqrj7783",
                "InstancePrice": {
                    "Currency": "CNY",
                    "OriginalBundlePrice": 50,
                    "OriginalPrice": 50,
                    "Discount": 40,
                    "DiscountPrice": 20
                },
                "DiscountDetail": [
                    {
                        "TimeSpan": 1,
                        "TimeUnit": "m",
                        "Discount": 40,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "ActivityDiscount": 40,
                            "FinalDiscount": 40,
                            "DiscountType": "activity"
                        },
                        "TotalCost": 50,
                        "RealTotalCost": 20
                    },
                    {
                        "TimeSpan": 2,
                        "TimeUnit": "m",
                        "Discount": 30,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "ActivityDiscount": 30,
                            "FinalDiscount": 30,
                            "DiscountType": "activity"
                        },
                        "TotalCost": 100,
                        "RealTotalCost": 30
                    },
                    {
                        "TimeSpan": 3,
                        "TimeUnit": "m",
                        "Discount": 25,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "ActivityDiscount": 25,
                            "FinalDiscount": 25,
                            "DiscountType": "activity"
                        },
                        "TotalCost": 150,
                        "RealTotalCost": 37.5
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
                    }
                ]
            }
        ],
        "TotalPrice": {
            "OriginalPrice": 50,
            "DiscountPrice": 20
        },
        "RequestId": "22e25e9c-a1d2-4a82-aca0-6fd9e18f3df2"
    }
}
```

