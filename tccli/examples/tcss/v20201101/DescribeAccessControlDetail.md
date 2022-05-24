**Example 1: 运行时访问控制事件详细信息**



Input: 

```
tccli tcss DescribeAccessControlDetail --cli-unfold-argument  \
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
            "ContainerIsolateOperationSrc": "xx",
            "ContainerNetSubStatus": "xx",
            "ContainerNetStatus": "xx"
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
            "Remark": "xx",
            "MatchRule": {
                "ProcessPath": "xx",
                "RuleMode": "xx",
                "TargetFilePath": "xx",
                "RuleId": "xx"
            },
            "Description": "xx",
            "RuleId": "xx",
            "Solution": "xx",
            "RuleName": "xx",
            "OperationTime": "xx"
        },
        "AncestorProcessInfo": {
            "ProcessPath": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx",
            "ProcessUserGroup": "xx"
        },
        "TamperedFileInfo": {
            "FilePath": "xx",
            "FileType": "xx",
            "FileName": "xx",
            "FileSize": 1,
            "LatestTamperedFileMTime": "2020-09-22 00:00:00",
            "FileCreateTime": "2020-09-22 00:00:00"
        },
        "ParentProcessInfo": {
            "ProcessPath": "xx",
            "ProcessParam": "xx",
            "ProcessStartUser": "xx",
            "ProcessUserGroup": "xx"
        },
        "RequestId": "xx"
    }
}
```

