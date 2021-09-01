**Example 1: 变配询价**



Input: 

```
tccli emr InquiryPriceUpdateInstance --cli-unfold-argument  \
    --TimeUnit s \
    --TimeSpan 3600 \
    --Placement.Zone 100003 \
    --Currency CNY \
    --Placement.ProjectId 0 \
    --UpdateSpec.Memory 16 \
    --UpdateSpec.CPUCores 8 \
    --UpdateSpec.ResourceId emr-vm-a0xxx9on \
    --PayMode 0
```

Output: 
```
{
    "Response": {
        "DiscountCost": 2.01,
        "OriginalCost": 3.04,
        "RequestId": "95eb9120-0883-407c-aa5a-43b4e2c250d1",
        "TimeSpan": 3600,
        "TimeUnit": "s"
    }
}
```

