**Example 1: 创建实例**



Input: 

```
tccli tdmysql CreateDBInstances --cli-unfold-argument  \
    --Zone ap-chengdu-2 \
    --VpcId vpc-jksnni36 \
    --SubnetId subnet-dz7wfk4r \
    --SpecCode 1c2g \
    --Disk 30 \
    --StorageNodeNum 3 \
    --Replications 3 \
    --InstanceCount 1 \
    --CreateVersion 21.2.3 \
    --InitParams.0.Param character_set_server \
    --InitParams.0.Value utf8mb4 \
    --StorageNodeCpu 1 \
    --StorageNodeMem 2 \
    --Zones ap-chengdu-2 \
    --InstanceType hybrid \
    --StorageType CLOUD_HSSD \
    --InstanceMode enhanced \
    --SQLMode MySQL
```

Output: 
```
{
    "Response": {
        "FlowId": 4294998382,
        "InstanceIds": [
            "tdsql3-ac67c142"
        ],
        "RequestId": "b3e61005-1e6d-48a2-b5af-de6c4f19dd01"
    }
}
```

