**Example 1: DescribeSuperNodePodList**

查询超级节点pod列表

Input: 

```
tccli tcss DescribeSuperNodePodList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PodName": "abc",
                "PodIP": "abc",
                "NodeUniqueID": "abc",
                "Status": "abc",
                "CpuRequest": 0,
                "CpuLimit": 0,
                "MemRequest": 0,
                "MemLimit": 0,
                "Namespace": "abc",
                "DeploymentName": "abc",
                "DeploymentID": "abc",
                "StartTime": "abc",
                "CreateTime": "abc",
                "RelateContainerCount": 1,
                "RunningTime": "abc",
                "PodUid": "abc",
                "ChargeCoresCnt": 1,
                "DefendStatus": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

