**Example 1: 查询云盘扩容到200G的价格**

查询云盘扩容到200G的价格

Input: 

```
tccli cbs InquiryPriceResizeDisk --cli-unfold-argument  \
    --DiskId disk-dw0bbzws \
    --DiskSize 200
```

Output: 
```
{
    "Response": {
        "RequestId": "138749c3-94a5-426e-8621-37c4b228951c",
        "DiskPrice": {
            "UnitPriceDiscountHigh": null,
            "DiscountPrice": 119.95,
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
                    "DiscountPrice": 119.95,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskSpace",
                    "OriginalPrice": 428.42,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                },
                {
                    "PriceTitle": "云硬盘性能包",
                    "DiscountPrice": 0.0,
                    "ChargeUnit": null,
                    "UnitPriceHigh": null,
                    "OriginalPriceHigh": null,
                    "PriceName": "DiskExtraPerformance",
                    "OriginalPrice": 0.0,
                    "UnitPriceDiscountHigh": null,
                    "UnitPriceDiscount": null,
                    "DiscountPriceHigh": null,
                    "UnitPrice": null
                }
            ],
            "UnitPriceHigh": null,
            "OriginalPriceHigh": null,
            "ChargeUnit": null,
            "OriginalPrice": 428.42,
            "UnitPriceDiscount": null,
            "DiscountPriceHigh": null,
            "UnitPrice": null
        }
    }
}
```

