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
        "ImageId": "abc",
        "ImageName": "abc",
        "CreateTime": "abc",
        "Size": 1,
        "FilePath": "abc",
        "ModifyTime": "abc",
        "VirusName": "abc",
        "RiskLevel": "abc",
        "ContainerName": "abc",
        "ContainerId": "abc",
        "HostName": "abc",
        "HostId": "abc",
        "ProcessName": "abc",
        "ProcessPath": "abc",
        "ProcessMd5": "abc",
        "ProcessId": 1,
        "ProcessArgv": "abc",
        "ProcessChan": "abc",
        "ProcessAccountGroup": "abc",
        "ProcessStartAccount": "abc",
        "ProcessFileAuthority": "abc",
        "SourceType": 0,
        "Tags": [
            "abc"
        ],
        "HarmDescribe": "abc",
        "SuggestScheme": "abc",
        "Mark": "abc",
        "FileName": "abc",
        "FileMd5": "abc",
        "EventType": "abc",
        "PodName": "abc",
        "Status": "abc",
        "SubStatus": "abc",
        "HostIP": "abc",
        "ClientIP": "abc",
        "PProcessStartUser": "abc",
        "PProcessUserGroup": "abc",
        "PProcessPath": "abc",
        "PProcessParam": "abc",
        "AncestorProcessStartUser": "abc",
        "AncestorProcessUserGroup": "abc",
        "AncestorProcessPath": "abc",
        "AncestorProcessParam": "abc",
        "OperationTime": "abc",
        "ContainerNetStatus": "abc",
        "ContainerNetSubStatus": "abc",
        "ContainerIsolateOperationSrc": "abc",
        "CheckPlatform": [
            "abc"
        ],
        "FileAccessTime": "abc",
        "FileModifyTime": "abc",
        "NodeSubNetID": "abc",
        "NodeSubNetName": "abc",
        "NodeSubNetCIDR": "abc",
        "ClusterID": "abc",
        "PodIP": "abc",
        "PodStatus": "abc",
        "NodeUniqueID": "abc",
        "NodeType": "abc",
        "NodeID": "abc",
        "ClusterName": "abc",
        "RequestId": "abc"
    }
}
```

