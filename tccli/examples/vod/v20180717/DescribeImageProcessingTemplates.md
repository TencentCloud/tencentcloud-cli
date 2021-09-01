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
                        "Type": "CenterCut"
                    },
                    {
                        "Type": "Scale"
                    }
                ]
            },
            {
                "Definition": 1009,
                "Operations": [
                    {
                        "Type": "Scale"
                    }
                ]
            }
        ],
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

