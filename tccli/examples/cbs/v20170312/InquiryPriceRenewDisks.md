**Example 1: 查询云盘续费1个月的价格**



Input: 

```
tccli cbs InquiryPriceRenewDisks --cli-unfold-argument  \
    --DiskChargePrepaids.0.Period 1 \
    --DiskIds disk-jwk0zvrg
```

Output: 
```
{
    "Response": {
        "RequestId": "2e7414a3-369f-4995-b708-80eb2e7414a3",
        "DiskPrice": {
            "UnitPriceDiscountHigh": null,
            "DiscountPrice": 250.0,
            "DetailPrices": [
                {
                    "PriceTitle": "云硬盘备份点配额",
                    "DiscountPrice": 0.0,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskBackupQuota",
                    "OriginalPrice": 0.0,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                },
                {
                    "PriceTitle": "云硬盘空间",
                    "DiscountPrice": 250.0,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskSpace",
                    "OriginalPrice": 500.0,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                }
            ],
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "500",
            "ChargeUnit": null,
            "OriginalPrice": 500.0,
            "UnitPriceDiscount": null,
            "DiscountPriceHigh": "250",
            "UnitPrice": null
        }
    }
}
```

**Example 2: 续费实例时，需续费挂载的预付费云盘，使云盘与实例的到期时间对齐。**

实例当前到期时间为：2018-03-17 15:15:03，需续费一个月，调用本接口续费实例挂载的预付费云盘，使云盘与实例的到期时间对齐。

Input: 

```
tccli cbs InquiryPriceRenewDisks --cli-unfold-argument  \
    --DiskChargePrepaids.0.CurInstanceDeadline 2018-03-17 15:15:03 \
    --DiskChargePrepaids.0.Period 1 \
    --DiskIds disk-jwk0zvrg
```

Output: 
```
{
    "Response": {
        "RequestId": "2e7414a3-369f-4995-b708-80eb2e7414a3",
        "DiskPrice": {
            "UnitPriceDiscountHigh": null,
            "DiscountPrice": 250,
            "DetailPrices": [
                {
                    "PriceTitle": "云硬盘备份点配额",
                    "DiscountPrice": 0,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskBackupQuota",
                    "OriginalPrice": 0,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                },
                {
                    "PriceTitle": "云硬盘空间",
                    "DiscountPrice": 250,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskSpace",
                    "OriginalPrice": 500,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                }
            ],
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "500",
            "ChargeUnit": null,
            "OriginalPrice": 500,
            "UnitPriceDiscount": null,
            "DiscountPriceHigh": "250",
            "UnitPrice": null
        }
    }
}
```

