**Example 1: 查询sdkappid下房间信息**



Input: 

```
tccli trtc DescribeRoomInfo --cli-unfold-argument  \
    --StartTime 1590065777 \
    --SdkAppId 1400353843 \
    --EndTime 1590065877 \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 10,
        "RoomList": [
            {
                "CommId": "1400188366_563398783_1587959355",
                "RoomString": "113a730673fee2d86e93e26cddb25b7d",
                "CreateTime": 1587959355,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_113a730673fee2d86e93e26cddb25b7d"
            },
            {
                "CommId": "1400188366_3791597063_1587959341",
                "RoomString": "4724f5b26c36bd53ea139e7e1c3dea1e",
                "CreateTime": 1587959341,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_4724f5b26c36bd53ea139e7e1c3dea1e"
            },
            {
                "CommId": "1400188366_15343445_1587731480",
                "RoomString": "ae4e2ebc3a71d5b151efca3e1dbe32e9",
                "CreateTime": 1587731480,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_ae4e2ebc3a71d5b151efca3e1dbe32e9"
            },
            {
                "CommId": "1400188366_1100067693_1587730962",
                "RoomString": "f83dec1f40adaf92117b62d6f9e7e0b4",
                "CreateTime": 1587730962,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_f83dec1f40adaf92117b62d6f9e7e0b4"
            },
            {
                "CommId": "1400188366_2420034035_1587723604",
                "RoomString": "76f067dfad1044171dad37bf65b1cf4b",
                "CreateTime": 1587723604,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_76f067dfad1044171dad37bf65b1cf4b"
            },
            {
                "CommId": "1400188366_2420034035_1587713998",
                "RoomString": "76f067dfad1044171dad37bf65b1cf4b",
                "CreateTime": 1587713998,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "mixer_76f067dfad1044171dad37bf65b1cf4b"
            },
            {
                "CommId": "1400188366_3501_1586952940",
                "RoomString": "3501",
                "CreateTime": 1586952940,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "yuting"
            },
            {
                "CommId": "1400188366_3015068783_1586952940",
                "RoomString": "7651c9da1253981c8b842bcdcad11c3e",
                "CreateTime": 1586952940,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "7651c9da1253981c8b842bcdcad11c3e"
            },
            {
                "CommId": "1400188366_3501_1586952865",
                "RoomString": "3501",
                "CreateTime": 1586952865,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "yuting"
            },
            {
                "CommId": "1400188366_3015068783_1586952865",
                "RoomString": "7651c9da1253981c8b842bcdcad11c3e",
                "CreateTime": 1586952865,
                "DestroyTime": 1588040628,
                "IsFinished": false,
                "UserId": "7651c9da1253981c8b842bcdcad11c3e"
            }
        ],
        "RequestId": "83ca6fdd-cf4c-46a9-a577-74c3497ad3fa"
    }
}
```

