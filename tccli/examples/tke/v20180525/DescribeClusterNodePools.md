**Example 1: 查询节点池列表**



Input: 

```
tccli tke DescribeClusterNodePools --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "NodePoolSet": [
            {
                "AutoscalingGroupId": "",
                "AutoscalingGroupStatus": "",
                "ClusterInstanceId": "cls-69hshd30",
                "DataDisks": null,
                "DeletionProtection": false,
                "DesiredNodesNum": 1,
                "DesiredPodNum": 0,
                "DockerGraphPath": "",
                "ExtraArgs": {
                    "Kubelet": null
                },
                "GPUArgs": null,
                "ImageId": "",
                "Labels": [],
                "LaunchConfigurationId": "",
                "LifeState": "normal",
                "MaxNodesNum": 1,
                "MinNodesNum": 0,
                "Name": "test",
                "NodeCountSummary": {
                    "AutoscalingAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 0,
                        "Total": 0
                    },
                    "ManuallyAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 0,
                        "Total": 1
                    }
                },
                "NodePoolId": "np-5tx2l4de",
                "NodePoolOs": "",
                "OsCustomizeType": "",
                "Tags": null,
                "Taints": [],
                "Unschedulable": 0,
                "UserScript": ""
            }
        ],
        "RequestId": "efb810cb-d5a2-4147-88ec-cd1e28c5202e",
        "TotalCount": 1
    }
}
```

