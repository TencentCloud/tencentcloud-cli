**Example 1: 获取音画质检测模板列表。**

获取音画质检测模板列表。

Input: 

```
tccli vod DescribeQualityInspectTemplates --cli-unfold-argument  \
    --Definitions 20001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "QualityInspectTemplateSet": [
            {
                "Definition": 20001,
                "Name": "test",
                "Comment": "",
                "Type": "Custom",
                "ScreenshotInterval": 1,
                "JitterConfigure": {
                    "Switch": "ON"
                },
                "BlurConfigure": null,
                "AbnormalLightingConfigure": null,
                "CrashScreenConfigure": null,
                "BlackWhiteEdgeConfigure": null,
                "NoiseConfigure": null,
                "MosaicConfigure": null,
                "QRCodeConfigure": null,
                "QualityEvaluationConfigure": null,
                "VoiceConfigure": null,
                "CreateTime": "2023-06-01T10:00:00Z",
                "UpdateTime": "2023-06-01T10:00:00Z"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

