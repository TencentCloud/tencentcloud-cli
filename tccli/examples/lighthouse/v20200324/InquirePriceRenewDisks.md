**Example 1: 续费磁盘询价**



Input: 

```
tccli lighthouse InquirePriceRenewDisks --cli-unfold-argument  \
    --DiskIds lhdisk-5vmz00i3 \
    --RenewDiskChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "DiskPrice": {
            "OriginalDiskPrice": 16.0,
            "OriginalPrice": 16.0,
            "Discount": 100,
            "DiscountPrice": 16.0
        },
        "RequestId": "4214ba7a-0784-4cbb-a342-e5cc288c484c"
    }
}
```

