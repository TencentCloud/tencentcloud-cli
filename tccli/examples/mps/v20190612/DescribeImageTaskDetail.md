**Example 1: 查询图片处理任务**



Input: 

```
tccli mps DescribeImageTaskDetail --cli-unfold-argument  \
    --TaskId 24******-WorkflowTask-***************tt6
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-04-30T06:26:49Z",
        "ImageTask": {
            "BeautyConfig": {
                "BeautyEffectItems": [
                    {
                        "ExtInfo": "",
                        "ResourcePath": "",
                        "Switch": "ON",
                        "Type": "Smooth",
                        "Value": 40
                    }
                ]
            }
        },
        "InputInfo": {
            "CosInputInfo": {
                "Bucket": "",
                "Object": "",
                "Region": ""
            },
            "S3InputInfo": null,
            "Type": "URL",
            "UrlInputInfo": {
                "Url": "http://***************.cos.ap-shanghai.tencentcos.cn/**********/01.jpeg"
            },
            "VODInputInfo": null
        },
        "Status": "PROCESSING",
        "TaskType": "WorkflowTask",
        "RequestId": "1610103f-dd39-44ca-90ea-e533219d9b53"
    }
}
```

