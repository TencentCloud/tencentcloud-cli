**Example 1: 查询恶意请求事件列表**

查询恶意请求事件列表

Input: 

```
tccli tcss DescribeRiskDnsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EventID": 1,
                "EventType": "abc",
                "Address": "abc",
                "ContainerID": "abc",
                "ContainerName": "abc",
                "ContainerNetStatus": "abc",
                "ContainerStatus": "abc",
                "ContainerNetSubStatus": "abc",
                "ContainerIsolateOperationSrc": "abc",
                "ImageID": "abc",
                "ImageName": "abc",
                "FoundTime": "abc",
                "LatestFoundTime": "abc",
                "EventStatus": "abc",
                "EventCount": 0,
                "Description": "abc",
                "Solution": "abc",
                "City": "abc",
                "HostName": "abc",
                "HostID": "abc",
                "HostIP": "abc",
                "PublicIP": "abc",
                "NodeType": "SUPER",
                "NodeName": "abc",
                "ClusterID": "abc",
                "PodIP": "abc",
                "PodName": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

