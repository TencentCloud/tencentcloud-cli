**Example 1: 修改ScheduledSQL任务**

修改ScheduledSQL任务

Input: 

```
tccli cls ModifyScheduledSql --cli-unfold-argument  \
    --EnableFlag 1 \
    --TaskId 6ef60bec-0242-43af-bb20-270359fxxxxx \
    --DstResource.TopicId 6ef60bec-0242-43af-bb20-270359fxxxxx \
    --DstResource.Region ap-guangzhou \
    --DstResource.BizType 1 \
    --DstResource.MetricName pv \
    --ProcessTimeWindow @m-15m,@m \
    --ProcessPeriod 5 \
    --ScheduledSqlContent * | select count(*) as pv \
    --SrcTopicId 6ef60bec-0242-43af-bb20-270359fbxxxx \
    --ProcessDelay 0 \
    --SrcTopicRegion ap-guangzhou \
    --Name task
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54ax"
    }
}
```

