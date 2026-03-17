**Example 1: 修改调度器参数信息**



Input: 

```
tccli tke ModifyClusterSchedulerPolicy --cli-unfold-argument  \
    --ClusterId cls-ncmx45jw \
    --HighPerformance True \
    --PoolSchedulerStartArg.PoolingShardingCount 10 \
    --PoolSchedulerStartArg.VirtualNodeCount 150 \
    --PoolSchedulerStartArg.PoolingKeyLabels "aaa_ccc"
```

Output: 
```
{
    "Response": {
        "RequestId": "96fbca81-f0fe-46d6-ad81-ab87f6ae24f6"
    }
}
```

