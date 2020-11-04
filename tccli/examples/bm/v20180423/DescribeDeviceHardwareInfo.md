**Example 1: 查询设备硬件配置信息**



Input: 

```
tccli bm DescribeDeviceHardwareInfo --cli-unfold-argument  \
    --InstanceIds cpm-xxx0
```

Output: 
```
{
    "Response": {
        "DeviceHardwareInfoSet": [
            {
                "InstanceId": "tcpm-xxx1",
                "DeviceClassCode": "PI100v3",
                "IsElastic": 0,
                "CpmPayMode": 2,
                "CpuId": 0,
                "Mem": 192,
                "Cpu": 40,
                "ContainRaidCard": 0,
                "SystemDiskTypeId": 0,
                "SystemDiskCount": 0,
                "DataDiskTypeId": 0,
                "DataDiskCount": 0,
                "CpuDescription": "6133(20核)*2",
                "MemDescription": "192GB",
                "DiskDescription": "480G(SSD)*1+3.6T(NVMeSSD)*4",
                "NicDescription": "10G * 2",
                "RaidDescription": "不支持"
            }
        ],
        "RequestId": "ff7a8b86-ec04-45c1-8cf9-3e6436f74263"
    }
}
```

