**Example 1: 查询自定义机型部件信息**



Input: 

```
tccli bm DescribeHardwareSpecification --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CpuInfoSet": [
            {
                "CpuId": 1,
                "CpuDescription": "E5-2620v3 (6核)  * 2",
                "Series": 1,
                "ContainRaidCard": [
                    0,
                    1
                ]
            },
            {
                "CpuId": 3,
                "CpuDescription": "E5-2670v3 (12核)  * 2",
                "Series": 1,
                "ContainRaidCard": [
                    1
                ]
            },
            {
                "CpuId": 4,
                "CpuDescription": "E5-2620v4 (8核)  * 2",
                "Series": 2,
                "ContainRaidCard": [
                    0,
                    1
                ]
            },
            {
                "CpuId": 2,
                "CpuDescription": "E5-2680v4 (14核)  * 2",
                "Series": 2,
                "ContainRaidCard": [
                    0,
                    1
                ]
            },
            {
                "CpuId": 5,
                "CpuDescription": "4110（8核）* 2",
                "Series": 3,
                "ContainRaidCard": [
                    0,
                    1
                ]
            },
            {
                "CpuId": 6,
                "CpuDescription": "6133 （20核）* 2",
                "Series": 3,
                "ContainRaidCard": [
                    0,
                    1
                ]
            }
        ],
        "MemSet": [
            64,
            128,
            192,
            256,
            384,
            512
        ],
        "DiskInfoSet": [
            {
                "DiskTypeId": 1,
                "Size": 300,
                "DiskDescription": "SAS-HDD-300G"
            },
            {
                "DiskTypeId": 2,
                "Size": 600,
                "DiskDescription": "SAS-HDD-600G"
            },
            {
                "DiskTypeId": 3,
                "Size": 1200,
                "DiskDescription": "SAS-HDD-1.2T"
            },
            {
                "DiskTypeId": 4,
                "Size": 2000,
                "DiskDescription": "SATA-HDD-2T"
            },
            {
                "DiskTypeId": 5,
                "Size": 4000,
                "DiskDescription": "SATA-HDD-4T"
            },
            {
                "DiskTypeId": 6,
                "Size": 8000,
                "DiskDescription": "SATA-HDD-8T"
            },
            {
                "DiskTypeId": 7,
                "Size": 240,
                "DiskDescription": "SATA-SSD-240G"
            },
            {
                "DiskTypeId": 8,
                "Size": 480,
                "DiskDescription": "SATA-SSD-480G"
            },
            {
                "DiskTypeId": 9,
                "Size": 800,
                "DiskDescription": "SATA-SSD-800G"
            },
            {
                "DiskTypeId": 10,
                "Size": 2000,
                "DiskDescription": "NVME-SSD-2T"
            },
            {
                "DiskTypeId": 11,
                "Size": 3200,
                "DiskDescription": "NVME-SSD-3.2T"
            },
            {
                "DiskTypeId": 12,
                "Size": 960,
                "DiskDescription": "SATA-SSD-960G"
            }
        ],
        "RequestId": "a2c2794e-fef1-4545-95f4-ec7c7fe773ae"
    }
}
```

