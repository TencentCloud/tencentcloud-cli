**Example 1: Getting a specified number of video content recognition templates**

This example shows you how to get 10 video content recognition templates with the serial number starting from 0.

Input: 

```
tccli vod DescribeAIRecognitionTemplates --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "AIRecognitionTemplateSet": [
            {
                "Definition": 30,
                "Name": "Template 1",
                "Comment": "Intelligent recognition template",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "ON"
                },
                "FaceConfigure": {
                    "Switch": "ON",
                    "FaceLibrary": "All",
                    "LabelSet": []
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON"
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            },
            {
                "Definition": 31,
                "Name": "Template 2",
                "Comment": "Intelligent recognition template",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "OFF"
                },
                "FaceConfigure": {
                    "Switch": "OFF",
                    "FaceLibrary": "All",
                    "LabelSet": []
                },
                "OcrFullTextConfigure": {
                    "Switch": "OFF"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "AsrFullTextConfigure": {
                    "Switch": "OFF"
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "CreateTime": "2019-01-01T11:00:00Z",
                "UpdateTime": "2019-01-01T12:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

**Example 2: Getting the video content recognition template whose template ID is 30**

This example shows you how to get 10 video content recognition templates with the serial number starting from 0.

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
                "Name": "Template 1",
                "Comment": "Intelligent recognition template",
                "HeadTailConfigure": {
                    "Switch": "ON"
                },
                "SegmentConfigure": {
                    "Switch": "ON"
                },
                "FaceConfigure": {
                    "Switch": "ON",
                    "FaceLibrary": "All",
                    "LabelSet": []
                },
                "OcrFullTextConfigure": {
                    "Switch": "ON"
                },
                "OcrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "AsrFullTextConfigure": {
                    "Switch": "ON"
                },
                "AsrWordsConfigure": {
                    "Switch": "OFF",
                    "LabelSet": null
                },
                "ObjectConfigure": {
                    "Switch": "ON",
                    "ObjectLibrary": "All"
                },
                "CreateTime": "2019-01-01T12:00:00Z",
                "UpdateTime": "2019-01-01T16:00:00Z"
            }
        ],
        "RequestId": "19ae8d8e-dce3-4151-9d4b-5594384987a9"
    }
}
```

