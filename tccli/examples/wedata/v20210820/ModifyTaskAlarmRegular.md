**Example 1: 修改任务告警规则**



Input: 

```
tccli wedata ModifyTaskAlarmRegular --cli-unfold-argument  \
    --ProjectId xx \
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
    --TaskAlarmInfo.RegularStatus 1 \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

