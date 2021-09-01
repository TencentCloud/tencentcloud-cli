**Example 1: 查询设备型号**



Input: 

```
tccli bm DescribeDeviceClass --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DeviceClassSet": [
            {
                "DeviceClassCode": "PS100v3",
                "CpuDescription": "6133(20核)*2",
                "MemDescription": "256GB",
                "DiskDescription": "480G(SSD)*6",
                "HaveRaidCard": 1,
                "NicDescription": "10G * 2",
                "GpuDescription": "",
                "DeviceType": "standard",
                "Series": 3,
                "Cpu": 40,
                "Mem": 256,
                "Discount": 50,
                "UnitPrice": 1100000,
                "RealPrice": 550000,
                "NormalPrice": 1100000
            },
            {
                "DeviceClassCode": "PS100v1",
                "CpuDescription": "E5-2670v3(12核)*2",
                "MemDescription": "128GB",
                "DiskDescription": "300G(SAS)*12",
                "HaveRaidCard": 1,
                "NicDescription": "10G * 2",
                "GpuDescription": "",
                "DeviceType": "standard",
                "Series": 1,
                "Cpu": 24,
                "Mem": 128,
                "Discount": 50,
                "UnitPrice": 590000,
                "RealPrice": 295000,
                "NormalPrice": 590000
            },
            {
                "DeviceClassCode": "PS001v1",
                "CpuDescription": "E5-2620v3(6核)*2",
                "MemDescription": "64GB",
                "DiskDescription": "6*300G(SAS)",
                "HaveRaidCard": 1,
                "NicDescription": "1G * 2",
                "GpuDescription": "",
                "DeviceType": "standard",
                "Series": 1,
                "Cpu": 12,
                "Mem": 64,
                "Discount": 50,
                "UnitPrice": 337000,
                "RealPrice": 168500,
                "NormalPrice": 337000
            }
        ],
        "RequestId": "9b01c2d9-ceda-4d90-8e38-c5246bbf3190"
    }
}
```

