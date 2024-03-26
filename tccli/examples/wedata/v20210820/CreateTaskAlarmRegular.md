**Example 1: 创建集成任务告警规则**



Input: 

```
tccli wedata CreateTaskAlarmRegular --cli-unfold-argument  \
    --ProjectId abc \
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
        "RequestId": "abc",
        "AlarmId": 0
    }
}
```

