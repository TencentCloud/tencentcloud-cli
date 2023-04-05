**Example 1: 创建告警策略**

创建告警策略

Input: 

```
tccli cls CreateAlarm --cli-unfold-argument  \
    --AlarmNoticeIds notice-b02af159-f67b-44c3-877c-a55343f874c3 \
    --Name test \
    --TriggerCount 1 \
    --AlarmPeriod 0 \
    --MonitorTime.Type Period \
    --MonitorTime.Time 10 \
    --AlarmTargets.0.TopicId be3d88bb-a9cb-4d29-b697-0fcfbfd601ef \
    --AlarmTargets.0.Number 1 \
    --AlarmTargets.0.Query * | select count(*) as count \
    --AlarmTargets.0.EndTimeOffset 0 \
    --AlarmTargets.0.StartTimeOffset 0 \
    --AlarmTargets.0.LogsetId fe3d45bb-a9cb-4d29-b697-0fcfbfd601ef \
    --Condition $1.count > 10
```

Output: 
```
{
    "Response": {
        "AlarmId": "alarm-479dec34-4a59-11eb-b378-0242ac130002",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

