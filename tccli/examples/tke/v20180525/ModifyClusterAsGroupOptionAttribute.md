**Example 1: 修改集群弹性伸缩属性**



Input: 

```
tccli tke ModifyClusterAsGroupOptionAttribute --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --ClusterAsGroupOption.IsScaleDownEnabled true \
    --ClusterAsGroupOption.UnregisteredNodeRemovalTime x \
    --ClusterAsGroupOption.OkTotalUnreadyCount x \
    --ClusterAsGroupOption.ScaleDownUnreadyTime x \
    --ClusterAsGroupOption.MaxTotalUnreadyPercentage x
```

Output: 
```
{
    "Response": {
        "RequestId": "82f2fe9c-c5fa-4077-9236-f1341180a696"
    }
}
```

