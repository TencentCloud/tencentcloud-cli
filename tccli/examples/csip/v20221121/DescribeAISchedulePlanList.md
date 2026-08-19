**Example 1: 触发计划列表**



Input: 

```
tccli csip DescribeAISchedulePlanList --cli-unfold-argument  \
    --ScheduleId sched-a1b2c3d4 \
    --StartTime 1704067200000 \
    --EndTime 1704153600000 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PlanSet": [
            {
                "FireTime": 1775725829063,
                "TriggerId": "trigger-mock-001",
                "TriggerType": 1
            }
        ],
        "TotalCount": 3,
        "RequestId": "de1463ad-426b-4970-8458-68f1208a907b"
    }
}
```

