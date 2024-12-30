**Example 1: 获取设备绑定的录制计划**



Input: 

```
tccli iotvideoindustry GetRecordPlanByDev --cli-unfold-argument  \
    --DeviceId dev001
```

Output: 
```
{
    "Response": {
        "Plan": {
            "PlanId": "plan-allday",
            "Name": "myallday",
            "TimeTemplateId": "tgrp-fmwq1f1a",
            "TimeTemplateName": "allday",
            "EventId": 0,
            "RecordStorageTime": 1,
            "Devices": [
                {
                    "DeviceId": "dev001"
                }
            ]
        },
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

