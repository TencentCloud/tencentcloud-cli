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
            "OriginalDiskPrice": 20.0,
            "OriginalPrice": 20.0,
            "Discount": 100,
            "DiscountPrice": 20.0,
            "DetailPrices": [
                {
                    "PriceName": "DiskSpace",
                    "OriginUnitPrice": 20.0,
                    "OriginalPrice": 20.0,
                    "Discount": 100,
                    "DiscountPrice": 20.0
                }
            ]
        },
        "RequestId": "25a4f680-0477-4f27-a494-1369eb310fe8"
    }
}
```

