**Example 1: 续费 TWeSee 视频理解订阅**



Input: 

```
tccli iotexplorer RenewTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --Period 1 \
    --ChannelId 0 \
    --CustomOrderId order-0013
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "1200",
        "OrderId": "2026042**********584511",
        "OriginalPrice": "2000",
        "ResourceId": "twesee-753yd29x30********jqww1",
        "Status": "DELIVERED",
        "RequestId": "0d350a07-0fc9-455c-98c8-0946d721dc1a"
    }
}
```

