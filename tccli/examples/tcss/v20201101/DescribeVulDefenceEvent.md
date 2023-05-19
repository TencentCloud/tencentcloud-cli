**Example 1: 查询漏洞防御事件列表**

DescribeVulDefenceEvent

Input: 

```
tccli tcss DescribeVulDefenceEvent --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
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
                "EventID": 0,
                "CreateTime": "abc",
                "ContainerNetStatus": "abc",
                "MergeTime": "abc",
                "ContainerStatus": "abc",
                "ContainerNetSubStatus": "abc",
                "ContainerIsolateOperationSrc": "abc",
                "QUUID": "abc",
                "HostIP": "abc",
                "HostName": "abc",
                "ClusterID": "abc",
                "NodeType": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

