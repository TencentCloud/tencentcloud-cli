**Example 1: 修改云硬盘备份点配额询价**



Input: 

```
tccli cbs InquirePriceModifyDiskBackupQuota --cli-unfold-argument  \
    --DiskId disk-xxxxxxxx \
    --DiskBackupQuota 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0195b2d8-fec5-490a-ace9-579f49435e69",
        "DiskPrice": {
            "UnitPriceDiscountHigh": "0.059",
            "DiscountPrice": null,
            "UnitPriceHigh": "0.059",
            "OriginalPriceHigh": null,
            "ChargeUnit": "HOUR",
            "OriginalPrice": null,
            "UnitPriceDiscount": 0.06,
            "DiscountPriceHigh": null,
            "UnitPrice": 0.06
        }
    }
}
```

