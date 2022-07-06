**Example 1: 运行时高危系统调用接口**



Input: 

```
tccli tcss DescribeRiskSyscallEvents --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "ContainerName": "xx",
                "LatestFoundTime": "xx",
                "Status": "xx",
                "Description": "xx",
                "ImageId": "xx",
                "EventId": "xx",
                "Remark": "xx",
                "NodeName": "xx",
                "EventCount": 0,
                "Solution": "xx",
                "SyscallName": "xx",
                "ImageName": "xx",
                "ContainerNetStatus": "xx",
                "ProcessPath": "xx",
                "ContainerStatus": "xx",
                "ContainerId": "xx",
                "ProcessName": "xx",
                "ContainerNetSubStatus": "xx",
                "FoundTime": "xx",
                "RuleExist": true,
                "PodName": "xx",
                "ContainerIsolateOperationSrc": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

