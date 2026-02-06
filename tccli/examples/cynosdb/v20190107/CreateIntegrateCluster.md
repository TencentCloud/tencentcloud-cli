**Example 1: 创建集成集群**

Create Integrate Cluster

Input: 

```
tccli cynosdb CreateIntegrateCluster --cli-unfold-argument  \
    --DbVersion 8.0 \
    --InstanceInitInfos.0.Cpu 1 \
    --InstanceInitInfos.0.DeviceType common \
    --InstanceInitInfos.0.InstanceCount 1 \
    --InstanceInitInfos.0.InstanceType rw \
    --InstanceInitInfos.0.Memory 2 \
    --IntegrateCreateClusterConfig.BackupSaveDays 7 \
    --IntegrateCreateClusterConfig.BinlogSaveDays 8 \
    --IntegrateCreateClusterConfig.SemiSyncTimeout 1000 \
    --SubnetId subnet-3du8lpau \
    --VpcId vpc-r2dqqiyv \
    --Zone ap-guangzhou-4
```

Output: 
```
{
    "Response": {
        "BigDealIds": [],
        "ClusterIds": [],
        "DealNames": [
            "20250909448021542853581"
        ],
        "RequestId": "081ec9cb-d476-4202-8943-966e1e552e3f",
        "ResourceIds": [],
        "TranId": "20250909448021542853591"
    }
}
```

