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
        "RequestId": "6c6088bc-15e6-42e5-9d73-d5e41593117e",
        "DiskPrice": {
            "DiscountPrice": null,
            "UnitPrice": 0.18,
            "UnitPriceHigh": "0.18",
            "OriginalPriceHigh": null,
            "OriginalPrice": null,
            "UnitPriceDiscount": 0.18,
            "UnitPriceDiscountHigh": "0.18",
            "DiscountPriceHigh": null,
            "ChargeUnit": "HOUR"
        }
    }
}
```

