**Example 1: 成功示例**



Input: 

```
tccli iss DescribeVLTemplate --cli-unfold-argument  \
    --VLTemplateId VT58c*************************04e3
```

Output: 
```
{
    "Response": {
        "Data": {
            "AIModel": "ivc-vl-1.0",
            "AnalysisMode": "image",
            "CreatedAt": "2026-08-17 17:23:42",
            "Describe": "",
            "ImageConfig": {
                "Interval": 10,
                "MultiMode": null,
                "Type": 1
            },
            "Name": "测试模板",
            "Prompt": "图片中有什么",
            "Times": [
                {
                    "BeginTime": "00:00:00",
                    "EndTime": "10:00:00",
                    "WeekDay": 1
                }
            ],
            "UpdatedAt": "2026-08-17 17:23:42",
            "VLTemplateId": "VT58c*************************04e3"
        },
        "RequestId": "6f7a4ac9-7fea-4418-a715-f04fc0a66c83"
    }
}
```

