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
        "OriginalCost": "abc",
        "DiscountCost": "abc",
        "Unit": "abc",
        "PriceSpec": {
            "Spec": "abc",
            "StorageType": 1,
            "DiskType": "abc",
            "RootSize": 0,
            "MemSize": 0,
            "Cpu": 0,
            "DiskSize": 0,
            "MultiDisks": [
                {
                    "DiskType": "abc",
                    "Volume": 0,
                    "Count": 0
                }
            ],
            "DiskCnt": 0,
            "InstanceType": "abc",
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "DiskNum": 0,
            "LocalDiskNum": 0
        },
        "MultipleEmrPrice": [
            {
                "OriginalCost": "abc",
                "DiscountCost": "abc",
                "Unit": "abc",
                "PriceSpec": {
                    "Spec": "abc",
                    "StorageType": 1,
                    "DiskType": "abc",
                    "RootSize": 0,
                    "MemSize": 0,
                    "Cpu": 0,
                    "DiskSize": 0,
                    "MultiDisks": [
                        {
                            "DiskType": "abc",
                            "Volume": 0,
                            "Count": 0
                        }
                    ],
                    "DiskCnt": 0,
                    "InstanceType": "abc",
                    "Tags": [
                        {
                            "TagKey": "abc",
                            "TagValue": "abc"
                        }
                    ],
                    "DiskNum": 0,
                    "LocalDiskNum": 0
                },
                "SupportSpotPaid": true
            }
        ],
        "RequestId": "abc"
    }
}
```

