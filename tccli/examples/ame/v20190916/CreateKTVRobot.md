**Example 1: 创建直播互动机器人**



Input: 

```
tccli ame CreateKTVRobot --cli-unfold-argument  \
    --RTCSystem TRTC \
    --JoinRoomInput.TRTCJoinRoomInput.Sign xxxxxxxxxxx \
    --JoinRoomInput.TRTCJoinRoomInput.RoomId 12345 \
    --JoinRoomInput.TRTCJoinRoomInput.SdkAppId 140000001 \
    --JoinRoomInput.TRTCJoinRoomInput.UserId tom
```

Output: 
```
{
    "Response": {
        "RobotId": "ame-xxxxx",
        "RequestId": "xx"
    }
}
```

