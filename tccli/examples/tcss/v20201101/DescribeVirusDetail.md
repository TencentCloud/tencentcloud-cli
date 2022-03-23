**Example 1: 运行时查询木马文件信息**

运行时查询木马文件信息

Input: 

```
tccli tcss DescribeVirusDetail --cli-unfold-argument  \
    --Id dskaldjskld
```

Output: 
```
{
    "Response": {
        "ContainerName": "xx",
        "ProcessStartAccount": "xx",
        "RiskLevel": "xx",
        "VirusName": "xx",
        "FileMd5": "xx",
        "ProcessChan": "xx",
        "ProcessAccountGroup": "xx",
        "Status": "xx",
        "ProcessId": 1,
        "Tags": [
            "xx"
        ],
        "EventType": "xx",
        "HostName": "xx",
        "HostIP": "xx",
        "SubStatus": "xx",
        "ImageId": "xx",
        "PProcessParam": "xx",
        "ClientIP": "xx",
        "AncestorProcessStartUser": "xx",
        "HarmDescribe": "xx",
        "SuggestScheme": "xx",
        "AncestorProcessParam": "xx",
        "ProcessName": "xx",
        "ProcessArgv": "xx",
        "ProcessMd5": "xx",
        "ProcessFileAuthority": "xx",
        "RequestId": "xx",
        "PProcessPath": "xx",
        "ModifyTime": "xx",
        "Mark": "xx",
        "SourceType": 1,
        "ProcessPath": "xx",
        "HostId": "xx",
        "ContainerId": "xx",
        "FilePath": "xx",
        "AncestorProcessUserGroup": "xx",
        "OperationTime": "xx",
        "AncestorProcessPath": "xx",
        "PProcessStartUser": "xx",
        "FileName": "xx",
        "ImageName": "xx",
        "PProcessUserGroup": "xx",
        "PodName": "xx",
        "CreateTime": "xx",
        "Size": 1
    }
}
```

