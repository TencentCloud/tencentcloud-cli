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

**Example 2: 创建直播互动机器人并初始化**



Input: 

```
tccli ame CreateKTVRobot --cli-unfold-argument  \
    --SyncRobotCommands.0.Command SetPlaylist \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Type Add \
    --SyncRobotCommands.0.SetPlaylistCommandInput.MusicIds xxxxxxx \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Index -1 \
    --SyncRobotCommands.1.Command SetVolume \
    --SyncRobotCommands.1.SetVolumeCommandInput.Volume 50 \
    --SyncRobotCommands.2.Command Play \
    --SyncRobotCommands.2.PlayCommandInput.Index 0 \
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

