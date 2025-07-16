**Example 1: 修改转码模板**



Input: 

```
tccli mps ModifyTranscodeTemplate --cli-unfold-argument  \
    --Definition 1008 \
    --Container mp4 \
    --VideoTemplate.Codec h264 \
    --VideoTemplate.Bitrate 256 \
    --VideoTemplate.Fps 60 \
    --AudioTemplate.SampleRate 48000 \
    --AudioTemplate.Codec aac \
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

**Example 2: 修改转码模板示例 2**



Input: 

```
tccli mps ModifyTranscodeTemplate --cli-unfold-argument  \
    --Definition 407020 \
    --Name 转码模板12 \
    --Comment 转码模板12 \
    --RemoveVideo 0 \
    --RemoveAudio 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3bxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxd6"
    }
}
```

