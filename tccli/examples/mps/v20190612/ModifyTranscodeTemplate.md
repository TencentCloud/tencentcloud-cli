**Example 1: Modifying transcoding template**



Input: 

```
tccli mps ModifyTranscodeTemplate --cli-unfold-argument  \
    --Definition 1008 \
    --Container mp4 \
    --VideoParam.Codec libx264 \
    --VideoParam.Fps 60 \
    --VideoParam.Bitrate 256 \
    --AudioParam.Codec libfdk_aac \
    --AudioParam.Bitrate 200 \
    --AudioParam.SampleRate 200
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

