**Example 1: 创建直播录制计划**



Input: 

```
tccli iotvideoindustry CreateLiveRecordPlan --cli-unfold-argument  \
    --TemplateId tgrp-cyjjxyyyds \
    --PlanType 1 \
    --PlanName 固定直播录制008 \
    --LiveChannelIds channel-01 channel-02
```

Output: 
```
{
    "Response": {
        "PlanId": "LivePlanxxx",
        "RequestId": "1"
    }
}
```

