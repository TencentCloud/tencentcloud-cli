**Example 1: 成功示例**



Input: 

```
tccli iss CreateVLTemplate --cli-unfold-argument  \
    --AIModel ivc-vl-1.0 \
    --Name 测试模板 \
    --Prompt 图片中有什么 \
    --AnalysisMode image \
    --Times.0.BeginTime 00:00:00 \
    --Times.0.EndTime 10:00:00 \
    --Times.0.WeekDay 1 \
    --ImageConfig.Type 1 \
    --ImageConfig.Interval 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "AIModel": "ivc-vl-1.0",
            "AnalysisMode": "image",
            "CreatedAt": "2026-08-17 17:23:41",
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
            "UpdatedAt": "2026-08-17 17:23:41",
            "VLTemplateId": "VT58c*************************04e3"
        },
        "RequestId": "1676edea-cb77-4629-968b-197833ba8d87"
    }
}
```

