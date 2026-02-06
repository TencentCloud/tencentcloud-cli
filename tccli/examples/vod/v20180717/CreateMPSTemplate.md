**Example 1: 创建 MPS 音视频增强任务模板**



Input: 

```
tccli vod CreateMPSTemplate --cli-unfold-argument  \
    --SubAppId 1500000001 \
    --TemplateType Transcode \
    --MPSCreateTemplateParams {"Container":"mp4","Name":"test","RemoveAudio":1,"VideoTemplate":{"Codec":"h264","Fps":0,"Bitrate":0},"EnhanceConfig":{"VideoEnhance":{"FrameRate":{"Switch":"ON","Fps":50}}}}
```

Output: 
```
{
    "Response": {
        "Definition": 22143,
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

