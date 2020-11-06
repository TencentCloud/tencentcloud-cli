**Example 1: 按量付费实例调整配置询价**



Input: 

```
tccli cvm InquiryPriceResetInstance --cli-unfold-argument  \
    --InstanceId ins-fd8spnmq
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.66,
                "ChargeUnit": "HOUR",
                "UnitPriceDiscount": 0.66,
                "Discount": 100
            }
        },
        "RequestId": "56d68b92-7004-4716-b3bf-3c2c231035c9"
    }
}
```

