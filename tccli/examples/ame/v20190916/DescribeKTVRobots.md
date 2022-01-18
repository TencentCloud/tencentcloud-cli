**Example 1: 查询机器人信息**



Input: 

```
tccli ame DescribeKTVRobots --cli-unfold-argument  \
    --RobotIds ame-xxxxx1 \
    --Statuses Play
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
                }
            }
        ],
        "RequestId": "xx"
    }
}
```

