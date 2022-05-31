**Example 1: 获转动图模板列表**



Input: 

```
tccli vod DescribeAnimatedGraphicsTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AnimatedGraphicsTemplateSet": [
            {
                "Definition": 10001,
                "Name": "转动图模板1",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Height": 540,
                "Width": 960,
                "Format": "gif",
                "Fps": 30,
                "Quality": 75,
                "ResolutionAdaptive": "open",
                "Type": "Custom",
                "Comment": ""
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

