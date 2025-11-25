**Example 1: 查询所有图片处理模板**

查询包括预设模板和自定义模板在内的所有图片处理模板信息

Input: 

```
tccli mps DescribeProcessImageTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ProcessImageTemplateSet": [
            {
                "Comment": "",
                "CreateTime": "2025-11-11T02:40:24Z",
                "Definition": 20180,
                "Name": "",
                "ProcessImageConfig": {
                    "EncodeConfig": {
                        "Format": "JPEG",
                        "Quality": 80
                    },
                    "EnhanceConfig": {
                        "ImageQualityEnhance": {
                            "Switch": "ON",
                            "Type": "weak"
                        }
                    }
                },
                "Type": "Custom",
                "UpdateTime": "2025-11-11T02:40:24Z"
            }
        ],
        "RequestId": "6781d678-c8d0-4af3-87c1-f31050c8a76a",
        "TotalCount": 1
    }
}
```

