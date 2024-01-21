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
                "Acodec": "aac",
                "Profile": "baseline",
                "Description": "模板描述",
                "VideoBitrate": 30,
                "BitrateToOrig": 0,
                "AiTransCode": 0,
                "HeightToOrig": 0,
                "AudioBitrate": 15,
                "Rotate": 0,
                "TemplateName": "模板名称",
                "AdaptBitratePercent": 0.0,
                "Vcodec": "h264",
                "NeedAudio": 1,
                "DRMTracks": "AUDIO|UHD2",
                "NeedVideo": 1,
                "DRMType": "widevine",
                "ShortEdgeAsHeight": 0,
                "Height": 250,
                "FpsToOrig": 0
            }
        ],
        "RequestId": "1dc2eb7b-b29b-4c5a-96f6-5699c54140fd"
    }
}
```

