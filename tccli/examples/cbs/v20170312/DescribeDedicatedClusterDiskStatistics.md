**Example 1: 查询CVM CDC集群云硬盘容量信息统计**

查询CVM CDC集群云硬盘容量信息统计

Input: 

```
tccli cbs DescribeDedicatedClusterDiskStatistics --cli-unfold-argument  \
    --DedicatedClusterId cluster-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "DedicatedClusterDiskStatisticSet": [
            {
                "AvailableDiskSize": 100,
                "DiskType": "CLOUD_SSD",
                "TotalDiskSize": 100,
                "UsedDiskSize": 100
            }
        ],
        "RequestId": "bbe8a3ff-8874-4196-b152-dbc8d912b3dd"
    }
}
```

