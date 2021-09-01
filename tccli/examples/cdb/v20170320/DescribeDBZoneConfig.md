**Example 1: 获取云数据库可售卖规格**



Input: 

```
tccli cdb DescribeDBZoneConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Items": [
            {
                "RegionName": "广州",
                "Area": "华南地区",
                "IsDefaultRegion": 0,
                "Region": "ap-guangzhou",
                "ZonesConf": [
                    {
                        "Status": 1,
                        "ZoneName": "广州二区",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportRemoteRo": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 100,
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
                            "ap-shanghai-3",
                            "ap-shanghai-4",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-beijing-3",
                            "ap-beijing-4",
                            "ap-guangzhou-open-1",
                            "ap-guangzhou-3",
                            "ap-guangzhou-4",
                            "ap-chengdu-1",
                            "ap-chengdu-2",
                            "ap-chongqing-1",
                            "na-ashburn-1",
                            "ap-nanjing-1"
                        ],
                        "RemoteRoZone": [
                            "ap-shanghai-2",
                            "ap-hongkong-2"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0,
                                1
                            ],
                            "MasterZone": [
                                "ap-guangzhou-2"
                            ],
                            "SlaveZone": [
                                "ap-guangzhou-2",
                                "ap-guangzhou-3"
                            ],
                            "BackupZone": [
                                "ap-guangzhou-2",
                                "ap-guangzhou-3"
                            ]
                        },
                        "Zone": "ap-guangzhou-2",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7",
                                    "8.0"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 600,
                                        "Qps": 1000,
                                        "Iops": 900,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1000,
                                        "Qps": 2400,
                                        "Iops": 1500,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 2,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1500,
                                        "Qps": 4400,
                                        "Iops": 3000,
                                        "Info": "日活跃用户数上十万人级别的中型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 2500,
                                        "Qps": 7200,
                                        "Iops": 6000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 5000,
                                        "Qps": 18000,
                                        "Iops": 12000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 8,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 10000,
                                        "Qps": 25000,
                                        "Iops": 18000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 18000,
                                        "Qps": 37689,
                                        "Iops": 24000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 40919,
                                        "Iops": 30000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 61378,
                                        "Iops": 32000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 192000,
                                        "Cpu": 24,
                                        "VolumeMin": 50,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 28000,
                                        "Qps": 100000,
                                        "Iops": 42000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 24,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 32000,
                                        "Qps": 122755,
                                        "Iops": 48000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 48,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 64000,
                                        "Qps": 245509,
                                        "Iops": 75000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 690000,
                                        "Cpu": 80,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 80000,
                                        "Qps": 300000,
                                        "Iops": 90000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "RegionName": "上海",
                "Area": "华东地区",
                "IsDefaultRegion": 0,
                "Region": "ap-shanghai",
                "ZonesConf": [
                    {
                        "Status": 1,
                        "ZoneName": "上海一区",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportRemoteRo": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 100,
                        "IsDefaultZone": false,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1",
                            "2"
                        ],
                        "DrZone": [
                            "ap-guangzhou-2",
                            "ap-guangzhou-3",
                            "ap-guangzhou-4",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-beijing-3",
                            "ap-beijing-4",
                            "ap-guangzhou-open-1",
                            "ap-shanghai-2",
                            "ap-shanghai-3",
                            "ap-shanghai-4",
                            "ap-chengdu-1",
                            "ap-chengdu-2"
                        ],
                        "RemoteRoZone": [
                            "ap-shanghai-3",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-beijing-3",
                            "ap-beijing-5",
                            "ap-guangzhou-2",
                            "ap-guangzhou-3"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0,
                                1
                            ],
                            "MasterZone": [
                                "ap-shanghai-1"
                            ],
                            "SlaveZone": [
                                "ap-shanghai-1",
                                "ap-shanghai-2"
                            ],
                            "BackupZone": [
                                "ap-shanghai-1",
                                "ap-shanghai-2"
                            ]
                        },
                        "Zone": "ap-shanghai-1",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7",
                                    "8.0"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 600,
                                        "Qps": 1000,
                                        "Iops": 900,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1000,
                                        "Qps": 2400,
                                        "Iops": 1500,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 2,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1500,
                                        "Qps": 4400,
                                        "Iops": 3000,
                                        "Info": "日活跃用户数上十万人级别的中型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 2500,
                                        "Qps": 7200,
                                        "Iops": 6000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 5000,
                                        "Qps": 18000,
                                        "Iops": 12000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 8,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 10000,
                                        "Qps": 25000,
                                        "Iops": 18000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 18000,
                                        "Qps": 37689,
                                        "Iops": 24000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 40919,
                                        "Iops": 30000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 61378,
                                        "Iops": 32000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 24,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 32000,
                                        "Qps": 122755,
                                        "Iops": 48000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 48,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 64000,
                                        "Qps": 245509,
                                        "Iops": 75000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 690000,
                                        "Cpu": 80,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 80000,
                                        "Qps": 300000,
                                        "Iops": 90000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Status": 2,
                        "ZoneName": "上海二区",
                        "IsCustom": true,
                        "IsSupportDr": true,
                        "IsSupportRemoteRo": true,
                        "IsSupportVpc": true,
                        "HourInstanceSaleMaxNum": 100,
                        "IsDefaultZone": false,
                        "IsBm": false,
                        "PayType": [
                            "0",
                            "1",
                            "2"
                        ],
                        "DrZone": [
                            "ap-guangzhou-1",
                            "ap-guangzhou-2",
                            "ap-guangzhou-3",
                            "ap-guangzhou-4",
                            "ap-shanghai-1",
                            "ap-shanghai-3",
                            "ap-shanghai-4",
                            "ap-beijing-1",
                            "ap-beijing-2",
                            "ap-beijing-3",
                            "ap-beijing-4",
                            "ap-guangzhou-open-1",
                            "ap-chengdu-1",
                            "ap-chengdu-2"
                        ],
                        "RemoteRoZone": [
                            "ap-beijing-1",
                            "ap-beijing-5"
                        ],
                        "ProtectMode": [
                            "0",
                            "1",
                            "2"
                        ],
                        "ZoneConf": {
                            "DeployMode": [
                                0,
                                1
                            ],
                            "MasterZone": [
                                "ap-shanghai-2"
                            ],
                            "SlaveZone": [
                                "ap-shanghai-1",
                                "ap-shanghai-2",
                                "ap-shanghai-4",
                                "ap-shanghai-5"
                            ],
                            "BackupZone": [
                                "ap-shanghai-1",
                                "ap-shanghai-2",
                                "ap-shanghai-4",
                                "ap-shanghai-5"
                            ]
                        },
                        "Zone": "ap-shanghai-2",
                        "SellType": [
                            {
                                "TypeName": "Z3",
                                "EngineVersion": [
                                    "5.5",
                                    "5.6",
                                    "5.7",
                                    "8.0"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 1000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 600,
                                        "Qps": 1000,
                                        "Iops": 900,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 2000,
                                        "Cpu": 1,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1000,
                                        "Qps": 2400,
                                        "Iops": 1500,
                                        "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 4000,
                                        "Cpu": 2,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 1500,
                                        "Qps": 4400,
                                        "Iops": 3000,
                                        "Info": "日活跃用户数上十万人级别的中型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 8000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 2500,
                                        "Qps": 7200,
                                        "Iops": 6000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 16000,
                                        "Cpu": 2,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 6000,
                                        "Qps": 18000,
                                        "Iops": 9000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 16000,
                                        "Cpu": 4,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 5000,
                                        "Qps": 18000,
                                        "Iops": 12000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 16000,
                                        "Cpu": 4,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 6000,
                                        "Qps": 18000,
                                        "Iops": 9000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 32000,
                                        "Cpu": 8,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 10000,
                                        "Qps": 25000,
                                        "Iops": 18000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 32000,
                                        "Cpu": 4,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 12000,
                                        "Qps": 25000,
                                        "Iops": 18000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 32000,
                                        "Cpu": 8,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 12000,
                                        "Qps": 25000,
                                        "Iops": 18000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 64000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 18000,
                                        "Qps": 37689,
                                        "Iops": 24000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 64000,
                                        "Cpu": 16,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 37689,
                                        "Iops": 24000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 64000,
                                        "Cpu": 8,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 37689,
                                        "Iops": 24000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 96000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 40919,
                                        "Iops": 30000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 128000,
                                        "Cpu": 32,
                                        "VolumeMin": 200,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 36000,
                                        "Qps": 61378,
                                        "Iops": 48000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 128000,
                                        "Cpu": 16,
                                        "VolumeMin": 200,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 36000,
                                        "Qps": 61378,
                                        "Iops": 48000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 128000,
                                        "Cpu": 16,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 24000,
                                        "Qps": 61378,
                                        "Iops": 32000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 244000,
                                        "Cpu": 24,
                                        "VolumeMin": 25,
                                        "VolumeMax": 3000,
                                        "VolumeStep": 5,
                                        "Connection": 32000,
                                        "Qps": 122755,
                                        "Iops": 48000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 256000,
                                        "Cpu": 32,
                                        "VolumeMin": 200,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 48000,
                                        "Qps": 122755,
                                        "Iops": 56000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 488000,
                                        "Cpu": 48,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 64000,
                                        "Qps": 245509,
                                        "Iops": 75000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "EXCLUSIVE",
                                        "Memory": 512000,
                                        "Cpu": 64,
                                        "VolumeMin": 200,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 86000,
                                        "Qps": 310001,
                                        "Iops": 99000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    },
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "Memory": 690000,
                                        "Cpu": 80,
                                        "VolumeMin": 6000,
                                        "VolumeMax": 6000,
                                        "VolumeStep": 5,
                                        "Connection": 80000,
                                        "Qps": 300000,
                                        "Iops": 90000,
                                        "Info": "日活跃用户数在百万人级别的大型游戏应用",
                                        "Status": 0,
                                        "Tag": 0
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "b22dae9b-61ae-4af0-94ed-73370fe272a5"
    }
}
```

