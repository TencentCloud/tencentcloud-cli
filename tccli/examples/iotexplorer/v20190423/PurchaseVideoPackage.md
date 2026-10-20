**Example 1: 成功示例**



Input: 

```
tccli iotexplorer PurchaseVideoPackage --cli-unfold-argument  \
    --RetentionDays 7 \
    --RecordingMode event \
    --Bitrate 1m \
    --ProductId YYZRTPMCUG \
    --DeviceName billing_test_7 \
    --ValidityPeriod monthly_card \
    --GoodsNum 1 \
    --Override 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a3d94a07-e0a1-4706-a541-76c201d712cd"
    }
}
```

