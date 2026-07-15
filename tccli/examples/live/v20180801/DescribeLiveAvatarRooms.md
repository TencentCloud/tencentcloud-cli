**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveAvatarRooms --cli-unfold-argument  \
    --PageIndex 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "InfoList": [
            {
                "AvatarKey": "9a7a2894ebd44ad3877ce98caac9a7cc",
                "CreateTime": "2025-07-02T07:19:08Z",
                "RoomId": "10002",
                "Name": "测试直播间",
                "TimbreKey": "male_1",
                "ToUrl": "rtmp://5000.livepush.myqcloud.com/live/testavatar?txSecret=9f84eb128c7414074e9b14651b6d03e0&txTime=68629cf1",
                "UpdateTime": "2025-07-02T07:19:08Z"
            }
        ],
        "LimitCreateNum": 100,
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e",
        "TotalNum": 1
    }
}
```

