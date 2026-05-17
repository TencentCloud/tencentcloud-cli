**Example 1: 修改或者更改处置状态**



Input: 

```
tccli csip ModifyAlarmRiskStatus --cli-unfold-argument  \
    --AlarmRiskIdSet.0.AlarmRiskId 1001 \
    --AlarmRiskIdSet.0.AppId 123456789 \
    --AlarmRiskIdSet.1.AlarmRiskId 1002 \
    --AlarmRiskIdSet.1.AppId 123456789 \
    --AlarmRiskIdSet.2.AlarmRiskId 1003 \
    --AlarmRiskIdSet.2.AppId 123456789 \
    --HandleStatus 1 \
    --AlarmRiskType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

