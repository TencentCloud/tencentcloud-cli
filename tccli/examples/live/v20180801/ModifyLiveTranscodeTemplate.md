**Example 1: 请求示例**

ModifyLiveTranscodeTemplate 例子。

Input: 

```
tccli live ModifyLiveTranscodeTemplate --cli-unfold-argument  \
    --Profile main \
    --AudioBitrate 600 \
    --Rotate 0 \
    --Description test \
    --VideoBitrate 1500 \
    --Vcodec h265 \
    --Height 240 \
    --Width 250 \
    --NeedAudio 1 \
    --FpsToOrig 0 \
    --Fps 30 \
    --TemplateId 1001 \
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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

