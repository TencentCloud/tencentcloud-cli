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
                "AlarmStatus": "OK",
                "AlarmType": "内存使用量",
                "Content": "内存使用量 >  66666 MB",
                "Dimensions": "{\"unInstanceId\":\"ins-19a06nn8\"}",
                "Duration": 600,
                "FirstOccurTime": "2019-11-16T15:50:00+08:00",
                "GroupId": 1278966,
                "GroupName": "dddd",
                "Id": 30057956,
                "InstanceGroup": [
                    {
                        "InstanceGroupId": 562,
                        "InstanceGroupName": "barad_nws_cvm"
                    }
                ],
                "LastOccurTime": "2019-11-16T16:00:00+08:00",
                "MetricId": 24,
                "MetricName": "mem_used",
                "NotifyWay": [
                    "EMAIL",
                    "SMS"
                ],
                "ObjId": "a961c198-e0e2-4989-a3b6-7b155b35ff6f",
                "ObjName": "10.0.0.14(251008737 vm1)",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "Region": "gz",
                "Status": 1,
                "ViewName": "cvm_device",
                "Vpc": "1"
            },
            {
                "AlarmStatus": "OK",
                "AlarmType": "内存使用量",
                "Content": "内存使用量 >=  200000 MB",
                "Dimensions": "{\"unInstanceId\":\"ins-19a06nn8\"}",
                "Duration": 180,
                "FirstOccurTime": "2019-11-16T15:45:00+08:00",
                "GroupId": 1279043,
                "GroupName": "-",
                "Id": 30057955,
                "InstanceGroup": [
                    {
                        "InstanceGroupId": 562,
                        "InstanceGroupName": "barad_nws_cvm"
                    }
                ],
                "LastOccurTime": "2019-11-16T15:48:00+08:00",
                "MetricId": 24,
                "MetricName": "mem_used",
                "NotifyWay": [
                    "EMAIL",
                    "SMS",
                    "WECHAT"
                ],
                "ObjId": "a961c198-e0e2-4989-a3b6-7b155b35ff6f",
                "ObjName": "10.0.0.14(251008737 vm1)",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "Region": "gz",
                "Status": 1,
                "ViewName": "cvm_device",
                "Vpc": "1"
            }
        ],
        "RequestId": "6b64cc24-0c60-483f-bdc3-2e55edbbc68c",
        "Total": 2,
        "Warning": "This method is deprecated! Use `DescribeAlarmHistories` instead!"
    }
}
```

