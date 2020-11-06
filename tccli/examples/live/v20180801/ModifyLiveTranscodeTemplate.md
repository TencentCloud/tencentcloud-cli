**Example 1: Sample request**



Input: 

```
tccli live ModifyLiveTranscodeTemplate --cli-unfold-argument  \
    --TemplateId 1001 \
    --Vcodec h265 \
    --Acodec aac \
    --AudioBitrate 600 \
    --Description test \
    --VideoBitrate 1500 \
    --Width 250 \
    --NeedVideo 1 \
    --NeedAudio 1 \
    --Height 240 \
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
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

