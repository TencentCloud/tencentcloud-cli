**Example 1: 请求示例**

CreateLiveTranscodeTemplate 例子。

Input: 

```
tccli live CreateLiveTranscodeTemplate --cli-unfold-argument  \
    --Profile main \
    --AudioBitrate 500 \
    --Rotate 0 \
    --Description test \
    --TemplateName 900m \
    --VideoBitrate 900 \
    --Vcodec h264 \
    --Height 250 \
    --Width 250 \
    --NeedAudio 1 \
    --FpsToOrig 0 \
    --Fps 30 \
    --BitrateToOrig 0 \
    --HeightToOrig 0 \
    --NeedVideo 1 \
    --Gop 3 \
    --Acodec aac
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

