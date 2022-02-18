**Example 1: CreateRecordPlan**



Input: 

```
tccli iotvideoindustry CreateRecordingPlan --cli-unfold-argument  \
    --Name myPlan \
    --TimeTemplateId template-xxxxx \
    --RecordStorageTime 30 \
    --Channels.0.ChannelId xx \
    --Channels.0.DeviceId xx
```

Output: 
```
{
    "Response": {
        "PlanId": "plan-xxxx",
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

**Example 2: 创建录制计划**



Input: 

```
tccli iotvideoindustry CreateRecordingPlan --cli-unfold-argument  \
    --TimeTemplateId tgrp-fmwq1f1a \
    --RecordStorageTime 3 \
    --Name xxxxx
```

Output: 
```
{
    "Response": {
        "PlanId": "plan-1u9z7ugo",
        "RequestId": "8ae1b70c-bf32-4cb0-a15e-dc2af40fa035"
    }
}
```

