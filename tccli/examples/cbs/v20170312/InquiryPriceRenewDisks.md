**Example 1: 查询云盘续费1个月的价格**



Input: 

```
tccli cbs InquiryPriceRenewDisks --cli-unfold-argument  \
    --DiskIds disk-jwk0zvrg \
    --DiskChargePrepaids.0.Period 1
```

Output: 
```
{
    "Response": {
        "DiskPrice": {
            "DiscountPrice": 33.26,
            "OriginalPrice": 37.8
        },
        "RequestId": "7269a7c9-daa0-48aa-372a-5a1f8029a4f4"
    }
}
```

**Example 2: 续费实例时，需续费挂载的预付费云盘，使云盘与实例的到期时间对齐。**

实例当前到期时间为：2018-03-17 15:15:03，需续费一个月，调用本接口续费实例挂载的预付费云盘，使云盘与实例的到期时间对齐。

Input: 

```
tccli cbs InquiryPriceRenewDisks --cli-unfold-argument  \
    --DiskIds disk-jwk0zvrg \
    --DiskChargePrepaids.0.Period 1 \
    --DiskChargePrepaids.0.CurInstanceDeadline '2018-03-17 15:15:03'
```

Output: 
```
{
    "Response": {
        "RequestId": "f31302ca-7e60-412c-9d84-0675e09db295",
        "DiskPrice": {
            "DiscountPrice": 6.0,
            "OriginalPrice": 6.0
        }
    }
}
```

