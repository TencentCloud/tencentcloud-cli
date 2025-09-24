**Example 1: 查询所有智能擦除模板**

查询包括预设模板和自定义模板在内的所有智能擦除模板信息

Input: 

```
tccli mps DescribeSmartEraseTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e2ad2688-ca7c-4f85-bbb0-1cfbdf258013",
        "SmartEraseTemplateSet": [
            {
                "AliasName": "FaceAndLicensePlateBlur",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 302,
                "ErasePrivacyConfig": {
                    "PrivacyModel": "blur",
                    "PrivacyTargets": [
                        "plate",
                        "face"
                    ]
                },
                "EraseSubtitleConfig": null,
                "EraseType": "privacy",
                "EraseWatermarkConfig": null,
                "Name": "人脸和车牌模糊",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "FaceBlur",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 301,
                "ErasePrivacyConfig": {
                    "PrivacyModel": "blur",
                    "PrivacyTargets": [
                        "face"
                    ]
                },
                "EraseSubtitleConfig": null,
                "EraseType": "privacy",
                "EraseWatermarkConfig": null,
                "Name": "人脸模糊",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "WatermarkRemoval-AdvancedVersion",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 201,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": null,
                "EraseType": "watermark",
                "EraseWatermarkConfig": {
                    "WatermarkEraseMethod": "auto",
                    "WatermarkModel": "advanced"
                },
                "Name": "去水印-高级版",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "SubtitleRemoval_OCRExtractSubtitlesAndTranslateToEnglish",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 103,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "ON",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleFormat": "vtt",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransDstLang": "en",
                    "TransSwitch": "ON"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "去字幕_OCR提取字幕并翻译为英文",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T18:36:53+08:00"
            },
            {
                "AliasName": "SubtitleRemovalAndOCRExtractSubtitles",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 102,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "ON",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleFormat": "vtt",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "去字幕_OCR提取字幕",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T18:36:53+08:00"
            },
            {
                "AliasName": "SubtitleRemoval",
                "Comment": "",
                "CreateTime": "2025-07-15T10:51:04+08:00",
                "Definition": 101,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "去字幕",
                "Type": "Preset",
                "UpdateTime": "2025-07-15T10:51:04+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-08-04T15:16:25+08:00",
                "Definition": 200385,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "测试8",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T20:49:04+08:00",
                "Definition": 200022,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleLang": "zh_en",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "测试7",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T20:48:48+08:00",
                "Definition": 200021,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "auto",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "测试6",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            },
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T19:21:24+08:00",
                "Definition": 200019,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "custom",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "测试5",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            }
        ],
        "TotalCount": 14
    }
}
```

**Example 2: 查询指定智能擦除模板**

查询指定智能擦除模板信息

Input: 

```
tccli mps DescribeSmartEraseTemplates --cli-unfold-argument  \
    --Definitions 200019
```

Output: 
```
{
    "Response": {
        "RequestId": "83c6c7c2-3dab-4c6a-bedb-227371c038c0",
        "SmartEraseTemplateSet": [
            {
                "AliasName": "",
                "Comment": "",
                "CreateTime": "2025-07-02T19:21:24+08:00",
                "Definition": 200019,
                "ErasePrivacyConfig": null,
                "EraseSubtitleConfig": {
                    "OcrSwitch": "OFF",
                    "SubtitleEraseMethod": "custom",
                    "SubtitleModel": "standard",
                    "TransSwitch": "OFF"
                },
                "EraseType": "subtitle",
                "EraseWatermarkConfig": null,
                "Name": "测试5",
                "Type": "Custom",
                "UpdateTime": "2025-08-04T20:08:14+08:00"
            }
        ],
        "TotalCount": 1
    }
}
```

