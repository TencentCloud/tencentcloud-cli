**Example 1: 扩容云硬盘询价**



Input: 

```
tccli lighthouse InquirePriceResizeDisks --cli-unfold-argument  \
    --DiskIds lhdisk-jgszqvs0 \
    --DiskSize 40
```

Output: 
```
{
    "Response": {
        "DiskPrice": {
            "OriginalDiskPrice": 7,
            "OriginalPrice": 7,
            "Discount": 100,
            "DiscountPrice": 7,
            "DetailPrices": [
                {
                    "PriceName": "DiskSpace",
                    "OriginUnitPrice": 7,
                    "OriginalPrice": 7,
                    "Discount": 100,
                    "DiscountPrice": 7
                }
            ]
        },
        "RequestId": "4aa10e72-1664-4df6-b043-a6cb92ebf069"
    }
}
```

