**Example 1: BatchCreateIntegrationTaskAlarms**



Input: 

```
tccli wedata BatchCreateIntegrationTaskAlarms --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskIds 20220506145218687 20220413105240052 \
    --TaskAlarmInfo.AlarmRecipientName v_vxbbzhang \
    --TaskAlarmInfo.TaskId 20220506171453813 \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.ProjectId 11022568003970304 \
    --TaskAlarmInfo.TaskType 201 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.Id 1 \
    --TaskAlarmInfo.Creater tom \
    --TaskAlarmInfo.RegularId 371 \
    --TaskAlarmInfo.RegularName 测试超时告警 \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.AlarmRecipientId 100022187073 \
    --TaskAlarmInfo.AlarmWay 1 \
    --TaskAlarmInfo.AlarmLevel 1 \
    --TaskAlarmInfo.RegularStatus 1
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

