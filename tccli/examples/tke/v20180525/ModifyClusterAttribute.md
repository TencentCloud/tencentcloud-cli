**Example 1: 修改集群属性**



Input: 

```
tccli tke ModifyClusterAttribute --cli-unfold-argument  \
    --AutoUpgradeClusterLevel.IsAutoUpgrade True \
    --ClusterName xx \
    --ProjectId 0 \
    --ClusterDesc xx \
    --ClusterId xx \
    --ClusterLevel xx
```

Output: 
```
{
    "Response": {
        "AutoUpgradeClusterLevel": {
            "IsAutoUpgrade": true
        },
        "ClusterName": "xx",
        "ProjectId": 0,
        "ClusterDesc": "xx",
        "RequestId": "xx",
        "ClusterLevel": "xx"
    }
}
```

