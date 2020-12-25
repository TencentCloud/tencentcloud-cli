**Example 1: 500G HSSD 额外购买200M性能询价**



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
        "RequestId": "55db49cf-b9d7-da27-825b-3232332eeewezxdsdrdew",
        "DiskPrice": {
            "DiscountPrice": -192.06,
            "UnitPrice": null,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": null,
            "OriginalPrice": -192.06,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": null,
            "ChargeUnit": null
        }
    }
}
```

