**Example 1: 创建告警策略**

创建告警策略

Input: 

```
tccli cls CreateAlarm --cli-unfold-argument  \
    --Name test-p0 告警策略 \
    --AlarmTargets.0.Query level:error | select count(*) as cnt limit 100 \
    --AlarmTargets.0.Number 1 \
    --AlarmTargets.0.StartTimeOffset -15 \
    --AlarmTargets.0.EndTimeOffset 0 \
    --AlarmTargets.0.SyntaxRule 1 \
    --AlarmTargets.0.LogsetId ad5a574c-xxxx-xxxx-bb67-990d0cb9747a \
    --AlarmTargets.0.TopicId test-cos-1254111111 \
    --MonitorTime.Type Period \
    --MonitorTime.Time 1 \
    --TriggerCount 1 \
    --AlarmPeriod 15 \
    --AlarmNoticeIds notice-1a2c6c17-xxxx-xxxx-81be-25248ada5a4c \
    --Status True \
    --MessageTemplate {{.Label}} \
    --CallBack.Body  \
    --Analysis.0.Name 自定义检索分析 \
    --Analysis.0.Type query \
    --Analysis.0.Content level:error | select err limit 100 \
    --Analysis.0.ConfigInfo.0.Key SyntaxRule \
    --Analysis.0.ConfigInfo.0.Value 1 \
    --GroupTriggerStatus False \
    --MonitorObjectType 0 \
    --MultiConditions.0.Condition [$1.__QUERYCOUNT__]> 10000 \
    --MultiConditions.0.AlarmLevel 0
```

Output: 
```
{
    "Response": {
        "AlarmId": "alarm-37cd7e19-xxxx-xxxx-82cc-00713ef449f6",
        "RequestId": "ab6b1233-xxxx-xxxx-91f5-c6fad91966fe"
    }
}
```

