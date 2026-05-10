**Example 1: 修改 MPS 音视频智能字幕模板**



Input: 

```
tccli vod ModifyMPSTemplate --cli-unfold-argument  \
    --SubAppId 221157 \
    --TemplateType SmartSubtitle \
    --SmartSubtitleTemplate.Definition 50023 \
    --SmartSubtitleTemplate.Name Template1 \
    --SmartSubtitleTemplate.Comment SmartSubtitle Template1 \
    --SmartSubtitleTemplate.SubtitleType 0 \
    --SmartSubtitleTemplate.VideoSrcLanguage en \
    --SmartSubtitleTemplate.SubtitleFormat vtt \
    --SmartSubtitleTemplate.TranslateSwitch OFF \
    --SmartSubtitleTemplate.ProcessType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0d54e984-91ba-4b2a-abb3-f417303bfd3a"
    }
}
```

