**Example 1: 查询节点池详情**



Input: 

```
tccli tke DescribeClusterNodePoolDetail --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --NodePoolId np-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "NodePool": {
            "AutoscalingGroupId": "asg-xxx",
            "AutoscalingGroupStatus": "enabled",
            "ClusterInstanceId": "cls-xxx",
            "DesiredNodesNum": 0,
            "Labels": [],
            "LaunchConfigurationId": "asc-xxx",
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
                    "Normal": 1,
                    "Total": 1
                }
            },
            "NodePoolId": "np-xxxxx",
            "Taints": []
        },
        "RequestId": "xxx"
    }
}
```

