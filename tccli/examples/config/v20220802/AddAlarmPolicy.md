**Example 1: 创建告警**



Input: 

```
tccli config AddAlarmPolicy --cli-unfold-argument  \
    --Name 告警规则1 \
    --Type 1 \
    --EventScope 1 \
    --RiskLevel 1 \
    --NoticeTime 09:30:00~23:30:00 \
    --NotificationMechanism 实时发送 \
    --Status 1 \
    --NoticePeriod 1
```

Output: 
```
{
    "Response": {
        "AlarmPolicyId": 2,
        "RequestId": "e2c458f6-dedc-46eb-955a-6d2c3555c597"
    }
}
```

