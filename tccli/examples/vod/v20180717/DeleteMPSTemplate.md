**Example 1: 删除 MPS 音视频增强任务模板**



Input: 

```
tccli vod DeleteMPSTemplate --cli-unfold-argument  \
    --SubAppId 1500000001 \
    --TemplateType Transcode \
    --Definition 24214
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

