**Example 1: 告警事件列表**



Input: 

```
tccli wedata DescribeAlarmEvents --cli-unfold-argument  \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 1 \
    --ProjectId xx \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --PageNumber 1 \
    --StartTime xx \
    --TaskType 1 \
    --EndTime xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AlarmEventInfoList": [
            {
                "TaskId": "xx",
                "EstimatedTime": 1,
                "ProjectId": "xx",
                "AlarmIndicator": 1,
                "AlarmTime": "xx",
                "AlarmId": 1,
                "RegularName": "xx",
                "TriggerType": 1,
                "AlarmRecipientId": "xx",
                "AlarmWay": 1,
                "AlarmLevel": 1,
                "AlarmIndicatorDesc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

