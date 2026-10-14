**Example 1: 成功示例**



Input: 

```
tccli iss ModifyVLPlan --cli-unfold-argument  \
    --VLPlanId VP6d24c8b1157d4894b7c74a1ef30cf6a2 \
    --FileExpires 90 \
    --VLTemplateId VTa911*************************6c2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Callback": {
                "Enable": true,
                "Token": "************************************",
                "Url": "http://************************"
            },
            "ChannelCount": 0,
            "CreatedAt": "2026-07-28 15:49:06",
            "Describe": "明厨亮灶识别",
            "FileExpires": 90,
            "Name": "明厨亮灶识别计划",
            "UpdatedAt": "2026-07-28 15:51:16",
            "VLPlanId": "VP6d24*************************6a2",
            "VLTemplateId": "VTa911*************************6c2"
        },
        "RequestId": "e03b018a-5766-4c41-9738-eae93630057f"
    }
}
```

