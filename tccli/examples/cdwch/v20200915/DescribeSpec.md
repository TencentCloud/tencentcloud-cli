**Example 1: 获取集群规格**

购买页拉取集群的数据节点和zookeeper节点的规格列表

Input: 

```
tccli cdwch DescribeSpec --cli-unfold-argument  \
    --Zone 'ap-guangzhou-1
 

{
  "Zone": "abc",
"PayMode":"xxxx",

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
                    "DiskDesc": "abc",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskCount": 1,
                    "DiskType": "abc"
                },
                "DisplayName": "abc",
                "Name": "abc",
                "ComputeSpecDesc": "abc",
                "Mem": 16,
                "MaxNodeSize": 50,
                "Type": "abc",
                "Cpu": 4,
                "DataDisk": {
                    "DiskDesc": "abc",
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskCount": 1,
                    "DiskType": "abc"
                }
            }
        ],
        "AttachCBSSpec": [
            {
                "DiskDesc": "abc",
                "MaxDiskSize": 32000,
                "MinDiskSize": 100,
                "DiskCount": 1,
                "DiskType": "abc"
            }
        ],
        "CommonSpec": [
            {
                "Available": true,
                "InstanceQuota": 1000,
                "SystemDisk": {
                    "DiskDesc": "abc",
                    "MaxDiskSize": 50,
                    "MinDiskSize": 50,
                    "DiskCount": 1,
                    "DiskType": "abc"
                },
                "DisplayName": "abc",
                "Name": "abc",
                "ComputeSpecDesc": "abc",
                "Mem": 4,
                "MaxNodeSize": 50,
                "Type": "abc",
                "Cpu": 2,
                "DataDisk": {
                    "DiskDesc": "abc",
                    "MaxDiskSize": 32000,
                    "MinDiskSize": 100,
                    "DiskCount": 1,
                    "DiskType": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

