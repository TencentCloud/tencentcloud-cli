**Example 1: 获取指定个数的视频内容识别模板**

获取序号从 0 开始，总共 10 个视频内容识别模板。

Input: 

```
tccli mps DescribeAIRecognitionTemplates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AIRecognitionTemplateSet": [
            {
                "Definition": 0,
                "Name": "abc",
                "Comment": "abc",
                "FaceConfigure": {
                    "Switch": "abc",
                    "Score": 0,
                    "DefaultLibraryLabelSet": [
                        "abc"
                    ],
                    "UserDefineLibraryLabelSet": [
                        "abc"
                    ],
                    "FaceLibrary": "abc"
                },
                "OcrFullTextConfigure": {
                    "Switch": "abc"
                },
                "OcrWordsConfigure": {
                    "Switch": "abc",
                    "LabelSet": [
                        "abc"
                    ]
                },
                "AsrFullTextConfigure": {
                    "Switch": "abc",
                    "SubtitleFormat": "abc",
                    "SourceLanguage": "abc"
                },
                "AsrWordsConfigure": {
                    "Switch": "abc",
                    "LabelSet": [
                        "abc"
                    ]
                },
                "TranslateConfigure": {
                    "Switch": "abc",
                    "SourceLanguage": "abc",
                    "DestinationLanguage": "abc",
                    "SubtitleFormat": "abc"
                },
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 获取模板 ID 为 30 的视频内容识别模板**



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
                "Definition": 0,
                "Name": "abc",
                "Comment": "abc",
                "FaceConfigure": {
                    "Switch": "abc",
                    "Score": 0,
                    "DefaultLibraryLabelSet": [
                        "abc"
                    ],
                    "UserDefineLibraryLabelSet": [
                        "abc"
                    ],
                    "FaceLibrary": "abc"
                },
                "OcrFullTextConfigure": {
                    "Switch": "abc"
                },
                "OcrWordsConfigure": {
                    "Switch": "abc",
                    "LabelSet": [
                        "abc"
                    ]
                },
                "AsrFullTextConfigure": {
                    "Switch": "abc",
                    "SubtitleFormat": "abc",
                    "SourceLanguage": "abc"
                },
                "AsrWordsConfigure": {
                    "Switch": "abc",
                    "LabelSet": [
                        "abc"
                    ]
                },
                "TranslateConfigure": {
                    "Switch": "abc",
                    "SourceLanguage": "abc",
                    "DestinationLanguage": "abc",
                    "SubtitleFormat": "abc"
                },
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

