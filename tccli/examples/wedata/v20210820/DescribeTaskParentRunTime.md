**Example 1: 示例1**

示例1

Input: 

```
tccli wedata DescribeTaskParentRunTime --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --CycleType HOUR_CYCLE \
    --CycleStep 1 \
    --CurRunDate 2024-01-09 01:00:00 \
    --DelayTime 0 \
    --CrontabExpression 0 0 0-23/1 * * ? \
    --ParentConfigs.0.ParentId 20240103163227274 \
    --ParentConfigs.0.StartTime 2024-01-09 00:00:00 \
    --ParentConfigs.0.EndTime 2099-12-31 23:59:59 \
    --ParentConfigs.0.CycleType HOUR_CYCLE \
    --ParentConfigs.0.CycleStep 1 \
    --ParentConfigs.0.SubordinateCyclicConfig CURRENT_HOUR \
    --ParentConfigs.0.PollingNullStrategy WAITING \
    --ParentConfigs.0.MainCyclicConfig HOUR \
    --ParentConfigs.0.DelayTime 3 \
    --ParentConfigs.0.ExecutionStartTime 2:00 \
    --ParentConfigs.0.ExecutionEndTime 22:59
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "InstanceCount": 1,
                "InstanceRunDateList": [
                    "2024-01-09 01:00:00"
                ],
                "ParentId": "20240103163227274",
                "SchedulerDescription": null
            }
        ],
        "RequestId": "25addd3d-bbdf-48c9-bebb-b3180fb66120"
    }
}
```

