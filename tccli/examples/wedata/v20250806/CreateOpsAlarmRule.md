**Example 1: CreateAlarmRule**



Input: 

```
tccli wedata CreateOpsAlarmRule --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --AlarmRuleName ruleName222 \
    --MonitorObjectIds 832b83ea-d285-43bd-b4bb-5a268aa8cb50 \
    --AlarmTypes failure \
    --AlarmGroups.0.AlarmWays 1 \
    --AlarmGroups.0.AlarmRecipientType 2 \
    --MonitorObjectType 2 \
    --AlarmRuleDetail.TimeOutExtInfo.0.RuleType 1 \
    --AlarmRuleDetail.TimeOutExtInfo.0.Type 1 \
    --AlarmRuleDetail.TimeOutExtInfo.0.Min 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmRuleId": "d736b8ba-b6d9-4a21-824a-84bdda3d9731"
        },
        "RequestId": "71ff56d1-7400-48f9-9c79-c749281c01c0"
    }
}
```

