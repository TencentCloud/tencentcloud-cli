**Example 1: 更新录制计划**



Input: 

```
tccli iotvideoindustry UpdateRecordPlan --cli-unfold-argument  \
    --PlanId plan-xxxxx \
    --Name xxxxxx \
    --TimeTemplateId tgrp-xxxxx \
    --EventId 1 \
    --IsModifyDevices 1 \
    --Devices.0.DeviceId xxxx
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

