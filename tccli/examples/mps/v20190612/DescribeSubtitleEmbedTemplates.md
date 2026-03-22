**Example 1: 获取字幕压制模板列表**



Input: 

```
tccli mps DescribeSubtitleEmbedTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SubtitleEmbedTemplateSet": [
            {
                "AliasName": "AutoFont-Background-LargeSize",
                "Comment": "",
                "CreateTime": "2026-03-17T15:06:16+08:00",
                "Definition": 4,
                "Name": "自动字体-有底大字幕",
                "SubtitleEmbedConfig": {
                    "CosInputInfo": {
                        "Bucket": "",
                        "Object": "",
                        "Region": ""
                    },
                    "FontAlpha": 1,
                    "FontColor": "0xFFFFFF",
                    "FontPath": "",
                    "FontSize": 10,
                    "FontSizeUnit": 1,
                    "FontType": "auto",
                    "PosX": 0,
                    "PosXUnit": 1,
                    "PosY": 13,
                    "PosYUnit": 1,
                    "SampleHeight": 0,
                    "SampleWidth": 0,
                    "SubtitleBoardConfig": {
                        "BoardAlpha": 1,
                        "BoardColor": "0x000000",
                        "BoardHeight": 30,
                        "BoardHeightUnit": 1,
                        "BoardWidth": 90,
                        "BoardWidthUnit": 1,
                        "BoardX": 0,
                        "BoardXUnit": 1,
                        "BoardY": 10,
                        "BoardYUnit": 1,
                        "SubtitleBoardConfigSwitch": 1
                    },
                    "SubtitleLayoutConfig": {
                        "Alignment": "bottom",
                        "LineSpacing": 0,
                        "LineSpacingUnit": 0,
                        "SubtitleLayoutConfigSwitch": 0
                    },
                    "SubtitleOutlineConfig": {
                        "OutlineAlpha": 1,
                        "OutlineColor": "0x000000",
                        "OutlineWidth": 1,
                        "OutlineWidthUnit": 0,
                        "SubtitleOutlineConfigSwitch": 1
                    },
                    "SubtitleShadowConfig": {
                        "ShadowAlpha": 1,
                        "ShadowColor": "0x000000",
                        "ShadowWidth": 0,
                        "ShadowWidthUnit": 0,
                        "SubtitleShadowConfigSwitch": 0
                    }
                },
                "Type": "Preset",
                "UpdateTime": "2026-03-17T15:06:16+08:00"
            }
        ],
        "TotalCount": 12,
        "RequestId": "52176f0d-29bd-4b2c-bb84-1670cbbeac0f"
    }
}
```

