**Example 1: 设置任务告警**

设置任务告警

Input: 

```
tccli wedata SetTaskAlarmNew --cli-unfold-argument  \
    --AlarmInfoList.0.TaskIds 20240307211852581 \
    --AlarmInfoList.0.AlarmType failure \
    --AlarmInfoList.0.AlarmWay email \
    --AlarmInfoList.0.AlarmRecipient micofywang \
    --AlarmInfoList.0.AlarmRecipientId 100033435965 \
    --AlarmInfoList.0.Hours 0 \
    --AlarmInfoList.0.Minutes 1 \
    --AlarmInfoList.0.TriggerType 1 \
    --AlarmInfoList.0.Status 1 \
    --ProjectId 1492511691706699776
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailedCount": 0,
            "SuccessCount": 1,
            "TotalCount": 1
        },
        "RequestId": "ddabe7a0-9747-4a52-ad37-f820a7c020ee"
    }
}
```

