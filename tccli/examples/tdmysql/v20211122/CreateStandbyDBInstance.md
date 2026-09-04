**Example 1: 创建灾备**



Input: 

```
tccli tdmysql CreateStandbyDBInstance --cli-unfold-argument  \
    --PrimaryInstanceId tdsql3-c5eab757 \
    --Zone ap-chengdu-1 \
    --VpcId vpc-jksnni36 \
    --SubnetId subnet-dz7wfk4r \
    --SpecCode 1c2g \
    --Disk 20 \
    --StorageNodeNum 3 \
    --Replications 3 \
    --FullReplications 3 \
    --StorageNodeCpu 1 \
    --StorageNodeMem 2 \
    --PayMode 0 \
    --Zones ap-chengdu-1 \
    --InstanceType hybrid \
    --StorageType CLOUD_HSSD \
    --PrimaryInstanceRegion ap-chengdu \
    --InstanceMode enhanced
```

Output: 
```
{
    "Response": {
        "FlowId": 4295043361,
        "InstanceId": "tdsql3-6e462513",
        "RequestId": "329c5c1e-b337-4733-a46b-543c3ed59435"
    }
}
```

