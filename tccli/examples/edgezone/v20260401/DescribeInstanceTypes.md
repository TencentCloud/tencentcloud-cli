**Example 1: 查询指定可用区的账号机型配额**

查询指定可用区下当前账号可用的机型配额列表。

Input: 

```
tccli edgezone DescribeInstanceTypes --cli-unfold-argument  \
    --Zone ap-guangzhou-1
```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Zone": "ap-guangzhou-1",
                "InstanceType": "BMS5.MEDIUM8",
                "InstanceFamily": "BM.S5",
                "CpuCores": 8,
                "CpuType": "6231C*2",
                "MemoryGb": 32,
                "SystemDiskType": "SSD",
                "SystemDiskSize": 480,
                "SystemDiskCount": 2,
                "DataDiskType": "SSD",
                "DataDiskSize": 960,
                "DataDiskCount": 4,
                "DiskType": "SSD-480G*2, SSD-960G*4",
                "NetworkInterfaceType": "25G*2",
                "GpuType": "",
                "Quota": 10
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 查询账号全部可用区机型配额**

不传 Zone 时，返回当前账号下所有可用区的机型配额列表。

Input: 

```
tccli edgezone DescribeInstanceTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Zone": "ap-guangzhou-1",
                "InstanceType": "BMS5.MEDIUM8",
                "InstanceFamily": "BM.S5",
                "CpuCores": 8,
                "CpuType": "6231C*2",
                "MemoryGb": 32,
                "SystemDiskType": "SSD",
                "SystemDiskSize": 480,
                "SystemDiskCount": 2,
                "DataDiskType": "SSD",
                "DataDiskSize": 960,
                "DataDiskCount": 4,
                "DiskType": "SSD-480G*2, SSD-960G*4",
                "NetworkInterfaceType": "25G*2",
                "GpuType": "",
                "Quota": 10
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceType": "BMS5.LARGE16",
                "InstanceFamily": "BM.S5",
                "CpuCores": 16,
                "CpuType": "6231C*2",
                "MemoryGb": 64,
                "SystemDiskType": "SSD",
                "SystemDiskSize": 480,
                "SystemDiskCount": 2,
                "DataDiskType": "SSD",
                "DataDiskSize": 1920,
                "DataDiskCount": 4,
                "DiskType": "SSD-480G*2, SSD-1920G*4",
                "NetworkInterfaceType": "25G*2",
                "GpuType": "",
                "Quota": 0
            }
        ],
        "TotalCount": 2,
        "RequestId": "b5d7f3a2-c418-4b9e-9c72-4a1e6d3f8b90"
    }
}
```

