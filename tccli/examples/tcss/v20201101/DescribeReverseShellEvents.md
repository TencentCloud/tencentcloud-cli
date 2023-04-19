**Example 1: 运行时反弹shell列表**

运行时反弹shell列表

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
        "TotalCount": 1,
        "EventSet": [
            {
                "ProcessName": "abc",
                "ProcessPath": "abc",
                "ImageId": "abc",
                "ContainerId": "abc",
                "ImageName": "abc",
                "ContainerName": "abc",
                "FoundTime": "abc",
                "Solution": "abc",
                "Description": "abc",
                "Status": "abc",
                "EventId": "abc",
                "Remark": "abc",
                "PProcessName": "abc",
                "EventCount": 0,
                "LatestFoundTime": "abc",
                "DstAddress": "abc",
                "ContainerNetStatus": "abc",
                "ContainerNetSubStatus": "abc",
                "ContainerIsolateOperationSrc": "abc",
                "ContainerStatus": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

