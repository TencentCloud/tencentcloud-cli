**Example 1: GetAlarmMessage**

查询告警信息详情

Input: 

```
tccli wedata GetAlarmMessage --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --AlarmMessageId 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmLevel": 3,
            "AlarmMessageId": 20,
            "AlarmReason": "4",
            "AlarmRecipients": [
                "mytestdd"
            ],
            "AlarmRuleId": "8f258dac-19e4-45c2-ac85-1e69c8626b89",
            "AlarmTime": "2025-08-09 15:00:00",
            "AlarmWays": [
                "email",
                "sms"
            ],
            "CurRunDate": "2022-08-16 00:05:00",
            "TaskId": "20220822133437682",
            "TaskName": "alarm_cycleNotCompleted_test"
        },
        "RequestId": "2022a62a-f8ca-4cc8-8c74-b56191d2d766"
    }
}
```

