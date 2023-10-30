**Example 1: DescribeEscapeEventInfo**

查询容器逃逸事件列表

Input: 

```
tccli tcss DescribeEscapeEventInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "EventType": "abc",
                "ContainerName": "abc",
                "ImageName": "abc",
                "Status": "abc",
                "EventId": "abc",
                "NodeName": "abc",
                "PodName": "abc",
                "FoundTime": "2020-09-22 00:00:00",
                "EventName": "abc",
                "ImageId": "abc",
                "ContainerId": "abc",
                "Solution": "abc",
                "Description": "abc",
                "EventCount": 0,
                "LatestFoundTime": "2020-09-22 00:00:00",
                "NodeIP": "abc",
                "HostID": "abc",
                "ContainerNetStatus": "abc",
                "ContainerNetSubStatus": "abc",
                "ContainerIsolateOperationSrc": "abc",
                "ContainerStatus": "abc",
                "ClusterID": "abc",
                "NodeType": "abc",
                "PodIP": "abc",
                "NodeUniqueID": "abc",
                "PublicIP": "abc",
                "NodeID": "abc",
                "HostIP": "abc",
                "ClusterName": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

