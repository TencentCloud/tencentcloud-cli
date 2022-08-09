**Example 1: 启动云端录制**

启动SdkAppId 为 1234 指定房间（房间号为3560）的云端录制。

房间空闲等待时间设置为1分钟。
录制模式为混流模式。
录制的流类型为音视频。
默认订阅所有用户的流。
第三方存储设置为腾讯云存储，存储的文件前缀为directory1/directory2/。
录制视频的宽度360，录制视频的高度640，帧率15，比特率500,000bps，默认背景色。
录制视频布局模式为九宫格布局。

Input: 

```
tccli trtc CreateCloudRecording --cli-unfold-argument  \
    --StorageParams.CloudVod.TencentVod.ExpireTime 0 \
    --UserSig xx \
    --UserId xx \
    --RecordParams.MaxIdleTime 60 \
    --RecordParams.StreamType 0 \
    --RecordParams.RecordMode 2 \
    --RoomIdType 1 \
    --MixTranscodeParams.VideoParams.Width 360 \
    --MixTranscodeParams.VideoParams.BitRate 500000 \
    --MixTranscodeParams.VideoParams.Fps 15 \
    --MixTranscodeParams.VideoParams.Height 640 \
    --MixTranscodeParams.VideoParams.Gop 10 \
    --SdkAppId 1234 \
    --RoomId 3560
```

Output: 
```
{
    "Response": {
        "TaskId": "5df46eb2-8e4b-490e-9c3c-dbd3b84faefc",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

