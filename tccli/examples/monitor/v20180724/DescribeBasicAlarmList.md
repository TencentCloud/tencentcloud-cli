**Example 1: Getting the basic alarm list**



Input: 

```
tccli monitor DescribeBasicAlarmList --cli-unfold-argument  \
    --Module monitor\
    --StartTime 1573660800\
    --EndTime 1573919999\
    --Limit 20\
    --Offset 0\
    --OccurTimeOrder DESC\
    --ProjectIds 0\
    --ViewNames cvm_device\
    --AlarmStatus '1
"MetricName": "mem_used",'
```

Output: 
```
{
    "Response": {
        "Alarms": [
            {
                "AlarmStatus": "OK",
                "AlarmType": "Used memory",
                "Content": "Used memory >  66666 MB",
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
                "ProjectName": "Default project",
                "Region": "gz",
                "Status": 1,
                "ViewName": "cvm_device",
                "Vpc": "1"
            },
            {
                "AlarmStatus": "OK",
                "AlarmType": "Used memory",
                "Content": "Used memory >=  200000 MB",
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
                "ProjectName": "Default project",
                "Region": "gz",
                "Status": 1,
                "ViewName": "cvm_device",
                "Vpc": "1"
            }
        ],
        "RequestId": "6b64cc24-0c60-483f-bdc3-2e55edbbc68c",
        "Total": 2
    }
}
```

