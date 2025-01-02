**Example 1: 修改集群弹性伸缩属性**



Input: 

```
tccli tke ModifyClusterAsGroupOptionAttribute --cli-unfold-argument  \
    --ClusterId cls-2wds9k9p \
    --ClusterAsGroupOption.IsScaleDownEnabled true \
    --ClusterAsGroupOption.UnregisteredNodeRemovalTime 10 \
    --ClusterAsGroupOption.OkTotalUnreadyCount 3 \
    --ClusterAsGroupOption.ScaleDownUnreadyTime 10 \
    --ClusterAsGroupOption.MaxTotalUnreadyPercentage 20
```

Output: 
```
{
    "Response": {
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

