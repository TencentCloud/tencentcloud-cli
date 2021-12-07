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
        "EventDetail": {
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
        "RequestId": "xx"
    }
}
```

