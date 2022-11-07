**Example 1: BatchCreateIntegrationTaskAlarms**



Input: 

```
tccli wedata BatchCreateIntegrationTaskAlarms --cli-unfold-argument  \
    --ProjectId xx \
    --TaskIds 123 124 \
    --TaskAlarmInfo.AlarmRecipientName xx \
    --TaskAlarmInfo.TaskId xx \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.ProjectId xx \
    --TaskAlarmInfo.TaskType 1 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.Id xx \
    --TaskAlarmInfo.Creater xx \
    --TaskAlarmInfo.RegularId xx \
    --TaskAlarmInfo.RegularName xx \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.AlarmRecipientId xx \
    --TaskAlarmInfo.AlarmWay xx \
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
        "RequestId": "xx"
    }
}
```

