**Example 1: 告警接收人详情**

告警接收人详情

Input: 

```
tccli wedata DescribeAlarmReceiver --cli-unfold-argument  \
    --AlarmRecipientName 用户A \
    --PageSize 1 \
    --ProjectId 123 \
    --MessageId 123 \
    --AlarmTime 2023-11-10 18:31:06 \
    --AlarmId 1 \
    --PageNumber 1 \
    --TaskType 1 \
    --AlarmRecipient 887
```

Output: 
```
{
    "Response": {
        "AlarmReceiverInfoList": [
            {
                "Http": 1,
                "Sms": 1,
                "AlarmId": "1",
                "Wechat": 1,
                "AlarmReceiver": "887",
                "Wecom": 1,
                "Voice": 1,
                "Email": 1,
                "WecomGroup": 1
            }
        ],
        "RequestId": "123",
        "TotalCount": 1
    }
}
```

