**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTranscodeTemplate --cli-unfold-argument  \
    --TemplateId 1000
```

Output: 
```
{
    "Response": {
        "Template": {
            "Profile": "xx",
            "AudioBitrate": 15,
            "Rotate": 0,
            "BitrateToOrig": 0,
            "TemplateName": "xx",
            "VideoBitrate": 30,
            "ShortEdgeAsHeight": 0,
            "Vcodec": "xx",
            "AdaptBitratePercent": 0.0,
            "AiTransCode": 0,
            "Height": 250,
            "Width": 250,
            "NeedAudio": 1,
            "FpsToOrig": 0,
            "Fps": 30,
            "TemplateId": 1000,
            "Description": "xx",
            "HeightToOrig": 0,
            "NeedVideo": 1,
            "Gop": 3,
            "Acodec": "xx"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

