**Example 1: 扩容询价**

扩容询价

Input: 

```
tccli emr InquiryPriceScaleOutInstance --cli-unfold-argument  \
    --TimeSpan 3600 \
    --InstanceId emr-3ida6zmi \
    --CoreCount 1 \
    --ZoneId 100003 \
    --PayMode 0 \
    --Currency CNY \
    --TaskCount 0 \
    --TimeUnit s \
    --RouterCount 0
```

Output: 
```
{
    "Response": {
        "DiscountCost": "0.65",
        "MultipleEmrPrice": [
            {
                "DiscountCost": "0.65",
                "OriginalCost": "1.21",
                "PriceSpec": {
                    "Cpu": 4,
                    "DiskCnt": 0,
                    "DiskNum": 0,
                    "DiskSize": 200,
                    "DiskType": "CLOUD_HSSD",
                    "InstanceType": "S6.LARGE8",
                    "LocalDiskNum": 0,
                    "MemSize": 8192,
                    "MultiDisks": [],
                    "RootSize": 70,
                    "Spec": "CVM.S6",
                    "StorageType": 6,
                    "Tags": null
                },
                "SupportSpotPaid": true,
                "Unit": "s"
            }
        ],
        "OriginalCost": "1.21",
        "PriceSpec": {
            "Cpu": 4,
            "DiskCnt": 0,
            "DiskNum": 0,
            "DiskSize": 200,
            "DiskType": "CLOUD_HSSD",
            "InstanceType": "S6.LARGE8",
            "LocalDiskNum": 0,
            "MemSize": 8192,
            "MultiDisks": [],
            "RootSize": 70,
            "Spec": "CVM.S6",
            "StorageType": 6,
            "Tags": null
        },
        "RequestId": "e0acae32-c70d-4d32-80bd-b2e528a33026",
        "Unit": "s"
    }
}
```

