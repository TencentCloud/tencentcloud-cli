**Example 1: 根据ID查询录制计划详情**



Input: 

```
tccli iotvideoindustry DescribeRecordingPlanById --cli-unfold-argument  \
    --PlanId plan-fyw1k9l5
```

Output: 
```
{
    "Response": {
        "Plan": {
            "PlanId": "plan-fyw1k9l5",
            "Name": "test",
            "TimeTemplateId": "tgrp-jfs89ahg",
            "TimeTemplateName": "全天候模板",
            "Channels": [
                {
                    "DeviceId": "99576636581320000330_99576636581320000330",
                    "ChannelId": "99576636581320000330_99576636581320000330"
                }
            ],
            "RecordStorageTime": 5
        },
        "RequestId": "86059248-9d5d-4f7d-8fec-1b7ac3b44867"
    }
}
```

