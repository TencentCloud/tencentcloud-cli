**Example 1: 集群弹性伸缩配置**

集群弹性伸缩配置

Input: 

```
tccli tke DescribeClusterAsGroupOption --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterAsGroupOption": {
            "ScaleDownUnreadyTime": 0,
            "ScaleDownDelay": 0,
            "ScaleDownUtilizationThreshold": 0,
            "MaxTotalUnreadyPercentage": 0,
            "IsScaleDownEnabled": true,
            "OkTotalUnreadyCount": 0,
            "SkipNodesWithSystemPods": true,
            "MaxEmptyBulkDelete": 0,
            "UnregisteredNodeRemovalTime": 0,
            "SkipNodesWithLocalStorage": true,
            "IgnoreDaemonSetsUtilization": true,
            "Expander": "xxx",
            "ScaleDownUnneededTime": 0
        },
        "RequestId": "xxx"
    }
}
```

