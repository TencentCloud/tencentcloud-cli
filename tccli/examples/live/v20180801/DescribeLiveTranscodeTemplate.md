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
            "Profile": "baseline",
            "AudioBitrate": 15,
            "Rotate": 0,
            "BitrateToOrig": 0,
            "TemplateName": "mytemplate",
            "VideoBitrate": 30,
            "ShortEdgeAsHeight": 0,
            "Vcodec": "h264",
            "AdaptBitratePercent": 0.0,
            "AiTransCode": 0,
            "Height": 250,
            "Width": 250,
            "NeedAudio": 1,
            "FpsToOrig": 0,
            "Fps": 30,
            "TemplateId": 1000,
            "Description": "desc",
            "HeightToOrig": 0,
            "NeedVideo": 1,
            "Gop": 3,
            "Acodec": "aac",
            "DRMTracks": "AUDIO",
            "DRMType": "widevine"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

