**Example 1: 查询漏洞防御事件详情**



Input: 

```
tccli tcss DescribeVulDefenceEventDetail --cli-unfold-argument  \
    --EventID 0
```

Output: 
```
{
    "Response": {
        "EventDetail": {
            "City": "xx",
            "CVEID": "xx",
            "StackTrace": "xx",
            "ImageID": "xx",
            "PocID": "xx",
            "NetworkPayload": "xx",
            "ServerArg": "xx",
            "EventCount": 0,
            "Status": "xx",
            "Description": "xx",
            "EventType": "xx",
            "HostName": "xx",
            "PID": 0,
            "ServerPort": "xx",
            "ServerAccount": "xx",
            "SourceIP": "xx",
            "ContainerID": "xx",
            "VulName": "xx",
            "ServerExe": "xx",
            "RaspDetail": [
                {
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "ContainerName": "xx",
            "JNDIUrl": "xx",
            "PublicIP": "xx",
            "ImageName": "xx",
            "MainClass": "xx",
            "OfficialSolution": "xx",
            "HostIP": "xx",
            "ContainerNetStatus": "xx",
            "EventID": 0,
            "ContainerStatus": "xx",
            "ContainerNetSubStatus": "xx",
            "QUUID": "xx",
            "PodName": "xx",
            "SourcePort": [
                "xx"
            ],
            "ContainerIsolateOperationSrc": "xx"
        },
        "RequestId": "xx"
    }
}
```

