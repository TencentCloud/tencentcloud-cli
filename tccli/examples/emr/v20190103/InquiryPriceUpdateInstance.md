**Example 1: 变配询价**



Input: 

```
tccli emr InquiryPriceUpdateInstance --cli-unfold-argument  \
    --Placement.ProjectId 0 \
    --Placement.Zone 100003 \
    --TimeSpan 3600 \
    --UpdateSpec.ResourceId emr-vm-a0xxx9on \
    --UpdateSpec.CPUCores 8 \
    --UpdateSpec.Memory 16 \
    --PayMode 0 \
    --Currency CNY \
    --TimeUnit s
```

Output: 
```
{
    "Response": {
        "DiscountCost": 2.01,
        "OriginalCost": 3.04,
        "RequestId": "95eb9120-0883-407c-aa5a-43b4e2c250d1",
        "TimeSpan": 3600,
        "TimeUnit": "s",
        "PriceDetail": [
            {
                "Formula": "(1).变配订单金额：2870.4 元[ 新配置单价3546.4*时长1*折扣100% - 旧配置单价676*时长1*折扣100%]<br/>(2).时长:1月",
                "DiscountCost": 2870.4,
                "ResourceId": "emr-vm-xxxxxxx",
                "OriginalCost": 2870.4
            }
        ]
    }
}
```

