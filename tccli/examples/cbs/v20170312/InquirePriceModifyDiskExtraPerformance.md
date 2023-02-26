**Example 1: 500G HSSD 额外购买200M性能询价**

500G HSSD 额外购买200M性能询价

Input: 

```
tccli cbs InquirePriceModifyDiskExtraPerformance --cli-unfold-argument  \
    --DiskId disk-dritwhhm \
    --ThroughputPerformance 200
```

Output: 
```
{
    "Response": {
        "RequestId": "2473a107-d3ee-49b6-98f1-2fa630610b85",
        "DiskPrice": {
            "DiscountPrice": 611.51,
            "UnitPrice": null,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": null,
            "OriginalPrice": 611.51,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": null,
            "ChargeUnit": null
        }
    }
}
```

