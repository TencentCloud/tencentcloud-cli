**Example 1: 获取指定个数的音视频内容分析模板**

指定从序号 0 开始，总共 10 个音视频内容分析模板，包括系统默认音视频内容分析模板。

Input: 

```
tccli vod DescribeAIAnalysisTemplates --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AIAnalysisTemplateSet": [
            {
                "Definition": 30,
                "Name": "模板1",
                "Comment": "智能分析模板",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "HighlightConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON",
                    "ScreenshotInterval": 1
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "模板2",
                "Comment": "智能分析模板",
                "ClassificationConfigure": {
                    "Switch": "OFF"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "HighlightConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON",
                    "ScreenshotInterval": 1
                },
                "CreateTime": "2019-01-01T13:00:00Z",
                "UpdateTime": "2019-01-01T17:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

**Example 2: 获取模板 ID 为 30 的音视频内容分析模板**



Input: 

```
tccli vod DescribeAIAnalysisTemplates --cli-unfold-argument  \
    --Definitions 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AIAnalysisTemplateSet": [
            {
                "Definition": 30,
                "Name": "模板1",
                "Comment": "智能分析模板",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
                    "Switch": "ON"
                },
                "HighlightConfigure": {
                    "Switch": "ON"
                },
                "FrameTagConfigure": {
                    "Switch": "ON",
                    "ScreenshotInterval": 1
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

