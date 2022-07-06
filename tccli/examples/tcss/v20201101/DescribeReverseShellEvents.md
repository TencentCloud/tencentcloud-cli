**Example 1: 运行时反弹shell列表**



Input: 

```
tccli tcss DescribeReverseShellEvents --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "Status": "xx",
                "ContainerName": "xx",
                "Remark": "xx",
                "ContainerIsolateOperationSrc": "xx",
                "ContainerStatus": "xx",
                "ContainerId": "xx",
                "PProcessName": "xx",
                "ProcessPath": "xx",
                "ContainerNetSubStatus": "xx",
                "Solution": "xx",
                "FoundTime": "xx",
                "ImageId": "xx",
                "ProcessName": "xx",
                "ImageName": "xx",
                "EventId": "xx",
                "EventCount": 0,
                "DstAddress": "xx",
                "LatestFoundTime": "xx",
                "ContainerNetStatus": "xx",
                "Description": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

