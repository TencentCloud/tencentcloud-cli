**Example 1: 创建转码模板**

创建转码模板

Input: 

```
tccli vod CreateTranscodeTemplate --cli-unfold-argument  \
    --RemoveVideo 0 \
    --Container mp4 \
    --Name 转码模板1 \
    --AudioTemplate.SampleRate 200 \
    --AudioTemplate.Codec libfdk_aac \
    --AudioTemplate.Bitrate 200 \
    --VideoTemplate.Codec libx264 \
    --VideoTemplate.Bitrate 256 \
    --VideoTemplate.Fps 45 \
    --RemoveAudio 0
```

Output: 
```
{
    "Response": {
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

