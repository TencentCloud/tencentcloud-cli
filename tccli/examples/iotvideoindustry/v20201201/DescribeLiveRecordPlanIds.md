**Example 1: 获取直播录制计划列表**



Input: 

```
tccli iotvideoindustry DescribeLiveRecordPlanIds --cli-unfold-argument  \
    --TemplateId plan-001
```

Output: 
```
{
    "Response": {
        "RequestId": "1",
        "TotalCount": 3,
        "Plans": [
            {
                "PlanId": "planxxx-0",
                "PlanName": "namexxx0"
            },
            {
                "PlanId": "planxxx-1",
                "PlanName": "namexxx1"
            },
            {
                "PlanId": "planxxx-2",
                "PlanName": "namexxx2"
            }
        ]
    }
}
```

