**Example 1: 创建集群**

创建一个管控节点和两个计算节点的集群。调度器为：SLURM。

Input: 

```
tccli thpc CreateCluster --cli-unfold-argument  \
    --ManagerNodeCount 1 \
    --Placement.Zone ap-guangzhou-2 \
    --SchedulerType SLURM \
    --ImageId img-3la7wgnt \
    --ComputeNode.InstanceChargeType SPOTPAID \
    --ComputeNode.InstanceType S2.SMALL2 \
    --ComputeNodeCount 2 \
    --ManagerNode.InstanceType S2.SMALL2
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

