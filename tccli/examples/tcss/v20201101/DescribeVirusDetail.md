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
        "Mark": "xx",
        "ProcessChan": "xx",
        "ProcessAccountGroup": "xx",
        "ProcessId": 1,
        "Tags": [
            "xx"
        ],
        "HostName": "xx",
        "ImageId": "xx",
        "HarmDescribe": "xx",
        "SuggestScheme": "xx",
        "ProcessName": "xx",
        "ProcessArgv": "xx",
        "ProcessMd5": "xx",
        "ProcessFileAuthority": "xx",
        "ModifyTime": "xx",
        "SourceType": 1,
        "ProcessPath": "xx",
        "HostId": "xx",
        "ContainerId": "xx",
        "FilePath": "xx",
        "ImageName": "xx",
        "PodName": "xx",
        "CreateTime": "xx",
        "Size": 1,
        "FileName": "xx",
        "FileMd5": "xx",
        "EventType": "xx",
        "Status": "xx",
        "SubStatus": "xx",
        "RequestId": "xx"
    }
}
```

