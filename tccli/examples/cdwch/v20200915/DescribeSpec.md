**Example 1: 获取集群规格**

购买页拉取集群的数据节点和zookeeper节点的规格列表

Input: 

```
tccli cdwch DescribeSpec --cli-unfold-argument  \
    --Zone 'ap-guangzhou-1
 

{
  "Zone": "abc",
"PayMode":"postpay",

}'
```

Output: 
```
{
    "Response": {
        "DataSpec": [
            {
                "Available": true,
                "InstanceQuota": 1000,
                "SystemDisk": {
                    "DiskCount": 10,
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                },
                "DisplayName": "4核16G",
                "Name": "4核16G",
                "ComputeSpecDesc": "4核16G",
                "Mem": 16,
                "MaxNodeSize": 50,
                "Type": "4核16G",
                "Cpu": 4,
                "DataDisk": {
                    "DiskCount": 10,
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                }
            }
        ],
        "AttachCBSSpec": [
            {
                "DiskCount": 1,
                "MaxDiskSize": 32000,
                "MinDiskSize": 1000,
                "DiskType": "CLOUD_HSSD",
                "DiskDesc": "增强型SSD云硬盘"
            }
        ],
        "CommonSpec": [
            {
                "Available": true,
                "InstanceQuota": 1000,
                "SystemDisk": {
                    "DiskCount": 10,
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                },
                "DisplayName": "4核16G",
                "Name": "4核16G",
                "ComputeSpecDesc": "4核16G",
                "Mem": 4,
                "MaxNodeSize": 50,
                "Type": "4核16G",
                "Cpu": 2,
                "DataDisk": {
                    "DiskCount": 10,
                    "MaxDiskSize": 320000,
                    "MinDiskSize": 200,
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskDesc": "高性能云硬盘"
                }
            }
        ],
        "RequestId": "e378c73e-a52a-4897-9155-ba2aa797006d"
    }
}
```

