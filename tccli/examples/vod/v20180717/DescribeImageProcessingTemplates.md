**Example 1: 读取多个模板**



Input: 

```
tccli vod DescribeImageProcessingTemplates --cli-unfold-argument  \
    --Definitions 1008 1009
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageProcessingTemplateSet": [
            {
                "Definition": 1008,
                "Operations": [
                    {
                        "Type": "CenterCut",
                        "ImageCenterCut": {
                            "Type": "Circle",
                            "Radius": 30
                        }
                    },
                    {
                        "Type": "Scale",
                        "ImageScale": {
                            "Type": "ShortEdgeFirst",
                            "ShortEdge": 100
                        }
                    }
                ]
            },
            {
                "Definition": 1009,
                "Operations": [
                    {
                        "Type": "Scale",
                        "ImageScale": {
                            "Type": "WidthFirst",
                            "Width": 200
                        }
                    }
                ]
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

