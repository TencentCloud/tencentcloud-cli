**Example 1: 集群弹性伸缩配置**

集群弹性伸缩配置

Input: 

```
tccli tke DescribeClusterAsGroupOption --cli-unfold-argument  \
    --ClusterId cls-hca1bmif
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
            "Expander": "random",
            "ScaleDownUnneededTime": 0
        },
        "RequestId": "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"
    }
}
```

