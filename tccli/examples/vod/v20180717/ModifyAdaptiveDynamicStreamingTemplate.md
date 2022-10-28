**Example 1: 修改转自适应码流模板**



Input: 

```
tccli vod ModifyAdaptiveDynamicStreamingTemplate --cli-unfold-argument  \
    --Definition 10038 \
    --StreamInfos.0.Audio.SampleRate 44100 \
    --StreamInfos.0.Audio.Codec flac \
    --StreamInfos.0.Audio.Bitrate 1000 \
    --StreamInfos.0.Video.Codec libx264 \
    --StreamInfos.0.Video.Bitrate 2000 \
    --StreamInfos.0.Video.Fps 25 \
    --Name 转自适应码流模板2 \
    --Format HLS
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

