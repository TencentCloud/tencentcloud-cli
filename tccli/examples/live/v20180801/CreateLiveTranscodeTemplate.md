**Example 1: 请求示例**



Input: 

```
tccli live CreateLiveTranscodeTemplate --cli-unfold-argument  \
    --Vcodec h264 \
    --Acodec aac \
    --AudioBitrate 500 \
    --TemplateName 900m \
    --Description test \
    --VideoBitrate 900 \
    --Width 250 \
    --NeedVideo 1 \
    --NeedAudio 1 \
    --Height 250 \
    --Fps 30 \
    --Gop 3 \
    --Rotate 0 \
    --Profile main \
    --BitrateToOrig 0 \
    --HeightToOrig 0 \
    --FpsToOrig 0
```

Output: 
```
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

