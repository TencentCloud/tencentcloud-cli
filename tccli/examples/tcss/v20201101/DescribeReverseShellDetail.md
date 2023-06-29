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
        "EventBaseInfo": {
            "EventId": "xx",
            "ContainerName": "xx",
            "ContainerId": "xx",
            "EventCount": 0,
            "EventType": "xx",
            "HostIP": "xx",
            "FoundTime": "2020-09-22 00:00:00",
            "Status": "xx",
            "EventName": "xx",
            "ImageId": "xx",
            "ImageName": "xx",
            "PodName": "xx",
            "ClientIP": "xx",
            "LatestFoundTime": "xx",
            "NodeName": "xx",
            "ContainerNetStatus": "xx",
            "ContainerNetSubStatus": "xx",
            "ContainerIsolateOperationSrc": "xx"
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
        "EventDetail": {
            "DstAddress": "xx",
            "Remark": "xx",
            "Description": "xx",
            "Solution": "xx",
            "OperationTime": "xx"
        },
        "AncestorProcessInfo": {
            "ProcessPath": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx",
            "ProcessUserGroup": "xx"
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

