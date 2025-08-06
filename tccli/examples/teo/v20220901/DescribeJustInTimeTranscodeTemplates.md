**Example 1: 获取转码模板**

根据模板名获取转码模板。

Input: 

```
tccli teo DescribeJustInTimeTranscodeTemplates --cli-unfold-argument  \
    --ZoneId zone-djuqmq \
    --Filters.0.Name template-name \
    --Filters.0.Values myTemplate \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TemplateSet": [
            {
                "TemplateId": "C1LZ7982VgTpYhJ7M",
                "TemplateName": "myTemplate",
                "Comment": "MyTranscodeTemplate",
                "Type": "Custom",
                "VideoStreamSwitch": "on",
                "AudioStreamSwitch": "on",
                "VideoTemplate": {
                    "Codec": "H.264",
                    "Fps": 24,
                    "FillType": "black",
                    "Bitrate": 2048,
                    "ResolutionAdaptive": "open",
                    "Width": 0,
                    "Height": 0
                },
                "AudioTemplate": {
                    "Codec": "libfdk_aac",
                    "AudioChannel": 2
                },
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

