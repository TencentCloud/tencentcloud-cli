**Example 1: 查询图片即时处理模板**

查询图片即时处理模板。

Input: 

```
tccli vod DescribeImageProcessingTemplates --cli-unfold-argument  \
    --Definitions 1008 1009
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ImageProcessingTemplateSet": [
            {
                "Definition": 1008,
                "Comment": "",
                "Name": "",
                "Type": "Custom",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Operations": [
                    {
                        "Type": "CenterCut",
                        "CenterCut": {
                            "Type": "Circle",
                            "Radius": 30
                        },
                        "Scale": {},
                        "Blur": {}
                    },
                    {
                        "Type": "Scale",
                        "Scale": {
                            "Type": "ShortEdgeFirst",
                            "ShortEdge": 100
                        },
                        "CenterCut": {},
                        "Blur": {}
                    }
                ]
            },
            {
                "Definition": 1009,
                "Comment": "",
                "Name": "",
                "Type": "Custom",
                "CreateTime": "2018-10-01T10:00:00Z",
                "Operations": [
                    {
                        "Type": "Scale",
                        "Scale": {
                            "Type": "WidthFirst",
                            "Width": 200
                        },
                        "CenterCut": {},
                        "Blur": {}
                    }
                ]
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

