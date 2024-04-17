**Example 1: 修改任务告警规则**



Input: 

```
tccli wedata ModifyTaskAlarmRegular --cli-unfold-argument  \
    --Id 1769 \
    --TaskAlarmInfo.Id 1289287 \
    --TaskAlarmInfo.TaskId 3cd6b1b3-76a0-4147-8f0e-6df206bc58c0 \
    --TaskAlarmInfo.RegularId 1769 \
    --TaskAlarmInfo.RegularName 测试规则 \
    --TaskAlarmInfo.RegularStatus 1 \
    --TaskAlarmInfo.AlarmLevel 1 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.AlarmWay 1 \
    --TaskAlarmInfo.AlarmRecipientId 100028448903 \
    --TaskAlarmInfo.TaskType 201 \
    --TaskAlarmInfo.ProjectId 1486446569620893696 \
    --TaskAlarmInfo.Creater 100028448903 \
    --TaskAlarmInfo.AlarmRecipientName 100028448903 \
    --TaskAlarmInfo.AlarmIndicatorDesc 任务失败 \
    --TaskAlarmInfo.Operator 1 \
    --TaskAlarmInfo.NodeId 12846 \
    --TaskAlarmInfo.NodeName node test name \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Id  \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicator 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicatorDesc 任务失败 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.TriggerType 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.EstimatedTime 20 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Operator 1 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.AlarmIndicatorUnit ms \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Duration 0 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.DurationUnit minute \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.MaxTimes 0 \
    --TaskAlarmInfo.AlarmIndicatorInfos.0.Threshold 0 \
    --TaskAlarmInfo.AlarmRecipientType 1 \
    --TaskAlarmInfo.QuietPeriods.0.DaysOfWeek 6 7 \
    --TaskAlarmInfo.QuietPeriods.0.EndTime 06:00:00 \
    --TaskAlarmInfo.QuietPeriods.0.StartTime 00:00:01 \
    --TaskAlarmInfo.WeComHook https://www.feishu.cn/ \
    --TaskAlarmInfo.UpdateTime 2022-04-10 10:49:56 \
    --TaskAlarmInfo.OperatorUin 100028448903 \
    --TaskAlarmInfo.TaskCount 1 \
    --TaskAlarmInfo.MonitorType 2 \
    --TaskAlarmInfo.MonitorObjectIds k753e8924-a3ed-4201-b5d3-35ce683b589c \
    --TaskAlarmInfo.LatestAlarmInstanceId 3047 \
    --TaskAlarmInfo.LatestAlarmTime 2022-04-11 10:49:56 \
    --TaskAlarmInfo.Description 描述 \
    --TaskAlarmInfo.LarkWebHooks https://www.feishu.cn/ \
    --ProjectId 1486446569620893696
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "a502d7c7-d872-408e-9c2"
    }
}
```

