**Example 1: 更新录制计划绑定的通道**



Input: 

```
tccli iotvideoindustry ModifyBindRecordingPlan --cli-unfold-argument  \
    --Channels.0.ChannelId 99870353841320000007_99870353841320000007 \
    --Channels.0.DeviceId 99870353841320000007_99870353841320000007 \
    --Type 1 \
    --PlanId plan-zn3ro30w
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

