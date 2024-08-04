**Example 1: 获取基础告警列表**



Input: 

```
tccli monitor DescribeBasicAlarmList --cli-unfold-argument  \
    --AlarmStatus 1 \
    --MetricNames mem_used \
    --Module monitor \
    --ViewNames cvm_device \
    --Limit 20 \
    --StartTime 1573660800 \
    --Offset 0 \
    --ProjectIds 0 \
    --EndTime 1573919999 \
    --OccurTimeOrder DESC
```

Output: 
```
{
    "Response": {
        "Alarms": [
            {
                "Id": 1,
                "ProjectId": 0,
                "ProjectName": "abc",
                "Status": 0,
                "AlarmStatus": "abc",
                "GroupId": 0,
                "GroupName": "abc",
                "FirstOccurTime": "abc",
                "Duration": 0,
                "LastOccurTime": "abc",
                "Content": "abc",
                "ObjName": "abc",
                "ObjId": "abc",
                "ViewName": "abc",
                "Vpc": "abc",
                "MetricId": 0,
                "MetricName": "abc",
                "AlarmType": 0,
                "Region": "abc",
                "Dimensions": "abc",
                "NotifyWay": [
                    "abc"
                ],
                "InstanceGroup": [
                    {
                        "InstanceGroupId": 0,
                        "InstanceGroupName": "abc"
                    }
                ]
            }
        ],
        "Total": 0,
        "Warning": "abc",
        "RequestId": "abc"
    }
}
```

