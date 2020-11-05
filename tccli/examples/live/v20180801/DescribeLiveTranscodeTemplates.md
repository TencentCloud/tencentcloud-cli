**Example 1: Sample request**



Input: 

```
tccli live DescribeLiveTranscodeTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Vcodec": "h265",
                "VideoBitrate": 30,
                "Avodec": "aac",
                "AudioBitrate": 15,
                "Width": 250,
                "Height": 250,
                "Fps": 30,
                "Gop": 3,
                "Rotate": 0,
                "Profile": "main",
                "BitrateToOrig": 0,
                "HeightToOrig": 0,
                "FpsToOirg": 0,
                "NeedVideo": 1,
                "NeedAudio": 1,
                "TemplateId": 1000,
                "TemplateName": "test",
                "Description": "test",
                "AiTransCode": 0,
                "AdaptBitratePercent": 0
            }
        ],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

