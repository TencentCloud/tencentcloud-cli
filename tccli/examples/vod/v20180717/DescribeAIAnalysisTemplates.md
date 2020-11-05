**Example 1: Getting a specified number of video content analysis templates**

This example shows you how to get 10 video content analysis templates with the serial number starting from 0, including system default ones.

Input: 

```
tccli vod DescribeAIAnalysisTemplates --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AIAnalysisTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Comment": "Intelligent analysis template",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
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
                "Name": "Template 2",
                "Comment": "Intelligent analysis template",
                "ClassificationConfigure": {
                    "Switch": "OFF"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
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

**Example 2: Getting the video content analysis template whose template ID is 30**

This example shows you how to get 10 video content analysis templates with the serial number starting from 0, including system default ones.

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
                "Name": "Template 1",
                "Comment": "Intelligent analysis template",
                "ClassificationConfigure": {
                    "Switch": "ON"
                },
                "TagConfigure": {
                    "Switch": "ON"
                },
                "CoverConfigure": {
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

