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
                "Definition": 10,
                "Type": "Preset",
                "Name": "雪碧图模板",
                "Width": 142,
                "Height": 80,
                "ResolutionAdaptive": "close",
                "SampleType": "Time",
                "SampleInterval": 10,
                "RowCount": 10,
                "ColumnCount": 10,
                "CreateTime": "2019-07-25T22:24:36Z",
                "UpdateTime": "2019-07-25T22:24:36Z",
                "FillType": "stretch",
                "Comment": "雪碧图模板说明",
                "Format": "jpg"
            }
        ],
        "RequestId": "008xxxxx-xxxx-xxxx-xxxx-xxxxxxxxaa48"
    }
}
```

