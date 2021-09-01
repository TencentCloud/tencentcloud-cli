**Example 1: 根据录制计划ID获取录制计划**



Input: 

```
tccli iotvideoindustry GetRecordPlanById --cli-unfold-argument  \
    --PlanId plan-xxxx
```

Output: 
```
{
    "Response": {
        "Plan": {
            "PlanId": "plan-xxxxx",
            "Name": "xxx",
            "TimeTemplateId": "tgrp-xxxx",
            "TimeTemplateName": "xxxx",
            "EventId": 0,
            "Devices": [
                {
                    "DeviceId": "dev02"
                }
            ]
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

