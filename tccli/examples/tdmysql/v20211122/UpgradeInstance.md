**Example 1: 加强型实例纵向变配**



Input: 

```
tccli tdmysql UpgradeInstance --cli-unfold-argument  \
    --InstanceId tdsql3-bcedf765 \
    --SpecCode 1c2g \
    --Disk 20 \
    --StorageNodeCpu 1 \
    --StorageNodeMem 2 \
    --StorageType CLOUD_TCS
```

Output: 
```
{
    "Response": {
        "FlowId": 4295036957,
        "RequestId": "c2341b01-296a-4fd3-9f5c-009c0f232d09"
    }
}
```

