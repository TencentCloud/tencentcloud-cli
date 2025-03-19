**Example 1: 查询智能字幕模板**



Input: 

```
tccli mps DescribeSmartSubtitleTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f89a1f41-1a26-4cda-9be1-2747cb44a045",
        "SmartSubtitleTemplateSet": [
            {
                "AliasName": "Generate_Chinese_And_English_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 212,
                "Name": "英文源视频-生成中英文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 2,
                "TranslateDstLanguage": "zh",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_Chinese_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 211,
                "Name": "英文源视频-生成中文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 1,
                "TranslateDstLanguage": "zh",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_English_Subtitle_For_English_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 200,
                "Name": "英文源视频-生成英文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "OFF",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "en"
            },
            {
                "AliasName": "Generate_Chinese_And_English_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 122,
                "Name": "中文源视频-生成中英文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 2,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "Generate_English_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 121,
                "Name": "中文源视频-生成英文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 1,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "ON",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "Generate_Chinese_Subtitle_For_Chinese_Video",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-11T15:41:29+08:00",
                "Definition": 100,
                "Name": "中文源视频-生成中文字幕",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "en",
                "TranslateSwitch": "OFF",
                "Type": "Preset",
                "UpdateTime": "2025-02-11T15:41:29+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-03-04T18:18:35+08:00",
                "Definition": 202226,
                "Name": "aaaaa",
                "SubtitleFormat": "",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-03-04T18:18:35+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "hwd-390af315ba0c31545156",
                    "Switch": "ON"
                },
                "AsrHotWordsLibraryName": "ValidName",
                "Comment": "",
                "CreateTime": "2025-02-21T16:26:37+08:00",
                "Definition": 201309,
                "Name": "0221",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T16:26:37+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "",
                    "Switch": "OFF"
                },
                "AsrHotWordsLibraryName": "",
                "Comment": "",
                "CreateTime": "2025-02-21T16:13:06+08:00",
                "Definition": 201308,
                "Name": "0221",
                "SubtitleFormat": "vtt",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T16:13:06+08:00",
                "VideoSrcLanguage": "zh"
            },
            {
                "AliasName": "",
                "AsrHotWordsConfigure": {
                    "LibraryId": "hwd-f1d930ebc6d9a7d910",
                    "Switch": "ON"
                },
                "AsrHotWordsLibraryName": "HotwordsName1",
                "Comment": "",
                "CreateTime": "2025-02-21T16:08:45+08:00",
                "Definition": 201307,
                "Name": "0221",
                "SubtitleFormat": "",
                "SubtitleType": 0,
                "TranslateDstLanguage": "",
                "TranslateSwitch": "OFF",
                "Type": "Custom",
                "UpdateTime": "2025-02-21T17:50:15+08:00",
                "VideoSrcLanguage": "zh"
            }
        ],
        "TotalCount": 21
    }
}
```

