**Example 1: 查询相关事件**



Input: 

```
tccli rum DescribeTDEMRelatedEvents --cli-unfold-argument  \
    --AppId 11 \
    --StartTime 1787404860000 \
    --EndTime 1789996860000 \
    --Mode timeline \
    --SessionId mp_81069b302d52d8396753e1c442276bfd \
    --Offset 0 \
    --Limit 200 \
    --Category all
```

Output: 
```
{
    "Response": {
        "CategoryCounts": [
            {
                "Key": "all",
                "Value": 147
            }
        ],
        "Events": [
            {
                "AppVersion": "1.0.0",
                "Browser": "Safari",
                "City": "深圳",
                "Country": "中国",
                "DeviceType": "mobile",
                "EventCategory": "custom",
                "EventId": "evt_1789718558702_n1402f",
                "EventName": "set_data_timing",
                "EventType": "custom",
                "Ip": "59.37.125.48",
                "Isp": "电信",
                "Measurements": [
                    {
                        "Key": "duration",
                        "Value": 36
                    }
                ],
                "NormalizedPageUrl": "pages/home/home",
                "Os": "iPhone OS",
                "PageUrl": "pages/home/home",
                "Platform": "miniprogram",
                "Province": "广东",
                "SessionId": "mp_81069b302d52d8396753e1c442276bfd",
                "Timestamp": 1789718558702,
                "UserId": "tdesigndemo"
            }
        ],
        "HasMore": false,
        "Limit": 200,
        "Offset": 0,
        "RequestId": "bd646822-8130-4d52-85df-31ba0fdc1ace"
    }
}
```

