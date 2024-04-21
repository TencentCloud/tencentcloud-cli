**Example 1: 创建转自适应码流模板**



Input: 

```
tccli mps CreateAdaptiveDynamicStreamingTemplate --cli-unfold-argument  \
    --Name 转自适应码流模板1 \
    --Format HLS \
    --StreamInfos.0.Video.Codec h264 \
    --StreamInfos.0.Video.Bitrate 2000 \
    --StreamInfos.0.Video.Fps 2000 \
    --StreamInfos.0.Audio.Codec flac \
    --StreamInfos.0.Audio.SampleRate 44100 \
    --StreamInfos.0.Audio.Bitrate 200
```

Output: 
```
{
    "Response": {
        "Definition": 30018,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

