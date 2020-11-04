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
                "AutoscalingGroupId": "asg-xxxxx",
                "AutoscalingGroupStatus": "enabled",
                "ClusterInstanceId": "cls-xxxxx",
                "DesiredNodesNum": 1,
                "Labels": [],
                "LaunchConfigurationId": "asc-xxxxx",
                "LifeState": "normal",
                "MaxNodesNum": 1,
                "MinNodesNum": 0,
                "Name": "test2",
                "NodeCountSummary": {
                    "AutoscalingAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 1,
                        "Total": 1
                    },
                    "ManuallyAdded": {
                        "Initializing": 0,
                        "Joining": 0,
                        "Normal": 0,
                        "Total": 0
                    }
                },
                "NodePoolId": "np-xxxx",
                "Taints": []
            }
        ],
        "RequestId": "xxxxxx",
        "TotalCount": 1
    }
}
```

