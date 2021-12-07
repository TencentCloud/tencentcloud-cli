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
            "RuleName": "xx"
        },
        "EventBaseInfo": {
            "EventId": "xx",
            "ContainerName": "xx",
            "ContainerId": "xx",
            "EventType": "xx",
            "FoundTime": "2020-09-22 00:00:00",
            "EventCount": 0,
            "LatestFoundTime": "2020-09-22 00:00:00",
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
        "TamperedFileInfo": {
            "FileCreateTime": "2020-09-22 00:00:00",
            "LatestTamperedFileMTime": "2020-09-22 00:00:00",
            "FileType": "xx",
            "FileName": "xx",
            "FileSize": 1,
            "FilePath": "xx"
        }
    }
}
```

