**Example 1: 播放指定音乐**

播放第2首歌曲

Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command Play \
    --SyncRobotCommands.0.PlayCommandInput.Index 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 变更歌曲音频参数**



Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SetAudioParam \
    --SyncRobotCommands.0.SetAudioParamCommandInput.Type Accompaniment
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: 切换下一首歌曲**



Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SwitchNext
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 4: 发送自定义消息**



Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SendMessage \
    --SyncRobotCommands.0.SendMessageCommandInput.Message {"Field1":"Value1"} \
    --SyncRobotCommands.0.SendMessageCommandInput.Repeat 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 5: 设置播放模式**

设置播放模式为随机播放。

Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SetPlayMode \
    --SyncRobotCommands.0.SetPlayModeCommandInput.PlayMode Shuffle
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 6: 设置销毁模式**

设置销毁模式为：房间没人后，2分钟内无人进入自动销毁。

Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SetDestroyMode \
    --SyncRobotCommands.0.SetDestroyModeCommandInput.DestroyMode Expire \
    --SyncRobotCommands.0.SetDestroyModeCommandInput.DestroyExpireTime 120
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 7: 播放列表添加歌曲并播放**



Input: 

```
tccli yinsuda SyncKTVRobotCommand --cli-unfold-argument  \
    --AppName ktv \
    --UserId 10001 \
    --RobotId xxxxx \
    --SyncRobotCommands.0.Command SetPlaylist \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Type Add \
    --SyncRobotCommands.0.SetPlaylistCommandInput.MusicIds xxxxxxx \
    --SyncRobotCommands.0.SetPlaylistCommandInput.Index -1 \
    --SyncRobotCommands.1.Command Play
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

