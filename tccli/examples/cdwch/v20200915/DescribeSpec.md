**Example 1: 获取集群规格**

购买页拉取集群的数据节点和zookeeper节点的规格列表

Input: 

```
tccli cdwch DescribeSpec --cli-unfold-argument  \
    --Zone ap-guangzhou-1
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
                    "DiskDesc": "xx",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskCount": 1,
                    "DiskType": "xx"
                },
                "DisplayName": "xx",
                "Name": "xx",
                "ComputeSpecDesc": "xx",
                "Mem": 16,
                "MaxNodeSize": 50,
                "Type": "xx",
                "Cpu": 4,
                "DataDisk": {
                    "DiskDesc": "xx",
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskCount": 1,
                    "DiskType": "xx"
                }
            }
        ],
        "AttachCBSSpec": [
            {
                "DiskDesc": "xx",
                "MaxDiskSize": 32000,
                "MinDiskSize": 100,
                "DiskCount": 1,
                "DiskType": "xx"
            }
        ],
        "CommonSpec": [
            {
                "Available": true,
                "InstanceQuota": 1000,
                "SystemDisk": {
                    "DiskDesc": "xx",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskCount": 1,
                    "DiskType": "xx"
                },
                "DisplayName": "xx",
                "Name": "xx",
                "ComputeSpecDesc": "xx",
                "Mem": 4,
                "MaxNodeSize": 50,
                "Type": "xx",
                "Cpu": 2,
                "DataDisk": {
                    "DiskDesc": "xx",
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskCount": 1,
                    "DiskType": "xx"
                }
            }
        ],
        "RequestId": "xx"
    }
}
```

