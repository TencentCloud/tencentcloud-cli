**Example 1: 获取水印模板**



Input: 

```
tccli vod DescribeWatermarkTemplates --cli-unfold-argument  \
    --Definitions 1001 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WatermarkTemplateSet": [
            {
                "Definition": 1001,
                "Type": "image",
                "Name": "示例结构体待完善",
                "Comment": "测试模板",
                "XPos": "10%",
                "YPos": "10%",
                "ImageTemplate": {
                    "ImageUrl": "http://1256768367.vod2.myqcloud.com/8b0dd2b5vodcq1256768367/4d27b39f5285890783754292994/aa.jpeg",
                    "Width": "80%",
                    "Height": "80%",
                    "RepeatType": "repeat",
                    "Transparency": 0
                },
                "TextTemplate": {
                    "FontType": "arial.ttf",
                    "FontSize": "16px",
                    "FontColor": "0xFF0000",
                    "FontAlpha": 1
                },
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

