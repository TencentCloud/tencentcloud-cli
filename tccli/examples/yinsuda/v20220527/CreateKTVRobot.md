**Example 1: 创建机器人**



Input: 

```
tccli yinsuda CreateKTVRobot --cli-unfold-argument  \
    --RTCSystem TRTC \
    --AppName ktv \
    --UserId 10001 \
    --JoinRoomInput.TRTCJoinRoomInput.Sign xxxxxxxxxxx \
    --JoinRoomInput.TRTCJoinRoomInput.RoomId 12345 \
    --JoinRoomInput.TRTCJoinRoomInput.SdkAppId 140000001 \
    --JoinRoomInput.TRTCJoinRoomInput.UserId tom
```

Output: 
```
{
    "Response": {
        "RobotId": "12500-robot-xxxxxxx",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 创建机器人并初始化**



Input: 

```
tccli yinsuda CreateKTVRobot --cli-unfold-argument  \
    --SyncRobotCommands.0.Command SetPlaylist \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Type Add \
    --SyncRobotCommands.0.SetPlaylistCommandInput.MusicIds xxxxxxx \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Index -1 \
    --SyncRobotCommands.1.Command SetVolume \
    --SyncRobotCommands.2.Command Play \
    --SyncRobotCommands.2.PlayCommandInput.Index 0 \
    --RTCSystem TRTC \
    --AppName ktv \
    --UserId 10001 \
    --JoinRoomInput.TRTCJoinRoomInput.Sign xxxxxxxxxxx \
    --JoinRoomInput.TRTCJoinRoomInput.RoomId 12345 \
    --JoinRoomInput.TRTCJoinRoomInput.SdkAppId 140000001 \
    --JoinRoomInput.TRTCJoinRoomInput.UserId tom
```

Output: 
```
{
    "Response": {
        "RobotId": "12500-robot-xxxxxxx",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

