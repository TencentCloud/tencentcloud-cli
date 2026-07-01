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
                "ProjectName": "默认项目",
                "Status": 0,
                "AlarmStatus": "未恢复",
                "GroupId": 12345,
                "GroupName": "cpu",
                "FirstOccurTime": "2026-06-26 10:15:30",
                "Duration": 300,
                "LastOccurTime": "2026-06-26 10:20:30",
                "Content": "CPU利用率超过90%，当前值95.2%",
                "ObjName": "ins-a1b2c3d4",
                "ObjId": "ins-a1b2c3d4",
                "ViewName": "cvm_device",
                "Vpc": "vpc-12345678",
                "MetricId": 5000,
                "MetricName": "cpu_usage",
                "AlarmType": 0,
                "Region": "ap-guangzhou",
                "Dimensions": "{\"unInstanceId\":\"ins-a1b2c3d4\"}",
                "NotifyWay": [
                    "SMS",
                    "EMAIL"
                ],
                "InstanceGroup": [
                    {
                        "InstanceGroupId": 6789,
                        "InstanceGroupName": "生产环境-Web服务器组"
                    }
                ]
            }
        ],
        "Total": 1,
        "Warning": "",
        "RequestId": "3a5f7e2d-8b1c-4d6a-9e0f-1a2b3c4d5e6f"
    }
}
```

