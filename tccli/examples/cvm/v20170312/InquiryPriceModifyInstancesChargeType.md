**Example 1: 切换实例的计费模式询价**

本示例用于切换一个实例的计费模式询价。

Input: 

```
tccli cvm InquiryPriceModifyInstancesChargeType --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --InstanceIds ins-r8hr2upy \
    --InstanceChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 720,
                "DiscountPrice": 720
            }
        },
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

