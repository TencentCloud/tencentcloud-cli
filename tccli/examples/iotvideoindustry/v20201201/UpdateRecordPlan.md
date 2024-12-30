**Example 1: 更新录制计划**



Input: 

```
tccli iotvideoindustry UpdateRecordPlan --cli-unfold-argument  \
    --PlanId plan-allday \
    --Name allday \
    --TimeTemplateId tgrp-allday \
    --EventId 1 \
    --IsModifyDevices 1 \
    --Devices.0.DeviceId 99870353841320000007_99870353841320000007
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "Status": "OK"
    }
}
```

