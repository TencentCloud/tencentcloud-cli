**Example 1: 查询图片异步处理模板列表**



Input: 

```
tccli vod DescribeProcessImageAsyncTemplates --cli-unfold-argument  \
    --SubAppId 221073 \
    --Definitions 7
```

Output: 
```
{
    "Response": {
        "ProcessImageAsyncTemplateSet": [
            {
                "Comment": "testcomment",
                "CreateTime": "2026-01-20T03:02:33Z",
                "Definition": 7,
                "Name": "test3",
                "ProcessImageConfigure": {
                    "EncodeConfig": {
                        "Format": "PNG",
                        "Quality": 100
                    },
                    "EnhanceConfig": {
                        "AdvancedSuperResolution": {
                            "Height": 720,
                            "Mode": "percent",
                            "Percent": 2,
                            "Switch": "ON",
                            "Type": "standard",
                            "Width": 1280
                        },
                        "ColorEnhance": {
                            "Switch": "ON",
                            "Type": "weak"
                        },
                        "Denoise": {
                            "Switch": "ON",
                            "Type": "weak"
                        },
                        "FaceEnhance": {
                            "Intensity": 1,
                            "Switch": "ON"
                        },
                        "ImageQualityEnhance": {
                            "Switch": "ON",
                            "Type": "weak"
                        },
                        "LowLightEnhance": {
                            "Switch": "ON",
                            "Type": "normal"
                        },
                        "SharpEnhance": {
                            "Intensity": 1,
                            "Switch": "ON"
                        },
                        "SuperResolution": null
                    }
                },
                "Type": "Custom",
                "UpdateTime": "2026-01-26T09:21:49Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "08cfed0c-2b5a-41bf-b0dd-b1985db203d8"
    }
}
```

