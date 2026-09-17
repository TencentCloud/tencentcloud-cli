**Example 1: 成功示例**



Input: 

```
tccli iotexplorer GetVodCloudStorageEventList --cli-unfold-argument  \
    --ProductId YYZRTPMCUG \
    --DeviceName billing_test_7 \
    --Date 2026-08-24 \
    --ChannelId 23
```

Output: 
```
{
    "Response": {
        "Context": "",
        "Events": [
            {
                "EventEndTime": 1787538066,
                "EventId": "_sys_static_1787538066",
                "EventStartTime": 1787538066,
                "IsStaticEvent": true,
                "ThumbnailUrl": "/700000625262/YYZRTPMCUG/billing_test_7/23/events/1787538070641402396.jpg",
                "VideoList": []
            }
        ],
        "Listover": true,
        "Total": 2,
        "VodAppId": "1500058***",
        "RequestId": "befa4124-838a-4baf-9bc3-1490f47655e2"
    }
}
```

