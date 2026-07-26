**Example 1: 创建实例**



Input: 

```
tccli tdmysql CreateDBInstances --cli-unfold-argument  \
    --Zone ap-chengdu-1 \
    --VpcId vpc-jksnni36 \
    --SubnetId subnet-dz7wfk4r \
    --SpecCode 1c2g \
    --Disk 30 \
    --StorageNodeNum 3 \
    --Replications 3 \
    --InstanceCount 1 \
    --CreateVersion 21.2.0 \
    --InitParams.0.Param character_set_server \
    --InitParams.0.Value utf8mb4 \
    --StorageNodeCpu 1 \
    --StorageNodeMem 2 \
    --Zones ap-chengdu-1 \
    --InstanceType hybrid \
    --StorageType CLOUD_HSSD \
    --InstanceMode enhanced \
    --SQLMode MySQL \
    --Password T********3
```

Output: 
```
{
    "Response": {
        "FlowId": 4295045790,
        "InstanceIds": [
            "tdsql3-a473bad5"
        ],
        "RequestId": "04bea82b-7915-4359-b050-6d31b7ca2613"
    }
}
```

