**Example 1: 批量开通 TWeSee 视频理解订阅**

批量开通多个 TWeSee 视频理解订阅。

Input: 

```
tccli iotexplorer BatchCreateTWeSeeSubscription --cli-unfold-argument  \
    --Entries.0.ProductId 4AHMY9X89Y \
    --Entries.0.DeviceName dev001 \
    --Entries.0.ChannelId 0 \
    --Entries.0.ServiceType VID_COMP \
    --Entries.0.ServiceTier BASIC \
    --Entries.0.Period 1 \
    --Entries.0.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --Entries.0.CustomOrderId order-0011 \
    --Entries.1.ProductId 4AHMY9X89Y \
    --Entries.1.DeviceName dev002 \
    --Entries.1.ChannelId 0 \
    --Entries.1.ServiceType VID_COMP \
    --Entries.1.ServiceTier BASIC \
    --Entries.1.Period 1 \
    --Entries.1.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --Entries.1.CustomOrderId order-0012
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "OrderId": "20260420*********550201",
                "Status": "DELIVERED",
                "ResourceId": "twesee-753yd29x30********jqww1"
            },
            {
                "OrderId": "20260420*********550202",
                "Status": "DELIVERING",
                "ResourceId": ""
            }
        ],
        "RequestId": "6f7647ba-757c-439c-8781-c187b5a561f3"
    }
}
```

