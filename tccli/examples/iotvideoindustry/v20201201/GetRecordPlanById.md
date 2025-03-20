**Example 1: 根据录制计划ID获取录制计划**



Input: 

```
tccli iotvideoindustry GetRecordPlanById --cli-unfold-argument  \
    --PlanId plan-fyw1k9l5
```

Output: 
```
{
    "Response": {
        "Plan": {
            "PlanId": "plan-fyw1k9l5",
            "Name": "fyw1k9l5",
            "TimeTemplateId": "tgrp-fyw1k9l5",
            "TimeTemplateName": "fyw1k9l5",
            "EventId": 0,
            "RecordStorageTime": 1,
            "Devices": [
                {
                    "DeviceId": "99350367561320000005",
                    "ChannelId": "99350367561320000005"
                }
            ]
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

