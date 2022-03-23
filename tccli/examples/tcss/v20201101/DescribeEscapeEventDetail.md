**Example 1: getecsapeDetail**



Input: 

```
tccli tcss DescribeEscapeEventDetail --cli-unfold-argument  \
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
            "NodeName": "xx"
        },
        "AncestorProcessInfo": {
            "ProcessPath": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx",
            "ProcessUserGroup": "xx"
        },
        "EventDetail": {
            "Description": "xx",
            "Remark": "xx",
            "Solution": "xx",
            "OperationTime": [
                "xx"
            ]
        },
        "RequestId": "xx",
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
        "ParentProcessInfo": {
            "ProcessPath": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx",
            "ProcessUserGroup": "xx"
        }
    }
}
```

