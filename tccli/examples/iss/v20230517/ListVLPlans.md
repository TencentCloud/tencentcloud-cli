**Example 1: 成功示例**



Input: 

```
tccli iss ListVLPlans --cli-unfold-argument  \
    --Name 明厨亮灶识别计划 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Callback": {
                    "Enable": true,
                    "Token": "************************************",
                    "Url": "http://************************"
                },
                "ChannelCount": 0,
                "CreatedAt": "2026-07-27 17:19:15",
                "Describe": "明厨亮灶识别",
                "FileExpires": 7,
                "Name": "明厨亮灶识别计划",
                "UpdatedAt": "2026-07-27 17:19:15",
                "VLPlanId": "VP7219*************************6f1",
                "VLTemplateId": "VTa911*************************6c2"
            }
        ],
        "TotalCount": 1,
        "RequestId": "16b41217-9532-4fd8-86e7-b333cca1177b"
    }
}
```

