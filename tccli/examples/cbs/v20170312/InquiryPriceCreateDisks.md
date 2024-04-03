**Example 1: 查询购买按小时后付费云盘价格**

查询购买一块大小100GB，云盘类型为高性能云硬盘，计费类型为按小时后付费的价格。

Input: 

```
tccli cbs InquiryPriceCreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_PREMIUM \
    --DiskSize 100 \
    --DiskCount 1 \
    --DiskChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "RequestId": "55e84d71-26f1-4b7c-8dc4-6bc26d0a2411",
        "DiskPrice": {
            "DiscountPrice": null,
            "UnitPrice": 0.04,
            "UnitPriceHigh": "0.042",
            "OriginalPriceHigh": null,
            "OriginalPrice": null,
            "UnitPriceDiscount": 0.04,
            "UnitPriceDiscountHigh": "0.042",
            "DiscountPriceHigh": null,
            "ChargeUnit": "HOUR"
        }
    }
}
```

**Example 2: 查询购买1个月500G TSSD 带100M额外性能询价**



Input: 

```
tccli cbs InquiryPriceCreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_TSSD \
    --DiskCount 1 \
    --DiskSize 500 \
    --DiskChargeType PREPAID \
    --DiskChargePrepaid.Period 1 \
    --ThroughputPerformance 100
```

Output: 
```
{
    "Response": {
        "RequestId": "55e84d71-26f1-4b7c-8dc4-6bc2611d0a2411",
        "DiskPrice": {
            "DiscountPrice": 800.0,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "800",
            "OriginalPrice": 800.0,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": "800",
            "UnitPrice": null,
            "ChargeUnit": null
        }
    }
}
```

