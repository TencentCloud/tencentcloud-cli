**Example 1: 请求示例**

CreateLiveTranscodeTemplate 例子。

Input: 

```
tccli live CreateLiveTranscodeTemplate --cli-unfold-argument  \
    --TemplateName jiang8 \
    --VideoBitrate 0 \
    --Description  \
    --IsAdaptiveBitRate 1 \
    --AdaptiveChildren.0.TemplateName jiang9 \
    --AdaptiveChildren.0.Vcodec origin \
    --AdaptiveChildren.0.VideoBitrate 3000 \
    --AdaptiveChildren.0.Height 2000 \
    --AdaptiveChildren.0.Fps 0 \
    --AdaptiveChildren.0.Gop 0 \
    --AdaptiveChildren.0.NeedVideo 1 \
    --AdaptiveChildren.0.NeedAudio 1 \
    --AdaptiveChildren.0.BitrateToOrig 0 \
    --AdaptiveChildren.0.HeightToOrig 0 \
    --AdaptiveChildren.0.FpsToOrig 0 \
    --AdaptiveChildren.0.ShortEdgeAsHeight 0 \
    --AdaptiveChildren.0.HlsContainerFormat ts \
    --AdaptiveChildren.0.HlsMp4VideoCodecTag hev1
```

Output: 
```
{
    "Response": {
        "TemplateId": 8453014,
        "RequestId": "12306f18-9332-412f-bf15-e5b47f6fcaf1"
    }
}
```

