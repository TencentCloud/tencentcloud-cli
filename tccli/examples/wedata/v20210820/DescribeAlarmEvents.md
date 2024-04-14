**Example 1: 告警事件列表**



Input: 

```
tccli wedata DescribeAlarmEvents --cli-unfold-argument  \
    --Filters.0.Values 1 \
    --Filters.0.Name AlarmLevel \
    --PageSize 1 \
    --ProjectId 1 \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name AlarmTime \
    --PageNumber 1 \
    --StartTime 2022-12-12 12:12:12 \
    --TaskType 1 \
    --EndTime 2022-12-12 12:12:12
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AlarmEventInfoList": [
            {
                "AlarmId": "1",
                "AlarmIndicator": 0,
                "AlarmIndicatorDesc": null,
                "AlarmLevel": 0,
                "AlarmRecipientId": "1",
                "AlarmRecipientName": "name1",
                "AlarmTime": "2023-11-07 07:22:36",
                "AlarmWay": 1,
                "EstimatedTime": null,
                "InstanceId": null,
                "IsSendSuccess": 2,
                "MessageId": "0ee4bf30",
                "Operator": 1,
                "ProjectId": "1455251608631480320",
                "RegularId": "814",
                "RegularName": "mmmm",
                "SendResult": "email:1,sms:0,wecom:0,voice:0,wechat:0,http:0,wecomgroup:0",
                "TaskId": "h8591470e",
                "TaskName": "test",
                "TaskType": 201,
                "TriggerType": null
            }
        ],
        "RequestId": "1"
    }
}
```

