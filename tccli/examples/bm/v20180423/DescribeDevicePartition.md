**Example 1: 获取物理机的分区格式**



Input: 

```
tccli bm DescribeDevicePartition --cli-unfold-argument  \
    --InstanceId cpm-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "DevicePartition": {
            "SystemDiskSize": 275,
            "DataDiskSize": 44703,
            "SysIsUefiType": true,
            "SysRootSpace": 20,
            "SysSwaporuefiSpace": 2,
            "SysUsrlocalSpace": 0,
            "SysDataSpace": 253,
            "DeviceDiskSizeInfoSet": [
                {
                    "DiskName": "sda",
                    "DiskSize": 275
                },
                {
                    "DiskName": "sdb",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdc",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdd",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sde",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdf",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdg",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdh",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdi",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdj",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdk",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdl",
                    "DiskSize": 3725
                },
                {
                    "DiskName": "sdm",
                    "DiskSize": 3725
                }
            ]
        },
        "RequestId": "bf746562-bedf-435f-ad6a-ddaa2b043ecd"
    }
}
```

