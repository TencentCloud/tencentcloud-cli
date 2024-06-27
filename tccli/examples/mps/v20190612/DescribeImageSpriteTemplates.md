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
                "Definition": 1,
                "Type": "abc",
                "Name": "abc",
                "Width": 1,
                "Height": 1,
                "ResolutionAdaptive": "abc",
                "SampleType": "abc",
                "SampleInterval": 1,
                "RowCount": 1,
                "ColumnCount": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "FillType": "abc",
                "Comment": "abc",
                "Format": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

