**Example 1: 扩容询价**



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
        "DiscountCost": "1.26",
        "PriceSpec": {
            "InstanceType": "S5",
            "DiskCnt": 1,
            "StorageType": 1,
            "DiskNum": 1,
            "DiskType": "2",
            "LocalDiskNum": 0,
            "Cpu": 0,
            "DiskSize": 100,
            "MemSize": 100,
            "RootSize": 50,
            "Spec": "S5.2XLARGE8"
        },
        "Unit": "s",
        "OriginalCost": "1.74",
        "MultipleEmrPrice": [
            {
                "DiscountCost": "1.26",
                "PriceSpec": {
                    "InstanceType": "S5",
                    "DiskCnt": 1,
                    "StorageType": 1,
                    "DiskNum": 1,
                    "DiskType": "2",
                    "LocalDiskNum": 0,
                    "Cpu": 0,
                    "DiskSize": 100,
                    "MemSize": 100,
                    "RootSize": 50,
                    "Spec": "S5.2XLARGE8"
                },
                "Unit": "s",
                "OriginalCost": "1.74"
            }
        ],
        "RequestId": "04daa603-e1e7-4243-b25d-31e6a6736528"
    }
}
```

