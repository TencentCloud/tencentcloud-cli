**Example 1: 查询机器人信息**



Input: 

```
tccli yinsuda DescribeKTVRobots --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
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
                    "Type": "Original"
                },
                "SetPlayModeInput": {
                    "PlayMode": "Order"
                }
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

