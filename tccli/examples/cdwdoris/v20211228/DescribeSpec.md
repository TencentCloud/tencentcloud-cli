**Example 1: 获取集群规格**

购买页拉取集群节点规格列表

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

**Example 2: 获取特定机型规格**

获取特定机型规格

Input: 

```
tccli cdwdoris DescribeSpec --cli-unfold-argument  \
    --Zone ap-chongqing-1 \
    --SpecName S_4_16_H
```

Output: 
```
{
    "Response": {
        "AttachCBSSpec": [
            {
                "DiskCount": 1,
                "DiskDesc": "增强型SSD云硬盘",
                "DiskType": "CLOUD_HSSD",
                "MaxDiskSize": 32000,
                "MinDiskSize": 1000
            },
            {
                "DiskCount": 1,
                "DiskDesc": "SSD云硬盘",
                "DiskType": "CLOUD_SSD",
                "MaxDiskSize": 32000,
                "MinDiskSize": 1000
            },
            {
                "DiskCount": 1,
                "DiskDesc": "高性能云硬盘",
                "DiskType": "CLOUD_PREMIUM",
                "MaxDiskSize": 32000,
                "MinDiskSize": 1000
            }
        ],
        "CNSpec": [
            {
                "Available": true,
                "ComputeSpecDesc": "4核16G",
                "Cpu": 4,
                "DataDisk": {
                    "DiskCount": 10,
                    "DiskDesc": "增强型SSD云硬盘",
                    "DiskType": "CLOUD_HSSD",
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200
                },
                "InstanceQuota": 583,
                "MaxNodeSize": 50,
                "Mem": 16,
                "Name": "S_4_16_H",
                "SystemDisk": {
                    "DiskCount": 1,
                    "DiskDesc": "高性能云硬盘",
                    "DiskType": "CLOUD_PREMIUM",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50
                },
                "Type": "STANDARD"
            }
        ],
        "CoreSpec": [
            {
                "Available": true,
                "ComputeSpecDesc": "4核16G",
                "Cpu": 4,
                "DataDisk": {
                    "DiskCount": 10,
                    "DiskDesc": "增强型SSD云硬盘",
                    "DiskType": "CLOUD_HSSD",
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200
                },
                "InstanceQuota": 583,
                "MaxNodeSize": 50,
                "Mem": 16,
                "Name": "S_4_16_H",
                "SystemDisk": {
                    "DiskCount": 1,
                    "DiskDesc": "高性能云硬盘",
                    "DiskType": "CLOUD_PREMIUM",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50
                },
                "Type": "STANDARD"
            }
        ],
        "MasterSpec": [
            {
                "Available": true,
                "ComputeSpecDesc": "4核16G",
                "Cpu": 4,
                "DataDisk": {
                    "DiskCount": 10,
                    "DiskDesc": "增强型SSD云硬盘",
                    "DiskType": "CLOUD_HSSD",
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200
                },
                "InstanceQuota": 583,
                "MaxNodeSize": 50,
                "Mem": 16,
                "Name": "S_4_16_H",
                "SystemDisk": {
                    "DiskCount": 1,
                    "DiskDesc": "高性能云硬盘",
                    "DiskType": "CLOUD_PREMIUM",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50
                },
                "Type": "STANDARD"
            }
        ],
        "RequestId": "d654c06b-173e-49d7-b368-c74aad9472f0"
    }
}
```

