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
        "TotalCount": 0,
        "KTVRobotInfoSet": [
            {
                "RobotId": "d2w7m6t9z8",
                "Status": "Play",
                "Playlists": [
                    "vvws7nzzxg"
                ],
                "CurIndex": 1,
                "Position": 120000,
                "SetAudioParamInput": {
                    "Type": "Original"
                },
                "JoinRoomInput": {
                    "TRTCJoinRoomInput": {
                        "Sign": "我是孤独的鹰",
                        "RoomId": "1234",
                        "SdkAppId": "140000001",
                        "UserId": "tom",
                        "RoomIdType": "Integer"
                    }
                },
                "RTCSystem": "TRTC",
                "SetPlayModeInput": {
                    "PlayMode": "RepeatPlaylist"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

