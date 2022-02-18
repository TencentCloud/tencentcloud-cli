**Example 1: 查询机器人信息**



Input: 

```
tccli ame DescribeKTVRobots --cli-unfold-argument  \
    --RobotIds ame-xxxxx1 \
    --Statuses Play \
    --CreateTime.After 2022-01-10T07:25:52Z \
    --CreateTime.Before 2022-01-11T07:25:52Z
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "KTVRobotInfoSet": [
            {
                "RobotId": "ame-xxxxx1",
                "Status": "Play",
                "Playlists": [
                    "xxxx1",
                    "xxxx2",
                    "xxxx3",
                    "xxxx4"
                ],
                "CurIndex": 2,
                "Position": 120,
                "RTCSystem": "TRTC",
                "JoinRoomInput": {
                    "TRTCJoinRoomInput": {
                        "Sign": "xxxxxxxxxxx",
                        "RoomId": "12345",
                        "SdkAppId": "140000001",
                        "UserId": "tom"
                    }
                },
                "SetAudioParamInput": {
                    "Definition": "audio/mi",
                    "Type": "Original"
                },
                "SetPlayModeInput": {
                    "PlayMode": "Order"
                }
            }
        ],
        "RequestId": "xx"
    }
}
```

