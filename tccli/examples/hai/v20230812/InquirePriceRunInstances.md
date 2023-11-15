**Example 1: 发货询价**



Input: 

```
tccli hai InquirePriceRunInstances --cli-unfold-argument  \
    --ApplicationId app-jknfna \
    --BundleType S \
    --SystemDisk.DiskType CLOUD_PREMIUM \
    --SystemDisk.DiskSize 250 \
    --InstanceName test
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.88,
                "DiscountUnitPrice": 0.88,
                "Discount": 100.0,
                "ChargeUnit": "HOUR",
                "Amount": 1
            },
            "CloudDiskPrice": {
                "UnitPrice": 0,
                "DiscountUnitPrice": 0,
                "Discount": 0,
                "ChargeUnit": "HOUR",
                "Amount": 1
            }
        },
        "RequestId": "abc"
    }
}
```

