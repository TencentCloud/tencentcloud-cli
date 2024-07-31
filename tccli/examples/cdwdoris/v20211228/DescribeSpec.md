**Example 1: 获取集群规格**

购买页拉取集群的数据节点和zookeeper节点的规格列表

Input: 

```
tccli cdwdoris DescribeSpec --cli-unfold-argument  \
    --Zone ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "RequestId": "10058bc0-40e7-4eb0-9b4d",
        "MasterSpec": [
            {
                "Name": "SCH3",
                "Cpu": 2,
                "Mem": 4,
                "Type": "STANDARD",
                "DataDisk": {
                    "DiskCount": 1,
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskType": "CLOUD_HSSD",
                    "DiskDesc": "增强型SSD云硬盘"
                },
                "SystemDisk": {
                    "DiskCount": 1,
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                },
                "MaxNodeSize": 50,
                "Available": true,
                "ComputeSpecDesc": "2核4G"
            }
        ],
        "CoreSpec": [
            {
                "Name": "SCH6",
                "Cpu": 4,
                "Mem": 16,
                "Type": "STANDARD",
                "DataDisk": {
                    "DiskCount": 1,
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskType": "CLOUD_HSSD",
                    "DiskDesc": "增强型SSD云硬盘"
                },
                "SystemDisk": {
                    "DiskCount": 1,
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                },
                "MaxNodeSize": 50,
                "Available": true,
                "ComputeSpecDesc": "4核16G"
            }
        ],
        "AttachCBSSpec": [
            {
                "DiskCount": 1,
                "MaxDiskSize": 32000,
                "MinDiskSize": 100,
                "DiskType": "CLOUD_HSSD",
                "DiskDesc": "增强型SSD云硬盘"
            }
        ]
    }
}
```

