**Example 1: 查询实例价格**



Input: 

```
tccli ecm DescribePriceRunInstance --cli-unfold-argument  \
    --SystemDisk.DiskSize 50 \
    --SystemDisk.DiskId "123" \
    --SystemDisk.DiskType "234" \
    --InstanceCount 2 \
    --InstanceType "SN3ne.LARGE8"
```

Output: 
```
{
    "Response": {
        "RequestId": "testreq.1634816636",
        "InstancePrice": {
            "InstancePricesPartDetail": {
                "DisksPrice": {
                    "OriginalPrice": 116,
                    "DiscountPrice": 75,
                    "Discount": 64
                },
                "MemPrice": {
                    "OriginalPrice": 8106,
                    "DiscountPrice": 5269,
                    "Discount": 65
                },
                "CpuPrice": {
                    "OriginalPrice": 12800,
                    "DiscountPrice": 8320,
                    "Discount": 65
                }
            },
            "OriginalPrice": 21023,
            "DiscountPrice": 13665,
            "Discount": 65
        }
    }
}
```

