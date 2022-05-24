**Example 1: 获取雪碧图模板列表**



Input: 

```
tccli mps DescribeImageSpriteTemplates --cli-unfold-argument  \
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
                "Name": "雪碧图模板1",
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z",
                "Height": 540,
                "SampleType": "Percent",
                "SampleInterval": 10,
                "RowCount": 10,
                "ColumnCount": 5,
                "ResolutionAdaptive": "xx",
                "FillType": "black",
                "Comment": "",
                "Type": "Preset",
                "Width": 960
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

