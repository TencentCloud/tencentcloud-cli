**Example 1: 扩容询价**



Input: 

```
tccli emr InquiryPriceScaleOutInstance --cli-unfold-argument  \
    --TimeUnit s \
    --TimeSpan 3600 \
    --ZoneId 100003 \
    --PayMode 0 \
    --InstanceId emr-3ida6zmi \
    --CoreCount 1 \
    --TaskCount 0 \
    --Currency CNY \
    --RouterCount 0
```

Output: 
```
{
    "Response": {
        "DiscountCost": "77",
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
        "Unit": "1",
        "OriginalCost": "1.1",
        "RequestId": "04daa603-e1e7-4243-b25d-31e6a6736528"
    }
}
```

