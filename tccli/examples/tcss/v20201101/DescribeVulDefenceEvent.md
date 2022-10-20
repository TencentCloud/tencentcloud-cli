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
        "TotalCount": 1,
        "List": [
            {
                "City": "xx",
                "CVEID": "xx",
                "ContainerName": "xx",
                "ImageID": "xx",
                "PocID": "xx",
                "EventCount": 0,
                "Status": "xx",
                "EventType": "xx",
                "HostName": "xx",
                "MergeTime": "xx",
                "SourceIP": "xx",
                "ContainerID": "xx",
                "VulName": "xx",
                "ImageName": "xx",
                "HostIP": "xx",
                "ContainerNetStatus": "xx",
                "EventID": 0,
                "ContainerStatus": "xx",
                "ContainerNetSubStatus": "xx",
                "QUUID": "xx",
                "ContainerIsolateOperationSrc": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

