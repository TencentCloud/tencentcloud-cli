**Example 1: ListAlarmMessages**

获取告警信息列表

Input: 

```
tccli wedata ListAlarmMessages --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 20 \
    --StartTime 2025-09-08 16:00:00 \
    --EndTime 2025-09-08 17:00:00 \
    --AlarmLevel 1 \
    --AlarmRecipientId 100042232112
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 20,
            "TotalCount": 100,
            "TotalPageNumber": 5,
            "Items": [
                {
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
                }
            ]
        },
        "RequestId": "2022a62a-f8ca-4cc8-8c74-b56191d2d766"
    }
}
```

