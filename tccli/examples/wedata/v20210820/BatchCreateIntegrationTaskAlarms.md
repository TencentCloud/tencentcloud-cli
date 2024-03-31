**Example 1: BatchCreateIntegrationTaskAlarms**



Input: 

```
tccli wedata BatchCreateIntegrationTaskAlarms --cli-unfold-argument  \
    --ProjectId abc \
    --TaskIds 123 124 \
    --TaskAlarmInfo.AlarmRecipientName abc \
    --TaskAlarmInfo.TaskId abc \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.ProjectId abc \
    --TaskAlarmInfo.TaskType 1 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.Id abc \
    --TaskAlarmInfo.Creater abc \
    --TaskAlarmInfo.RegularId abc \
    --TaskAlarmInfo.RegularName abc \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.AlarmRecipientId abc \
    --TaskAlarmInfo.AlarmWay abc \
    --TaskAlarmInfo.AlarmLevel 1 \
    --TaskAlarmInfo.RegularStatus 1
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "abc"
    }
}
```

