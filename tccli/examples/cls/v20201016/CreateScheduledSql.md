**Example 1: 创建ScheduledSQL任务**

创建ScheduledSQL任务

Input: 

```
tccli cls CreateScheduledSql --cli-unfold-argument  \
    --EnableFlag 1 \
    --ProcessStartTime 1 \
    --Name abc1 \
    --DstResource.TopicId abc \
    --DstResource.Region abc \
    --ProcessTimeWindow abc \
    --ProcessPeriod 0 \
    --ScheduledSqlContent abc \
    --SrcTopicId abc \
    --ProcessDelay 0 \
    --ProcessType 0 \
    --SrcTopicRegion abc \
    --ProcessEndTime 1
```

Output: 
```
{
    "Response": {
        "TaskId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

