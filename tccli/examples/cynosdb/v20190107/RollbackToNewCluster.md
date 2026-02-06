**Example 1: 回档到新集群**

Rollback To New Cluster

Input: 

```
tccli cynosdb RollbackToNewCluster --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --ClusterName  \
    --ProjectId 0 \
    --PayMode 0 \
    --OriginalClusterId cynosdbmysql-0fs2nhc7 \
    --FromSaveBackup False \
    --RollbackId 64142 \
    --InstanceInitInfos.0.Cpu 1 \
    --InstanceInitInfos.0.Memory 1 \
    --InstanceInitInfos.0.DeviceType common \
    --InstanceInitInfos.0.InstanceType rw \
    --InstanceInitInfos.0.InstanceCount 1 \
    --UniqVpcId vpc-ns1jr6ff \
    --UniqSubnetId subnet-gncsqeuq
```

Output: 
```
{
    "Response": {
        "BigDealIds": [],
        "ClusterIds": [],
        "DealNames": [
            "20250928456021591536011"
        ],
        "RequestId": "0c646e65-3597-44d7-b68b-d43391eedb33",
        "ResourceIds": [],
        "TranId": "20250928456021591536021"
    }
}
```

