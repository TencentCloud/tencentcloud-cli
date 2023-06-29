**Example 1: 创建集群**



Input: 

```
tccli thpc CreateCluster --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --SchedulerType SLURM \
    --ImageId img-3la7wgnt \
    --ManagerNode.InstanceType S2.SMALL2 \
    --ManagerNodeCount 1 \
    --ComputeNode.InstanceType S2.SMALL2 \
    --ComputeNode.InstanceChargeType SPOTPAID \
    --ComputeNodeCount 2
```

Output: 
```
{
    "Response": {
        "ClusterId": "hpc-5lyv94lq",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

