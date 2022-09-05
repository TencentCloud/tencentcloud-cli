**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTranscodeTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Width": 250,
                "Fps": 30,
                "TemplateId": 1000,
                "Gop": 3,
                "Acodec": "xx",
                "Profile": "xx",
                "Description": "xx",
                "VideoBitrate": 30,
                "BitrateToOrig": 0,
                "AiTransCode": 0,
                "HeightToOrig": 0,
                "AudioBitrate": 15,
                "Rotate": 0,
                "TemplateName": "xx",
                "AdaptBitratePercent": 0.0,
                "Vcodec": "xx",
                "NeedAudio": 1,
                "DRMTracks": "xx",
                "NeedVideo": 1,
                "DRMType": "xx",
                "ShortEdgeAsHeight": 0,
                "Height": 250,
                "FpsToOrig": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

