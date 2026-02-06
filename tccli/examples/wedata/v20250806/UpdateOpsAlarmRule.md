**Example 1: UpdateOpsAlarmRule**



Input: 

```
tccli wedata UpdateOpsAlarmRule --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --AlarmRuleId 01b38b0a-6102-4b96-ac61-cfabb7f22552 \
    --AlarmRuleName dddd22xxss \
    --MonitorObjectType 2 \
    --MonitorObjectIds 832b83ea-d285-43bd-b4bb-5a268aa8cb50 \
    --AlarmTypes failure \
    --AlarmRuleDetail.Trigger 2 \
    --AlarmRuleDetail.DataBackfillOrRerunTrigger 1 \
    --AlarmRuleDetail.TimeOutExtInfo.0.RuleType 1 \
    --AlarmRuleDetail.TimeOutExtInfo.0.Type 1 \
    --AlarmRuleDetail.DataBackfillOrRerunTimeOutExtInfo.0.RuleType 1 \
    --AlarmRuleDetail.DataBackfillOrRerunTimeOutExtInfo.0.Type 1 \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.AlarmType projectSuccessInstanceDownwardFluctuationAlarm \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.InstanceThresholdCountPercent 1 \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.InstanceThresholdCount 2 \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.StabilizeThreshold 3 \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.StabilizeStatisticsCycle 4 \
    --AlarmRuleDetail.ProjectInstanceStatisticsAlarmInfoList.0.IsCumulant True \
    --AlarmRuleDetail.ReconciliationExtInfo.0.RuleType reconciliationMismatch \
    --AlarmRuleDetail.ReconciliationExtInfo.0.MismatchCount 100 \
    --AlarmRuleDetail.ReconciliationExtInfo.0.Hour 100 \
    --AlarmRuleDetail.ReconciliationExtInfo.0.Min 1 \
    --Status 1 \
    --AlarmLevel 3 \
    --AlarmGroups.0.AlarmEscalationInterval 0 \
    --AlarmGroups.0.NotificationFatigue.NotifyCount 1 \
    --AlarmGroups.0.NotificationFatigue.NotifyInterval 5 \
    --AlarmGroups.0.NotificationFatigue.QuietIntervals.0.DaysOfWeek 1 \
    --AlarmGroups.0.NotificationFatigue.QuietIntervals.0.StartTime 12:00:00 \
    --AlarmGroups.0.NotificationFatigue.QuietIntervals.0.EndTime 15:00:00 \
    --AlarmGroups.0.AlarmWays 1 \
    --AlarmGroups.0.WebHooks.0.AlarmWay 7 \
    --AlarmGroups.0.WebHooks.0.WebHooks xxb \
    --AlarmGroups.0.AlarmRecipientType 3 \
    --AlarmGroups.0.AlarmRecipientIds 158 \
    --Description this is your description
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "a821688d-110f-49ae-8d79-818cbc2ec0cd"
    }
}
```

