**Example 1: 批量续费 TWeSee 视频理解订阅**

批量续费多个 TWeSee 视频理解订阅。

Input: 

```
tccli iotexplorer BatchRenewTWeSeeSubscription --cli-unfold-argument  \
    --Entries.0.ProductId 4AHMY9X89Y \
    --Entries.0.DeviceName dev001 \
    --Entries.0.ChannelId 0 \
    --Entries.0.ServiceType VID_COMP \
    --Entries.0.Period 1 \
    --Entries.0.CustomOrderId order-0013 \
    --Entries.1.ProductId 4AHMY9X89Y \
    --Entries.1.DeviceName dev002 \
    --Entries.1.ChannelId 0 \
    --Entries.1.ServiceType VID_COMP \
    --Entries.1.Period 1 \
    --Entries.1.CustomOrderId order-0014
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "OrderId": "2026042**********584511",
                "Status": "DELIVERED",
                "ResourceId": "twesee-753yd29x30********jqww1"
            },
            {
                "OrderId": "2026042**********584512",
                "Status": "DELIVERING",
                "ResourceId": ""
            }
        ],
        "RequestId": "0d350a07-0fc9-455c-98c8-0946d721dc1a"
    }
}
```

