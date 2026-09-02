**Example 1: 修改吗转码模版**



Input: 

```
tccli live ModifyLiveTranscodeTemplate --cli-unfold-argument  \
    --TemplateId 8452765 \
    --Vcodec origin \
    --Acodec  \
    --Description  \
    --VideoBitrate 0 \
    --Width 0 \
    --NeedVideo 1 \
    --NeedAudio 1 \
    --Height 0 \
    --Fps 0 \
    --Gop 0 \
    --Rotate 0 \
    --Profile  \
    --BitrateToOrig 0 \
    --HeightToOrig 0 \
    --FpsToOrig 0 \
    --AdaptBitratePercent 0.12 \
    --ShortEdgeAsHeight 0 \
    --DRMType  \
    --DRMTracks  \
    --IsAdaptiveBitRate 0 \
    --AudienceDrivenTranscode 1 \
    --AudienceThreshold 101
```

Output: 
```
{
    "Response": {
        "RequestId": "7a8256df-cd2c-4a23-9516-1b2cd9a31b80"
    }
}
```

