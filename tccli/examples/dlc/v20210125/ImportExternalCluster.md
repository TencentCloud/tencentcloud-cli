**Example 1: ImportExternalCluster**



Input: 

```
tccli dlc ImportExternalCluster --cli-unfold-argument  \
    --PartitionName PartitionTest \
    --ClusterType TKE \
    --ClusterId cls-m6fgdp2o \
    --CosBucketId aidanyxu-260209337 \
    --PrometheusInstanceId prom-8r1jdbdk \
    --LoadBalancerId lb-1vuex1zi \
    --NodeLabels.0.Key testK \
    --NodeLabels.0.Value testV \
    --PartitionDescription PartitionDescriptionTest \
    --TargetAppId 120779018 \
    --TargetUin 1808365191
```

Output: 
```
{
    "Response": {
        "ResourcePoolCode": "dlc-3dc08527",
        "ResourcePoolId": 48,
        "WorkflowId": 1558,
        "RequestId": "89736fa1-7b00-43b3-8b72-f5b4def4d861"
    }
}
```

