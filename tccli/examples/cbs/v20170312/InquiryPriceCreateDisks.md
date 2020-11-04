**Example 1: 查询购买6个月50G普通云盘的价格**



Input: 

```
tccli cbs InquiryPriceCreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_BASIC\
    --DiskCount 1\
    --DiskSize 50\
    --DiskChargeType PREPAID\
    --DiskChargePrepaid.Period 6
```

Output: 
```
{
    "Response": {
        "RequestId": "55e84d71-26f1-4b7c-8dc4-6bc2611d0a2411",
        "DiskPrice": {
            "DiscountPrice": 90.0,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "90",
            "OriginalPrice": 90.0,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": "90",
            "UnitPrice": null
        }
    }
}
```

**Example 2: 查询购买按小时后付费云盘价格**

查询购买一块大小100GB，云盘类型为高性能云硬盘，计费类型为按小时后付费的价格。

Input: 

```
tccli cbs InquiryPriceCreateDisks --cli-unfold-argument  \
    --DiskType CLOUD_PREMIUM\
    --DiskSize 100\
    --DiskCount 1\
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

