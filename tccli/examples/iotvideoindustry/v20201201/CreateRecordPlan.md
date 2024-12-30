**Example 1: CreateRecordPlan**



Input: 

```
tccli iotvideoindustry CreateRecordPlan --cli-unfold-argument  \
    --Name myPlan \
    --TimeTemplateId template-001 \
    --EventId 1 \
    --Devices.0.DeviceId 99870353841320000007_99870353841320000007
```

Output: 
```
{
    "Response": {
        "PlanId": "plan-001",
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

