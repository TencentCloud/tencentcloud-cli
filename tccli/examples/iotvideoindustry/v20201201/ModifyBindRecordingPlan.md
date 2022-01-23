**Example 1: 更新录制计划绑定的通道**



Input: 

```
tccli iotvideoindustry ModifyBindRecordingPlan --cli-unfold-argument  \
    --Channels.0.ChannelId xx \
    --Channels.0.DeviceId xxx \
    --Type 1 \
    --PlanId plan-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

