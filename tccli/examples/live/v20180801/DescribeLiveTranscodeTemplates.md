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
            }
        ],
        "RequestId": "xx"
    }
}
```

