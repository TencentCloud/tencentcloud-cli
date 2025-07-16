**Example 1: 获取即时转码模板列表**



Input: 

```
tccli vod DescribeJustInTimeTranscodeTemplates --cli-unfold-argument  \
    --Names testtempaltename
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "JustInTimeTranscodeTemplateSet": [
            {
                "Type": "Custom",
                "Name": "MyTemplateName",
                "Comment": "comment",
                "VideoConfigure": {
                    "Width": 720,
                    "Height": 1080,
                    "Bitrate": 10000,
                    "ResolutionAdaptive": "open"
                },
                "WatermarkConfigure": {
                    "Switch": "ON",
                    "Url": "http://example.com/watermark.png",
                    "Width": "10%",
                    "Height": "10%",
                    "XPos": "10%",
                    "YPos": "10%"
                }
            }
        ],
        "RequestId": "58759c60-aceb-4b02-b0ed-6c62bfea88cc"
    }
}
```

