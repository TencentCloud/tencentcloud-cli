**Example 1: 获取雪碧图模板列表**



Input: 

```
tccli vod DescribeImageSpriteTemplates --cli-unfold-argument  \
    --Definitions 10001
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageSpriteTemplateSet": [
            {
                "Definition": 10001,
                "Type": "Custom",
                "Name": "雪碧图模板1",
                "Format": "jpg",
                "Comment": "test",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Height": 540,
                "SampleType": "Percent",
                "SampleInterval": 10,
                "ResolutionAdaptive": "open",
                "FillType": "black",
                "ColumnCount": 1,
                "RowCount": 1,
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

