**Example 1: 查询任务告警规则列表**

查询告警规则列表

Input: 

```
tccli wedata DescribeTaskAlarmRegulations --cli-unfold-argument  \
    --Filters.0.Values TaskId \
    --Filters.0.Name j224b9321-3be0-45de-ad6a-8fed924036a4 \
    --PageSize 10 \
    --ProjectId 123 \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name CreateTime \
    --PageNumber 1 \
    --TaskId j224b9321-3be0-45de-ad6a-8fed924036a4 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "TaskAlarmInfos": [
            {
                "Id": "",
                "TaskId": "j224b9321-3be0-45de-ad6a-8fed924036a4",
                "RegularId": "1768",
                "RegularName": "规则名称",
                "RegularStatus": 1,
                "AlarmLevel": 1,
                "AlarmIndicator": 1,
                "TriggerType": 1,
                "EstimatedTime": 1,
                "AlarmWay": "7",
                "AlarmRecipientId": "100035441697",
                "TaskType": 201,
                "ProjectId": "1486446569620893696",
                "Creater": "100035441697",
                "AlarmRecipientName": "username",
                "AlarmIndicatorDesc": "",
                "Operator": 1,
                "NodeId": "",
                "NodeName": "",
                "AlarmIndicatorInfos": [
                    {
                        "Id": "",
                        "AlarmIndicator": 12,
                        "AlarmIndicatorDesc": "每10分钟内累计重启次数",
                        "TriggerType": 5,
                        "EstimatedTime": 1,
                        "Operator": 1,
                        "AlarmIndicatorUnit": "ms",
                        "Duration": 0,
                        "DurationUnit": "ms",
                        "MaxTimes": 1,
                        "Threshold": 0
                    }
                ],
                "AlarmRecipientType": 0,
                "QuietPeriods": [
                    {
                        "DaysOfWeek": [
                            6,
                            7
                        ],
                        "EndTime": "06:00:00",
                        "StartTime": "00:00:00"
                    }
                ],
                "WeComHook": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=50d83e54-97e3-41234567890",
                "UpdateTime": "2024-02-27 14:45:12",
                "OperatorUin": "100035441697",
                "TaskCount": 0,
                "MonitorType": 0,
                "MonitorObjectIds": [
                    "k753e8924-a3ed-4201-b5d3-35ce683b589c"
                ],
                "Description": "",
                "LatestAlarmInstanceId": "",
                "LatestAlarmTime": "",
                "LarkWebHooks": ""
            }
        ],
        "TotalCount": 10,
        "RequestId": "ec06dfed-ce42-4a5c-b23c-14a3a2227b39"
    }
}
```

