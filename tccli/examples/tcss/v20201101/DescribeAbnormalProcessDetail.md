**Example 1: 运行时异常进程事件详细信息**



Input: 

```
tccli tcss DescribeAbnormalProcessDetail --cli-unfold-argument  \
    --EventId xxx
```

Output: 
```
{
    "Response": {
        "EventDetail": {
            "Remark": "xx",
            "MatchRule": {
                "ProcessPath": "xx",
                "RuleMode": "xx",
                "RuleId": "xx"
            },
            "Description": "xx",
            "RuleId": "xx",
            "Solution": "xx",
            "RuleName": "xx"
        },
        "EventBaseInfo": {
            "EventId": "xx",
            "ContainerName": "xx",
            "ContainerId": "xx",
            "EventType": "xx",
            "FoundTime": "2020-09-22 00:00:00",
            "Status": "xx",
            "EventName": "xx",
            "ImageName": "xx",
            "PodName": "xx",
            "ImageId": "xx",
            "NodeName": "xx",
            "LatestFoundTime": "xx",
            "EventCount": 0
        },
        "ProcessInfo": {
            "ProcessPath": "xx",
            "ProcessTree": "xx",
            "ProcessId": 1,
            "ProcessAuthority": "xx",
            "ProcessUserGroup": "xx",
            "ProcessName": "xx",
            "ProcessParam": "xx",
            "ProcessMd5": "xx",
            "ProcessStartUser": "xx"
        },
        "RequestId": "xx",
        "ParentProcessInfo": {
            "ProcessPath": "xx",
            "ProcessId": 1,
            "ProcessUserGroup": "xx",
            "ProcessName": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx"
        }
    }
}
```

