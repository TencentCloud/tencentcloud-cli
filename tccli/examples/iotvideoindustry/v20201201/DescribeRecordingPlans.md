**Example 1: 获取录制计划列表**



Input: 

```
tccli iotvideoindustry DescribeRecordingPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Plans": [
            {
                "PlanId": "plan-fyw1k9l5",
                "Name": "arvinxu_test",
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
            {
                "PlanId": "plan-c8obq4v0",
                "Name": "xx",
                "TimeTemplateId": "tgrp-fmwq1f1a",
                "TimeTemplateName": "工作日模板",
                "Channels": [],
                "RecordStorageTime": 3
            }
        ],
        "RequestId": "c70e67c3-c244-4b25-8518-1bdee3ccacab",
        "TotalCount": 2
    }
}
```

