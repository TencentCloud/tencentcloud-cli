**Example 1: 查询磁盘配置**



Input: 

```
tccli lighthouse DescribeDiskConfigs --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-2
```

Output: 
```
{
    "Response": {
        "DiskConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "DiskType": "CLOUD_PREMIUM",
                "MaxDiskSize": 1000,
                "MinDiskSize": 10,
                "DiskStepSize": 10,
                "DiskSalesState": "SOLD_OUT"
            },
            {
                "Zone": "ap-guangzhou-2",
                "DiskType": "CLOUD_SSD",
                "MaxDiskSize": 1000,
                "MinDiskSize": 20,
                "DiskStepSize": 10,
                "DiskSalesState": "SOLD_OUT"
            }
        ],
        "RequestId": "8f8e7988-39e6-4ed6-8e36-135b639e9a3a"
    }
}
```

