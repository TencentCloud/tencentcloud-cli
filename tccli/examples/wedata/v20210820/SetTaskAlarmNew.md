**Example 1: 设置任务告警**



Input: 

```
tccli wedata SetTaskAlarmNew --cli-unfold-argument  \
    --AlarmInfoList.0.AlarmId yyyy \
    --AlarmInfoList.0.TaskIds xxx,12323 \
    --AlarmInfoList.0.Status 1 \
    --AlarmInfoList.0.AlarmType overtime \
    --AlarmInfoList.0.AlarmWay SMS,Email \
    --AlarmInfoList.0.AlarmRecipient wang;ming \
    --AlarmInfoList.0.AlarmRecipientId 1;2 \
    --AlarmInfoList.0.Hours 0 \
    --AlarmInfoList.0.Minutes 59 \
    --AlarmInfoList.0.TriggerType 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "SuccessCount": 0,
            "FailedCount": 0,
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

