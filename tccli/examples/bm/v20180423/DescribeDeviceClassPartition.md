**Example 1: 查询机型RAID方式以及系统盘大小**



Input: 

```
tccli bm DescribeDeviceClassPartition --cli-unfold-argument  \
    --DeviceClassCode PS001v1
```

Output: 
```
{
    "Response": {
        "DeviceClassPartitionInfoSet": [
            {
                "RaidId": 2,
                "Raid": "RAID5",
                "RaidDisplay": "RAID5",
                "SystemDiskSize": 1392,
                "SysRootSpace": 20,
                "SysSwaporuefiSpace": 2,
                "SysUsrlocalSpace": 0,
                "SysDataSpace": 1370,
                "SysIsUefiType": 0,
                "DataDiskSize": 0,
                "DeviceDiskSizeInfoSet": [
                    {
                        "DiskName": "sda",
                        "DiskSize": 1392
                    }
                ]
            }
        ],
        "RequestId": "a62dbf3f-45d8-45c4-a659-22b1c844f4d9"
    }
}
```

**Example 2: 查询机型RAID方式以及系统盘大小（自定义机型）**



Input: 

```
tccli bm DescribeDeviceClassPartition --cli-unfold-argument  \
    --DeviceClassCode 任意值 \
    --InstanceId tcpm-xxx
```

Output: 
```
{
    "Response": {
        "DeviceClassPartitionInfoSet": [
            {
                "RaidId": 1,
                "Raid": "RAID0",
                "RaidDisplay": "RAID0",
                "SystemDiskSize": 554,
                "SysRootSpace": 20,
                "SysSwaporuefiSpace": 2,
                "SysUsrlocalSpace": 0,
                "SysDataSpace": 532,
                "SysIsUefiType": 1,
                "DataDiskSize": 0,
                "DeviceDiskSizeInfoSet": [
                    {
                        "DiskName": "sda",
                        "DiskSize": 554
                    }
                ]
            },
            {
                "RaidId": 8,
                "Raid": "RAID1",
                "RaidDisplay": "RAID 1",
                "SystemDiskSize": 275,
                "SysRootSpace": 20,
                "SysSwaporuefiSpace": 2,
                "SysUsrlocalSpace": 0,
                "SysDataSpace": 253,
                "SysIsUefiType": 1,
                "DataDiskSize": 0,
                "DeviceDiskSizeInfoSet": [
                    {
                        "DiskName": "sda",
                        "DiskSize": 275
                    }
                ]
            }
        ],
        "RequestId": "3e4b965e-b543-411a-8f9b-bf20479de1f1"
    }
}
```

