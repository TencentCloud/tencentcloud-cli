**Example 1: 告警接收人详情**

告警接收人详情

Input: 

```
tccli wedata DescribeAlarmReceiver --cli-unfold-argument  \
    --AlarmRecipientName xx \
    --PageSize 1 \
    --ProjectId xx \
    --MessageId xx \
    --AlarmTime xx \
    --AlarmId xx \
    --PageNumber 1 \
    --TaskType 1 \
    --AlarmRecipient xx
```

Output: 
```
{
    "Response": {
        "AlarmReceiverInfoList": [
            {
                "Http": 1,
                "Sms": 1,
                "AlarmId": 1,
                "Wechat": 1,
                "AlarmReceiver": "xx",
                "Wecom": 1,
                "Voice": 1,
                "Email": 1
            }
        ],
        "RequestId": "xx",
        "TotalCount": 1
    }
}
```

