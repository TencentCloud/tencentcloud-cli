**Example 1: Querying the purchasable specifications of a TencentDB instance**



Input: 

```
tccli cdb DescribeDBZoneConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 17,
        "Items": [
            {
                "RegionName": "Guangzhou",
                "Area": "South China",
                "IsDefaultRegion": 0,
                "Region": "ap-guangzhou",
                "ZonesConf": [
                    {
                        "Status": 1,
                        "ZoneName": "Guangzhou Zone 2",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 30,
                        "IsDefaultZone": false,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1",
                            "2"
                        ],
                        "DrZone": [
                            "ap-shanghai-1",
                            "ap-shanghai-2",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-guangzhou-open-1",
                            "ap-guangzhou-3",
                            "ap-guangzhou-4",
                            "ap-chengdu-1",
                            "ap-chengdu-2"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0
                            ],
                            "MasterZone": [
                                "ap-guangzhou-2"
                            ],
                            "SlaveZone": [
                                "ap-guangzhou-2"
                            ],
                            "BackupZone": [
                                "ap-guangzhou-2"
                            ]
                        },
                        "Zone": "ap-guangzhou-2",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 1000,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 2400,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 4400,
                                        "Iops": 0,
                                        "Info": "Medium-scale game apps with hundreds of thousands of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 7200,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 18000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 25000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 37689,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 40919,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 61378,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 122755,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 0,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 245509,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Status": 1,
                        "ZoneName": "Guangzhou Zone 3",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 30,
                        "IsDefaultZone": false,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1"
                        ],
                        "DrZone": [
                            "ap-shanghai-1",
                            "ap-shanghai-2",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-guangzhou-open-1",
                            "ap-guangzhou-2",
                            "ap-guangzhou-4",
                            "ap-seoul-1",
                            "ap-chengdu-1",
                            "ap-chengdu-2"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0
                            ],
                            "MasterZone": [
                                "ap-guangzhou-3"
                            ],
                            "SlaveZone": [
                                "ap-guangzhou-3"
                            ],
                            "BackupZone": [
                                "ap-guangzhou-3"
                            ]
                        },
                        "Zone": "ap-guangzhou-3",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 1000,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 2400,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 4400,
                                        "Iops": 0,
                                        "Info": "Medium-scale game apps with hundreds of thousands of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 7200,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 18000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 25000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 37689,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 40919,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 61378,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 122755,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 0,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 245509,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Status": 4,
                        "ZoneName": "Guangzhou Zone 1",
                        "IsCustom": true,
                        "IsSupportDr": false,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 30,
                        "IsDefaultZone": false,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0
                            ],
                            "MasterZone": [
                                "ap-guangzhou-1"
                            ],
                            "SlaveZone": [
                                "ap-guangzhou-1"
                            ],
                            "BackupZone": [
                                "ap-guangzhou-1"
                            ]
                        },
                        "Zone": "ap-guangzhou-1",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 360,
                                        "Cpu": 0,
                                        "VolumeMin": 10,
                                        "VolumeMax": 500,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 120,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 500,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 1000,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 500,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 2400,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 4400,
                                        "Iops": 0,
                                        "Info": "Medium-scale game apps with hundreds of thousands of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 7200,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 12000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 15000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 18000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 24000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 23000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 48000,
                                        "Cpu": 0,
                                        "VolumeMin": 1000,
                                        "VolumeMax": 1000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 37000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Status": 2,
                        "ZoneName": "Guangzhou Zone 4",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 30,
                        "IsDefaultZone": true,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1",
                            "2"
                        ],
                        "DrZone": [
                            "ap-shanghai-1",
                            "ap-shanghai-2",
                            "ap-shanghai-3",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-guangzhou-open-1",
                            "ap-guangzhou-2",
                            "ap-guangzhou-3",
                            "na-ashburn-1",
                            "ap-chengdu-1",
                            "ap-chengdu-2",
                            "ap-bangkok-1"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0
                            ],
                            "MasterZone": [
                                "ap-guangzhou-4"
                            ],
                            "SlaveZone": [
                                "ap-guangzhou-4"
                            ],
                            "BackupZone": [
                                "ap-guangzhou-4"
                            ]
                        },
                        "Zone": "ap-guangzhou-4",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 1000,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 2400,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 4400,
                                        "Iops": 0,
                                        "Info": "Medium-scale game apps with hundreds of thousands of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 7200,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 18000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 25000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 37689,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 40919,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 61378,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 122755,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 0,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 245509,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "RegionName": "Bangkok",
                "Area": "Asia Pacific",
                "IsDefaultRegion": 0,
                "Region": "ap-bangkok",
                "ZonesConf": [
                    {
                        "Status": 2,
                        "ZoneName": "Bangkok Zone 1",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 30,
                        "IsDefaultZone": true,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1"
                        ],
                        "DrZone": [
                            "ap-guangzhou-4"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0
                            ],
                            "MasterZone": [
                                "ap-bangkok-1"
                            ],
                            "SlaveZone": [
                                "ap-bangkok-1"
                            ],
                            "BackupZone": [
                                "ap-bangkok-1"
                            ]
                        },
                        "Zone": "ap-bangkok-1",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 1000,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 2400,
                                        "Iops": 0,
                                        "Info": "Small-scale game apps with tens of thousands of DAUs or widget apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 4400,
                                        "Iops": 0,
                                        "Info": "Medium-scale game apps with hundreds of thousands of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 7200,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 18000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 25000,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 37689,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 40919,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 61378,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 0,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 122755,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "High-availability edition",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 0,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 0,
                                        "Qps": 245509,
                                        "Iops": 0,
                                        "Info": "Large-scale game apps with millions of DAUs",
                                        "Status": 0
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "f1ccdafe-6803-455e-bb84-e33c08ba8247"
    }
}
```

