**Example 1: 启动云端混流**

启动指定房间（字符串房间号为Room_3560）的云端混流，同时指定各路画面按屏幕分享模板排布。

设置云端混流参数如下：
- CDN直播流ID：1400188366_3560_mix。
- 录制文件名：1400188366_3560_mix_file。
- CDN直播流视频参数：视频宽为1280、高为720，视频码率为1560kbps，视频帧率为15，gop为2秒。
- CDN直播流音频参数：音频采样率为48kHz，音频码率为64kbps，音频声道数为双声道。
- 各路画面按屏幕分享模板排布，占据屏幕左侧大画面的视频流为用户(main_pc)的屏幕分享。

Input: 

```
tccli trtc StartMCUMixTranscodeByStrRoomId --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --StrRoomId Room_3560 \
    --OutputParams.StreamId 1400188366_3560_mix \
    --OutputParams.PureAudioStream 0 \
    --OutputParams.RecordId 1400188366_3560_mix_file \
    --OutputParams.RecordAudioOnly 0 \
    --EncodeParams.VideoWidth 1280 \
    --EncodeParams.VideoHeight 720 \
    --EncodeParams.VideoBitrate 1560 \
    --EncodeParams.VideoFramerate 15 \
    --EncodeParams.VideoGop 2 \
    --EncodeParams.BackgroundColor 0 \
    --EncodeParams.AudioSampleRate 48000 \
    --EncodeParams.AudioBitrate 64 \
    --EncodeParams.AudioChannels 2 \
    --LayoutParams.Template 2 \
    --LayoutParams.MainVideoUserId main_pc \
    --LayoutParams.MainVideoStreamType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

