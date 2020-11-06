**Example 1: Creating transcoding template**



Input: 

```
tccli mps CreateTranscodeTemplate --cli-unfold-argument  \
    --Container mp4 \
    --Name 'Transcoding template 1' \
    --RemoveVideo 0 \
    --RemoveAudio 0 \
    --VideoTemplate.Codec libx264 \
    --VideoTemplate.Fps 45 \
    --VideoTemplate.Bitrate 256 \
    --AudioTemplate.Codec libfdk_aac \
    --AudioTemplate.Bitrate 200 \
    --AudioTemplate.SampleRate 200
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

