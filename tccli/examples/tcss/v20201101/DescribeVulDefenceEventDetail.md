**Example 1: 查询漏洞防御事件详情**

查询漏洞防御事件详情

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
            "CVEID": "abc",
            "VulName": "abc",
            "PocID": "abc",
            "EventType": "abc",
            "SourceIP": "abc",
            "City": "abc",
            "EventCount": 0,
            "ContainerID": "abc",
            "ContainerName": "abc",
            "ImageID": "abc",
            "ImageName": "abc",
            "Status": "abc",
            "SourcePort": [
                "abc"
            ],
            "EventID": 0,
            "HostName": "abc",
            "HostIP": "abc",
            "PublicIP": "abc",
            "PodName": "abc",
            "Description": "abc",
            "OfficialSolution": "abc",
            "NetworkPayload": "abc",
            "PID": 0,
            "MainClass": "abc",
            "StackTrace": "abc",
            "ServerAccount": "abc",
            "ServerPort": "abc",
            "ServerExe": "abc",
            "ServerArg": "abc",
            "QUUID": "abc",
            "ContainerNetStatus": "abc",
            "ContainerNetSubStatus": "abc",
            "ContainerIsolateOperationSrc": "abc",
            "ContainerStatus": "abc",
            "JNDIUrl": "abc",
            "RaspDetail": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "NodeSubNetName": "abc",
            "NodeSubNetCIDR": "abc",
            "PodIP": "abc",
            "NodeType": "abc",
            "NodeID": "abc",
            "NodeUniqueID": "abc",
            "NodeSubNetID": "abc",
            "ClusterID": "abc",
            "ClusterName": "abc",
            "Namespace": "abc",
            "WorkloadType": "abc"
        },
        "RequestId": "abc"
    }
}
```

