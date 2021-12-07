**Example 1: 运行时反弹shell事件详细信息**



Input: 

```
tccli tcss DescribeReverseShellDetail --cli-unfold-argument  \
    --EventId xxx
```

Output: 
```
{
    "Response": {
        "EventDetail": {
            "DstAddress": "xx",
            "Remark": "xx",
            "Description": "xx",
            "Solution": "xx"
        },
        "EventBaseInfo": {
            "EventId": "xx",
            "ContainerName": "xx",
            "ContainerId": "xx",
            "EventType": "xx",
            "FoundTime": "2020-09-22 00:00:00",
            "LatestFoundTime": "2020-09-22 00:00:00",
            "EventCount": 0,
            "Status": "xx",
            "EventName": "xx",
            "ImageName": "xx",
            "PodName": "xx",
            "ImageId": "xx",
            "NodeName": "xx"
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

