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
            "OriginalDiskPrice": 22.0,
            "OriginalPrice": 22.0,
            "Discount": 100,
            "DiscountPrice": 22.0,
            "DetailPrices": [
                {
                    "PriceName": "DiskSpace",
                    "OriginUnitPrice": 20.0,
                    "OriginalPrice": 20.0,
                    "Discount": 100,
                    "DiscountPrice": 20.0
                },
                {
                    "PriceName": "DiskBackupQuota",
                    "OriginUnitPrice": 2.0,
                    "OriginalPrice": 2.0,
                    "Discount": 100,
                    "DiscountPrice": 2.0
                }
            ]
        },
        "RequestId": "03da2972-121e-4dcc-9a10-4cbec5c8991a"
    }
}
```

