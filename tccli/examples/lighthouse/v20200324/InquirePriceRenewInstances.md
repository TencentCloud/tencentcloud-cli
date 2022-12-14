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
                "Discount": 100,
                "DiscountPrice": 50
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
                    "Discount": 100,
                    "DiscountPrice": 50
                },
                "DiscountDetail": [
                    {
                        "TimeSpan": 1,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
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
                            "FinalDiscount": 100
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
                            "FinalDiscount": 100
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
                            "FinalDiscount": 100
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
                            "FinalDiscount": 100
                        },
                        "TotalCost": 250,
                        "RealTotalCost": 250
                    },
                    {
                        "TimeSpan": 6,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 300,
                        "RealTotalCost": 300
                    },
                    {
                        "TimeSpan": 7,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 350,
                        "RealTotalCost": 350
                    },
                    {
                        "TimeSpan": 8,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 400,
                        "RealTotalCost": 400
                    },
                    {
                        "TimeSpan": 9,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 450,
                        "RealTotalCost": 450
                    },
                    {
                        "TimeSpan": 10,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 500,
                        "RealTotalCost": 500
                    },
                    {
                        "TimeSpan": 11,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 550,
                        "RealTotalCost": 550
                    },
                    {
                        "TimeSpan": 12,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 600,
                        "RealTotalCost": 600
                    },
                    {
                        "TimeSpan": 24,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 1200,
                        "RealTotalCost": 1200
                    },
                    {
                        "TimeSpan": 36,
                        "TimeUnit": "m",
                        "Discount": 100,
                        "PolicyDetail": {
                            "UserDiscount": 100,
                            "CommonDiscount": 100,
                            "FinalDiscount": 100
                        },
                        "TotalCost": 1800,
                        "RealTotalCost": 1800
                    }
                ]
            }
        ],
        "TotalPrice": {
            "OriginalPrice": 50,
            "DiscountPrice": 50
        },
        "RequestId": "97772a05-93ca-4856-a1f2-b4e0856ade25"
    }
}
```

