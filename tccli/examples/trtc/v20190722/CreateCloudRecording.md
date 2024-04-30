**Example 1: 启动云端录制**

启动SdkAppId 为 1234 指定房间（房间号为3560）的云端录制。

房间空闲等待时间设置为1分钟。
录制模式为合流模式。
录制的流类型为音视频。
默认订阅所有用户的流。
录制视频的宽度360，录制视频的高度640，帧率15，比特率500,000bps，默认背景色。
录制视频布局模式为九宫格布局。
存储至腾讯云点播VOD

Input: 

```
tccli trtc CreateCloudRecording --cli-unfold-argument  \
    --StorageParams.CloudVod.TencentVod.ExpireTime 0 \
    --UserSig 11xx111 \
    --UserId 10001 \
    --RecordParams.MaxIdleTime 60 \
    --RecordParams.StreamType 0 \
    --RecordParams.RecordMode 2 \
    --RoomIdType 1 \
    --MixTranscodeParams.VideoParams.Width 360 \
    --MixTranscodeParams.VideoParams.BitRate 500000 \
    --MixTranscodeParams.VideoParams.Fps 15 \
    --MixTranscodeParams.VideoParams.Height 640 \
    --MixTranscodeParams.VideoParams.Gop 10 \
    --MixLayoutParams.MixLayoutMode 3 \
    --SdkAppId 1234 \
    --RoomId 3560
```

Output: 
```
{
    "Response": {
        "TaskId": "-gCTFWtU7t7DUlo7A8IswFszO9z2O-rbERqJAoK-4pycoZXKjIAAnasdcasdOEycyX4CnzhIm4RAQ..",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

