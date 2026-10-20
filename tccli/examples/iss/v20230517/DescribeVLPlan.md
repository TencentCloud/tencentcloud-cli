**Example 1: 成功示例**



Input: 

```
tccli iss DescribeVLPlan --cli-unfold-argument  \
    --VLPlanId VPdc05*************************5eb
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
            "CreatedAt": "2026-07-27 17:10:26",
            "Describe": "明厨亮灶识别",
            "FileExpires": 7,
            "Name": "明厨亮灶识别计划",
            "UpdatedAt": "2026-07-27 17:10:26",
            "VLPlanId": "VPdc05*************************5eb",
            "VLTemplateId": "VTa911*************************6c2"
        },
        "RequestId": "7739d6e5-6e3e-4246-afe8-2fa7a01a9ca6"
    }
}
```

