**Example 1: 加强型实例创建克隆**



Input: 

```
tccli tdmysql CreateCloneInstance --cli-unfold-argument  \
    --Zone ap-chengdu-1 \
    --VpcId vpc-jksnni36 \
    --SubnetId subnet-dz7wfk4r \
    --SpecCode 1c2g \
    --Disk 20 \
    --StorageNodeNum 3 \
    --InstanceId tdsql3-2a6b33ef \
    --BackupName /tdsql3_ap_chengdu/251231015/tdsql3-2a6b33ef/automatic/physical/full-backup/2026-04-22/1776859363/tdstore-data \
    --StorageNodeCpu 1 \
    --StorageNodeMem 2 \
    --CreateVersion 21.2.5 \
    --InstanceType hybrid \
    --StorageType CLOUD_HSSD \
    --Zones ap-chengdu-1 \
    --InstanceMode enhanced
```

Output: 
```
{
    "Response": {
        "FlowId": 4295036956,
        "InstanceId": "tdsql3-ba6b4cbc",
        "RequestId": "f23a4c9f-39d1-489f-839f-bab199c2d37e"
    }
}
```

