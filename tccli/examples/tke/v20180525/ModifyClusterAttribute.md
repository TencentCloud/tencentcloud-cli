**Example 1: 修改集群属性**

修改集群属性

Input: 

```
tccli tke ModifyClusterAttribute --cli-unfold-argument  \
    --AutoUpgradeClusterLevel.IsAutoUpgrade True \
    --ClusterName tke \
    --ProjectId 0 \
    --ClusterDesc tke \
    --ClusterId cls-7ph3twqe \
    --ClusterLevel L5 \
    --ClusterProperty.NodeNameType lan-ip
```

Output: 
```
{
    "Response": {
        "AutoUpgradeClusterLevel": {
            "IsAutoUpgrade": true
        },
        "ClusterName": "tke",
        "ProjectId": 0,
        "ClusterDesc": "tke",
        "QGPUShareEnable": true,
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886",
        "ClusterLevel": "L5",
        "ClusterProperty": {
            "NodeNameType": "lan-ip"
        }
    }
}
```

