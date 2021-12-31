**Example 1: 新购磁盘询价**



Input: 

```
tccli lighthouse InquirePriceCreateDisks --cli-unfold-argument  \
    --DiskSize 20 \
    --DiskType CLOUD_SSD \
    --DiskChargePrepaid.Period 1
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

