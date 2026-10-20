**Example 1: 成功示例**



Input: 

```
tccli iotexplorer PurchaseImagePackage --cli-unfold-argument  \
    --RetentionDays 30 \
    --ProductId YYZRTPMCUG \
    --DeviceName billing_test_7 \
    --ValidityPeriod annual_card \
    --ImageCapacity 300 \
    --GoodsNum 1 \
    --ChannelId 22
```

Output: 
```
{
    "Response": {
        "RequestId": "86c45250-8e08-48b2-8c20-3d668c86b42b"
    }
}
```

