**Example 1: CreateRecordPlan**



Input: 

```
tccli iotvideoindustry CreateRecordPlan --cli-unfold-argument  \
    --Name myPlan \
    --TimeTemplateId template-xxxxx \
    --EventId 1 \
    --Devices.0.DeviceId xxxx
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

