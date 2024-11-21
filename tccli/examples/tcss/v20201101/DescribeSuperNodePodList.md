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
                "PodName": "web-node1",
                "PodIP": "10.0.0.11",
                "NodeUniqueID": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
                "Status": "Running",
                "CpuRequest": 0,
                "CpuLimit": 0,
                "MemRequest": 0,
                "MemLimit": 0,
                "Namespace": "defalut",
                "DeploymentName": "web-node",
                "DeploymentID": "5d95adf3-b2b2-4ebe-99ab-70cd18842344",
                "StartTime": "2024-10-30 10:35:51",
                "CreateTime": "2024-10-30 10:35:55",
                "RelateContainerCount": 1,
                "RunningTime": "2024-10-30 10:36:02",
                "PodUid": "392f05bd-bf86-4911-8cf9-b8c34541987",
                "ChargeCoresCnt": 1,
                "DefendStatus": "Defended"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5d95adf3-b2b2-4ebe-99ab-70cd24348884"
    }
}
```

