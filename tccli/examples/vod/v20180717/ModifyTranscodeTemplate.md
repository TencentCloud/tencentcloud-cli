**Example 1: 修改转码模板**

修改转码模板

Input: 

```
tccli vod ModifyTranscodeTemplate --cli-unfold-argument  \
    --Definition 1008 \
    --Container mp4 \
    --VideoTemplate.Codec libx264 \
    --VideoTemplate.Bitrate 256 \
    --VideoTemplate.Fps 60 \
    --AudioTemplate.SampleRate 200 \
    --AudioTemplate.Codec libfdk_aac \
    --AudioTemplate.Bitrate 200
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

