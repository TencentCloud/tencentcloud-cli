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
        "RequestId": "86f40e10-8b5e-4085-8aea-6188283e38de",
        "DiskPrice": {
            "DiscountPrice": 7,
            "UnitPrice": null,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "7",
            "OriginalPrice": 7,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": "7",
            "ChargeUnit": null
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
        "RequestId": "86f40e10-8b5e-4085-8aea-6188283e38de",
        "DiskPrice": {
            "DiscountPrice": 7,
            "UnitPrice": null,
            "UnitPriceHigh": null,
            "OriginalPriceHigh": "7",
            "OriginalPrice": 7,
            "UnitPriceDiscount": null,
            "UnitPriceDiscountHigh": null,
            "DiscountPriceHigh": "7",
            "ChargeUnit": null
        }
    }
}
```

