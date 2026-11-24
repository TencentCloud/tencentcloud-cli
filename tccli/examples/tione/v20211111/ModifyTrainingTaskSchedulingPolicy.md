**Example 1: 修改训练任务调度策略**



Input: 

```
tccli tione ModifyTrainingTaskSchedulingPolicy --cli-unfold-argument  \
    --TrainingTaskId train-1440591021184975616 \
    --CrossResourceGroupScheduling False \
    --SchedulePolicy.PriorityClass p0
```

Output: 
```
{
    "Response": {
        "RequestId": "78f4f261-dde6-4cee-8747-fe66c165b3e3"
    }
}
```

