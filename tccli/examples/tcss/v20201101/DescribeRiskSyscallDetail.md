**Example 1: 运行时高危系统调用事件详细信息**

运行时高危系统调用事件详细信息

Input: 

```
tccli tcss DescribeRiskSyscallDetail --cli-unfold-argument  \
    --EventId abc
```

Output: 
```
{
    "Response": {
        "EventBaseInfo": {
            "EventId": "abc",
            "FoundTime": "2020-09-22 00:00:00",
            "ContainerId": "abc",
            "ContainerName": "abc",
            "ImageId": "abc",
            "ImageName": "abc",
            "NodeName": "abc",
            "Status": "abc",
            "EventName": "abc",
            "EventType": "abc",
            "EventCount": 0,
            "LatestFoundTime": "abc",
            "HostIP": "abc",
            "ClientIP": "abc",
            "ContainerNetStatus": "abc",
            "ContainerNetSubStatus": "abc",
            "ContainerIsolateOperationSrc": "abc",
            "NodeID": "abc",
            "NodeType": "abc",
            "NodeSubNetID": "abc",
            "NodeSubNetName": "abc",
            "NodeSubNetCIDR": "abc",
            "PodName": "abc",
            "PodIP": "abc",
            "PodStatus": "abc",
            "ClusterID": "abc"
        },
        "ProcessInfo": {
            "ProcessName": "abc",
            "ProcessAuthority": "abc",
            "ProcessId": 1,
            "ProcessStartUser": "abc",
            "ProcessUserGroup": "abc",
            "ProcessPath": "abc",
            "ProcessTree": "abc",
            "ProcessMd5": "abc",
            "ProcessParam": "abc"
        },
        "ParentProcessInfo": {
            "ProcessName": "abc",
            "ProcessId": 1,
            "ProcessStartUser": "abc",
            "ProcessUserGroup": "abc",
            "ProcessPath": "abc",
            "ProcessParam": "abc"
        },
        "EventDetail": {
            "Description": "abc",
            "Solution": "abc",
            "Remark": "abc",
            "SyscallName": "abc",
            "OperationTime": "abc"
        },
        "AncestorProcessInfo": {
            "ProcessStartUser": "abc",
            "ProcessUserGroup": "abc",
            "ProcessPath": "abc",
            "ProcessParam": "abc"
        },
        "RequestId": "abc"
    }
}
```

