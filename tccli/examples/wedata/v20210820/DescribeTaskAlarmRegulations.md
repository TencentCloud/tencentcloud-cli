**Example 1: 查询任务告警规则列表**

查询告警规则列表

Input: 

```
tccli wedata DescribeTaskAlarmRegulations --cli-unfold-argument  \
    --Filters.0.Values TaskId \
    --Filters.0.Name 123 \
    --PageSize 0 \
    --ProjectId 123 \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name ID \
    --PageNumber 0 \
    --TaskId 123 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "TaskAlarmInfos": [
            {
                "Id": "abc",
                "TaskId": "abc",
                "RegularId": "abc",
                "RegularName": "abc",
                "RegularStatus": 1,
                "AlarmLevel": 1,
                "AlarmIndicator": 1,
                "TriggerType": 1,
                "EstimatedTime": 1,
                "AlarmWay": "abc",
                "AlarmRecipientId": "abc",
                "TaskType": 1,
                "ProjectId": "abc",
                "Creater": "abc",
                "AlarmRecipientName": "abc",
                "AlarmIndicatorDesc": "abc",
                "Operator": 1,
                "NodeId": "abc",
                "NodeName": "abc",
                "AlarmIndicatorInfos": [
                    {
                        "Id": "abc",
                        "AlarmIndicator": 1,
                        "AlarmIndicatorDesc": "abc",
                        "TriggerType": 1,
                        "EstimatedTime": 1,
                        "Operator": 1,
                        "AlarmIndicatorUnit": "abc"
                    }
                ],
                "AlarmRecipientType": 1,
                "WeComHook": "abc",
                "UpdateTime": "abc",
                "OperatorUin": "abc",
                "TaskCount": 0,
                "MonitorType": 0,
                "MonitorObjectIds": [
                    "abc"
                ],
                "Description": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

