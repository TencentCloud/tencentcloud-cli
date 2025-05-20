**Example 1: 调整云硬盘备份点配额询价**



Input: 

```
tccli lighthouse InquirePriceModifyDisksBackupQuota --cli-unfold-argument  \
    --DiskIds lhdisk-guzg7nsa \
    --DiskBackupQuota 4
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

