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
                "Name": "模板1",
                "Type": "Preset",
                "Comment": "智能识别模板",
                "FaceConfigure": {
                    "Switch": "ON",
                    "Score": 0.0,
                    "FaceLibrary": "All",
                    "DefaultLibraryLabelSet": [
                        "xx"
                    ],
                    "UserDefineLibraryLabelSet": [
                        "xx"
                    ]
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": [
                        "xx"
                    ]
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON",
                    "SubtitleFormat": "xx"
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": [
                        "xx"
                    ]
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

**Example 2: 获取指定个数的视频内容识别模板**

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
                "Definition": 30,
                "Name": "模板1",
                "Comment": "智能识别模板",
                "Type": "Preset",
                "FaceConfigure": {
                    "Switch": "ON",
                    "Score": 0.0,
                    "FaceLibrary": "All",
                    "DefaultLibraryLabelSet": [
                        "xx"
                    ],
                    "UserDefineLibraryLabelSet": [
                        "xx"
                    ]
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON",
                    "SubtitleFormat": "xx"
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

