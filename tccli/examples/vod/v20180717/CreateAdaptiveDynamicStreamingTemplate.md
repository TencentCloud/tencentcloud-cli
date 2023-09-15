**Example 1: 创建转自适应码流模板**

创建转自适应码流模板。

Input: 

```
tccli vod CreateAdaptiveDynamicStreamingTemplate --cli-unfold-argument  \
    --StreamInfos.0.Audio.SampleRate 44100 \
    --StreamInfos.0.Audio.Codec flac \
    --StreamInfos.0.Audio.Bitrate 1024 \
    --StreamInfos.0.Video.Codec libx264 \
    --StreamInfos.0.Video.Bitrate 2000 \
    --StreamInfos.0.Video.Fps 25 \
    --Name 转自适应码流模板1 \
    --Format HLS
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

