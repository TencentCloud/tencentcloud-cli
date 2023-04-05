**Example 1: 修改告警策略**

修改告警策略

Input: 

```
tccli cls ModifyAlarm --cli-unfold-argument  \
    --AlarmNoticeIds notice-479dec34-4a59-11eb-b378-0242ac130002 \
    --Name test \
    --TriggerCount 1 \
    --AlarmPeriod 0 \
    --MonitorTime.Type Period \
    --MonitorTime.Time 10 \
    --AlarmTargets.0.TopicId 6f574591-01b0-4475-bf0c-68255839a35d \
    --AlarmTargets.0.Number 1 \
    --AlarmTargets.0.Query * | select source \
    --AlarmTargets.0.EndTimeOffset 0 \
    --AlarmTargets.0.StartTimeOffset 0 \
    --AlarmTargets.0.LogsetId ff574591-01b0-4475-bf0c-68255839a35d \
    --Condition $1.source='10.0.0.1' \
    --AlarmId alarm-bea71170-4a59-11eb-b378-0242ac130002
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

