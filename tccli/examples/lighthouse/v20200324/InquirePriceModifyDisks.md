**Example 1: 变配云硬盘询价**



Input: 

```
tccli lighthouse InquirePriceModifyDisks --cli-unfold-argument  \
    --DiskIds lhdisk-gqsibq9s
```

Output: 
```
{
    "Response": {
        "DiskPrice": {
            "OriginalDiskPrice": 1.99,
            "OriginalPrice": 3.61,
            "Discount": 100,
            "DiscountPrice": 3.61,
            "DetailPrices": []
        },
        "RequestId": "e0d75bac-5f87-4a72-aa6f-6211964237ec"
    }
}
```

