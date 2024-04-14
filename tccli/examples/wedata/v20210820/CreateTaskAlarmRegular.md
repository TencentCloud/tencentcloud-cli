**Example 1: 创建集成任务告警规则**



Input: 

```
tccli wedata CreateTaskAlarmRegular --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --TaskAlarmInfo.AlarmRecipientName hive2mysql \
    --TaskAlarmInfo.TaskId 20220506145218687 \
    --TaskAlarmInfo.EstimatedTime 1 \
    --TaskAlarmInfo.ProjectId 11022568003970304 \
    --TaskAlarmInfo.TaskType 201 \
    --TaskAlarmInfo.AlarmIndicator 1 \
    --TaskAlarmInfo.Id 11022568003970304 \
    --TaskAlarmInfo.Creater tom \
    --TaskAlarmInfo.RegularId 1 \
    --TaskAlarmInfo.RegularName 测试验证_17 \
    --TaskAlarmInfo.TriggerType 1 \
    --TaskAlarmInfo.AlarmRecipientId 100022187073,100024263714 \
    --TaskAlarmInfo.AlarmWay 2,1,3,5,6 \
    --TaskAlarmInfo.AlarmLevel 1 \
    --TaskAlarmInfo.RegularStatus 1
```

Output: 
```
{
    "Response": {
        "RequestId": "as1cs2c123asyi23bh213cc",
        "AlarmId": 312
    }
}
```

