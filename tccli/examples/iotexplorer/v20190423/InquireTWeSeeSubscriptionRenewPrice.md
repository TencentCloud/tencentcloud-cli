**Example 1: 查询续费 1 个月视频理解的价格**



Input: 

```
tccli iotexplorer InquireTWeSeeSubscriptionRenewPrice --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --Period 1 \
    --ChannelId 0
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "1200",
        "OriginalPrice": "2000",
        "RequestId": "6010f2e8-e5e0-4b85-b0d0-cf0a7c068a2b"
    }
}
```

