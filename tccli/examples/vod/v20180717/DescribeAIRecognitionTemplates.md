**Example 1: 获取指定个数的音视频内容识别模板**

获取序号从 0 开始，总共 10 个音视频内容识别模板。

Input: 

```
tccli vod DescribeAIRecognitionTemplates --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AIRecognitionTemplateSet": [
            {
                "Definition": 30,
                "Name": "模板1",
                "Comment": "智能识别模板",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "ON"
                },
                "FaceConfigure": {
                    "Switch": "ON",
                    "FaceLibrary": "All",
                    "Score": 0,
                    "UserDefineLibraryLabelSet": [],
                    "DefaultLibraryLabelSet": []
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
                    "SrcLanguage": "",
                    "SubtitleFormat": "",
                    "SubtitleFormats": []
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "ScreenshotInterval": 10,
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "模板2",
                "Comment": "智能识别模板",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "OFF"
                },
                "FaceConfigure": {
                    "Switch": "OFF",
                    "FaceLibrary": "All",
                    "Score": 0,
                    "UserDefineLibraryLabelSet": [],
                    "DefaultLibraryLabelSet": []
                },
                "OcrFullTextConfigure": {
                    "Switch": "OFF"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "AsrFullTextConfigure": {
                    "Switch": "OFF",
                    "SrcLanguage": "",
                    "SubtitleFormat": "",
                    "SubtitleFormats": []
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "ScreenshotInterval": 10,
                "CreateTime": "2019-01-01T11:00:00Z",
                "UpdateTime": "2019-01-01T12:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

**Example 2: 获取模板 ID 为 30 的音视频内容识别模板**

获取模板 ID 为 30 的音视频内容识别模板

Input: 

```
tccli vod DescribeAIRecognitionTemplates --cli-unfold-argument  \
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
                "Comment": "智能识别模板",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "ON"
                },
                "FaceConfigure": {
                    "Switch": "ON",
                    "FaceLibrary": "All",
                    "Score": 0,
                    "UserDefineLibraryLabelSet": [],
                    "DefaultLibraryLabelSet": []
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
                    "SrcLanguage": "",
                    "SubtitleFormat": "",
                    "SubtitleFormats": []
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": []
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "ScreenshotInterval": 10,
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

