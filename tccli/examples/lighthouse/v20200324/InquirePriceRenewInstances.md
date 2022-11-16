**Example 1: 创建实例询价-成功返回**



Input: 

```
tccli lighthouse InquirePriceRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds lhins-atqh8y7p
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalBundlePrice": 40.0,
                "OriginalPrice": 40.0,
                "Discount": 100,
                "DiscountPrice": 40.0
            }
        },
        "DataDiskPriceSet": [
            {
                "DiskId": "lhdisk-ffyrsb6q",
                "InstanceId": "lhins-atqh8y7p",
                "OriginalDiskPrice": 7.0,
                "OriginalPrice": 7.0,
                "Discount": 100,
                "DiscountPrice": 7.0
            }
        ],
        "InstancePriceDetailSet": [
            {
                "InstanceId": "lhins-atqh8y7p",
                "InstancePrice": {
                    "OriginalBundlePrice": 40.0,
                    "OriginalPrice": 40.0,
                    "Discount": 100,
                    "DiscountPrice": 40.0
                }
            }
        ],
        "RequestId": "0151123a-c99c-4eda-b267-2d9800b977dc"
    }
}
```

