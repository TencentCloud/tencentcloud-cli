**Example 1: 创建ScheduledSQL任务**

创建ScheduledSQL任务

Input: 

```
tccli cls CreateScheduledSql --cli-unfold-argument  \
    --EnableFlag 1 \
    --ProcessStartTime 1690515360000 \
    --Name scheduler_sql_delete_task \
    --DstResource.TopicId 6ef60bec-xxxx-xxxx-bb20-270359fbxxxx \
    --DstResource.Region ap-guangzhou \
    --DstResource.BizType 1 \
    --DstResource.MetricName pv \
    --ProcessTimeWindow @m-15m,@m \
    --ProcessPeriod 5 \
    --ScheduledSqlContent * | select count(*) as pv \
    --SrcTopicId 6ef60bec-xxxx-xxxx-bb20-270359fbxxxxx \
    --ProcessDelay 0 \
    --ProcessType 1 \
    --SrcTopicRegion ap-guangzhou \
    --ProcessEndTime 1690515440000
```

Output: 
```
{
    "Response": {
        "TaskId": "abdcebec-xxxx-xxxx-bb20-270359fb54a7",
        "RequestId": "6ef60bec-xxxx-xxxx-bb20-270359fb54a7"
    }
}
```

