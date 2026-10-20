**Example 1: 成功示例**



Input: 

```
tccli iss CreateVLPlan --cli-unfold-argument  \
    --Name 明厨亮灶识别计划 \
    --VLTemplateId VTa911*************************6c2 \
    --Describe 明厨亮灶识别 \
    --FileExpires 7 \
    --Callback.Url http://************************ \
    --Callback.Token ************************************
```

Output: 
```
{
    "Response": {
        "Data": {
            "Callback": {
                "Enable": true,
                "Token": "************************************",
                "Url": "*******************************"
            },
            "ChannelCount": 0,
            "CreatedAt": "2026-07-28 15:49:05",
            "Describe": "明厨亮灶识别",
            "FileExpires": 7,
            "Name": "明厨亮灶识别计划",
            "UpdatedAt": "2026-07-28 15:49:05",
            "VLPlanId": "VP6d24*************************6a2",
            "VLTemplateId": "VTa911*************************6c2"
        },
        "RequestId": "c50a3279-5c94-429a-a709-c2f80efa77c3"
    }
}
```

