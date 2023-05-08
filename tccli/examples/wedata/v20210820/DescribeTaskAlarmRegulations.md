**Example 1: 查询任务告警规则列表**



Input: 

```
tccli wedata DescribeTaskAlarmRegulations --cli-unfold-argument  \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 0 \
    --ProjectId 0 \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --PageNumber 0 \
    --TaskId 1 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "TaskAlarmInfos": [
            {
                "TaskId": "xx",
                "EstimatedTime": 1,
                "ProjectId": "xx",
                "TaskType": 1,
                "AlarmIndicator": 1,
                "Id": "xx",
                "Creater": "xx",
                "RegularId": "xx",
                "RegularName": "xx",
                "TriggerType": 1,
                "AlarmWay": 1,
                "AlarmLevel": 1,
                "RegularStatus": 1
            }
        ]
    }
}
```

