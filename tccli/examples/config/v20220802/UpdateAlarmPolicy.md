**Example 1: 更新告警设置**



Input: 

```
tccli config UpdateAlarmPolicy --cli-unfold-argument  \
    --AlarmPolicyId 123 \
    --Name u544au8b66u89c4u5219 \
    --EventScope 1 \
    --RiskLevel 1 \
    --NoticeTime 09:30:00~23:30:00 \
    --NotificationMechanism u5b9eu65f6u53d1u9001 \
    --Status 1 \
    --NoticePeriod 1 \
    --Description u5bf9u4e0du5408u89c4u89c4u5219u8fdbu884cu544au8b66
```

Output: 
```
{
    "Response": {
        "RequestId": "a7a78dce-732b-4c5e-8cd1-c11ea0e4a40e"
    }
}
```

