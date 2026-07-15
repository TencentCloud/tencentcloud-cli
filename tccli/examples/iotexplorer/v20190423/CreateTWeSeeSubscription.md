**Example 1: 开通 TWeSee 视频理解基础版**



Input: 

```
tccli iotexplorer CreateTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --Period 1 \
    --ServiceTier BASIC
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "1200",
        "OrderId": "20260420*********550201",
        "OriginalPrice": "2000",
        "ResourceId": "twesee-753yd29x30********jqww1",
        "Status": "DELIVERED",
        "RequestId": "6f7647ba-757c-439c-8781-c187b5a561f3"
    }
}
```

