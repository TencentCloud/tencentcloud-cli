**Example 1: 获取模板 ID 为 30 的视频内容识别模板**



Input: 

```
tccli mps DescribeAIRecognitionTemplates --cli-unfold-argument  \
    --Definitions 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AIRecognitionTemplateSet": [
            {
                "Definition": 30,
                "Name": "Presetting Template30",
                "Comment": "默认模板，打开所有识别开关，只使用户自定义库且不带过滤标签",
                "Type": "Preset",
                "FaceConfigure": {
                    "Switch": "ON",
                    "Score": 95,
                    "DefaultLibraryLabelSet": [],
                    "UserDefineLibraryLabelSet": [],
                    "FaceLibrary": "UserDefine"
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "ON",
                    "LabelSet": []
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON",
                    "SubtitleFormat": "vtt",
                    "SourceLanguage": "zh"
                },
                "AsrWordsConfigure": {
                    "Switch": "ON",
                    "LabelSet": []
                },
                "TranslateConfigure": {
                    "Switch": "OFF",
                    "SourceLanguage": "en",
                    "DestinationLanguage": "zh",
                    "SubtitleFormat": "vtt"
                },
                "CreateTime": "2019-06-13T11:07:07+08:00",
                "UpdateTime": "2020-01-06T08:21:46+08:00"
            }
        ],
        "RequestId": "9a12345af0-4a9c-ae02-704f3d5a8040"
    }
}
```

