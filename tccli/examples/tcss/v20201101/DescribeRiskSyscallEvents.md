**Example 1: 运行时高危系统调用接口**

运行时高危系统调用接口

Input: 

```
tccli tcss DescribeRiskSyscallEvents --cli-unfold-argument ```

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
                "SyscallName": "abc",
                "Status": "abc",
                "EventId": "abc",
                "NodeName": "abc",
                "PodName": "abc",
                "Remark": "abc",
                "RuleExist": true,
                "EventCount": 0,
                "LatestFoundTime": "abc",
                "ContainerNetStatus": "abc",
                "ContainerNetSubStatus": "abc",
                "ContainerIsolateOperationSrc": "abc",
                "ContainerStatus": "abc",
                "NodeType": "abc",
                "ClusterID": "abc",
                "PodIP": "abc",
                "NodeUniqueID": "abc",
                "PublicIP": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

