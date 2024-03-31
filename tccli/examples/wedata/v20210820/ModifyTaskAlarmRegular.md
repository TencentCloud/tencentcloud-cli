**Example 1: 修改任务告警规则**



Input: 

```
tccli wedata ModifyTaskAlarmRegular --cli-unfold-argument  \
    --Id abc \
    --TaskAlarmInfo.Id abc \
    --TaskAlarmInfo.TaskId abc \
    --TaskAlarmInfo.RegularId abc \
    --TaskAlarmInfo.RegularName abc \
    --TaskAlarmInfo.RegularStatus 1 \
    --TaskAlarmInfo.AlarmLevel 1 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.AlarmWay abc \
    --TaskAlarmInfo.AlarmRecipientId abc \
    --TaskAlarmInfo.TaskType 1 \
    --TaskAlarmInfo.ProjectId abc \
    --TaskAlarmInfo.Creater abc \
    --TaskAlarmInfo.AlarmRecipientName abc \
    --TaskAlarmInfo.AlarmIndicatorDesc abc \
    --TaskAlarmInfo.Operator 1 \
    --TaskAlarmInfo.NodeId abc \
    --TaskAlarmInfo.NodeName abc \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Id abc \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicator 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicatorDesc abc \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.TriggerType 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.EstimatedTime 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Operator 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicatorUnit abc \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Duration 0 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.DurationUnit abc \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.MaxTimes 0 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Threshold 0 \
    --TaskAlarmInfo.AlarmRecipientType 1 \
    --TaskAlarmInfo.QuietPeriods.0.DaysOfWeek 1 \
    --TaskAlarmInfo.QuietPeriods.0.StartTime abc \
    --TaskAlarmInfo.QuietPeriods.0.EndTime abc \
    --TaskAlarmInfo.WeComHook abc \
    --TaskAlarmInfo.UpdateTime abc \
    --TaskAlarmInfo.OperatorUin abc \
    --TaskAlarmInfo.TaskCount 0 \
    --TaskAlarmInfo.MonitorType 0 \
    --TaskAlarmInfo.MonitorObjectIds abc \
    --TaskAlarmInfo.LatestAlarmInstanceId abc \
    --TaskAlarmInfo.LatestAlarmTime abc \
    --TaskAlarmInfo.Description abc \
    --TaskAlarmInfo.LarkWebHooks abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

