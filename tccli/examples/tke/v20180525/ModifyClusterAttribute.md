**Example 1: 修改集群属性**



Input: 

```
tccli tke ModifyClusterAttribute --cli-unfold-argument  \
    --AutoUpgradeClusterLevel.IsAutoUpgrade True \
    --ClusterName tke-test \
    --ProjectId 0 \
    --ClusterDesc 测试 \
    --ClusterId cls-7ph3twqe \
    --ClusterLevel L5
```

Output: 
```
{
    "Response": {
        "AutoUpgradeClusterLevel": {
            "IsAutoUpgrade": true
        },
        "ClusterName": "tke-test",
        "ProjectId": 0,
        "ClusterDesc": "测试",
        "QGPUShareEnable": true,
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886",
        "ClusterLevel": "L5"
    }
}
```

