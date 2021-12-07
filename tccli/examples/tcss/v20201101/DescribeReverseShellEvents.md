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
                "ContainerId": "xx",
                "PProcessName": "xx",
                "ProcessPath": "xx",
                "Solution": "xx",
                "FoundTime": "2020-09-22T00:00:00+00:00",
                "ImageId": "xx",
                "ProcessName": "xx",
                "ImageName": "xx",
                "EventId": "xx",
                "EventCount": 0,
                "LatestFoundTime": "2020-09-22T00:00:00+00:00",
                "Description": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

