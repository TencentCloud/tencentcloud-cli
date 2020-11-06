**Example 1: Creating adaptive bitrate streaming template**



Input: 

```
tccli vod CreateAdaptiveDynamicStreamingTemplate --cli-unfold-argument  \
    --Name 'Adaptive bitrate streaming template 1' \
    --Format HLS \
    --StreamInfos.0.Video.Codec libx264 \
    --StreamInfos.0.Video.Bitrate 2000 \
    --StreamInfos.0.Audio.Codec flac \
    --StreamInfos.0.Audio.SampleRate 44100
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

