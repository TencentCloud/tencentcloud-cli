**Example 1: 获取数据库可售卖规格**



Input: 

```
tccli cdb DescribeCdbZoneConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DataResult": {
            "Configs": [
                {
                    "Cpu": 1,
                    "DeviceType": "CUSTOM",
                    "EngineType": "InnoDB",
                    "Id": 11,
                    "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                    "Iops": 1200,
                    "Memory": 1000,
                    "Status": 0,
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                },
                {
                    "Cpu": 1,
                    "DeviceType": "CUSTOM",
                    "EngineType": "InnoDB",
                    "Id": 12,
                    "Info": "日活跃用户数上万的小型游戏应用或百万人级别的工具类应用",
                    "Iops": 2000,
                    "Memory": 2000,
                    "Status": 0,
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                },
                {
                    "Cpu": 8,
                    "DeviceType": "CUSTOM",
                    "EngineType": "RocksDB",
                    "Id": 175,
                    "Info": "日活跃用户数在百万人级别的大型游戏应用",
                    "Iops": 28000,
                    "Memory": 32000,
                    "Status": 0,
                    "VolumeMax": 3000,
                    "VolumeMin": 25,
                    "VolumeStep": 5
                }
            ],
            "Regions": [
                {
                    "Area": "华东地区",
                    "IsDefaultRegion": 0,
                    "Region": "ap-shanghai",
                    "RegionConfig": [
                        {
                            "DrZone": [
                                "ap-guangzhou-2",
                                "ap-guangzhou-3",
                                "ap-guangzhou-4",
                                "ap-guangzhou-5",
                                "ap-guangzhou-6",
                                "ap-guangzhou-7"
                            ],
                            "EngineType": [
                                "InnoDB",
                                "RocksDB"
                            ],
                            "ExClusterRemoteRoZone": [],
                            "ExClusterStatus": 3,
                            "ExClusterZoneConf": {
                                "BackupZone": [],
                                "DeployMode": [
                                    0
                                ],
                                "MasterZone": [],
                                "SlaveZone": []
                            },
                            "HourInstanceSaleMaxNum": 10000,
                            "IsBm": false,
                            "IsCustom": true,
                            "IsDefaultZone": false,
                            "IsSupportDr": true,
                            "IsSupportIpv6": false,
                            "IsSupportRemoteRo": true,
                            "IsSupportVpc": true,
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
                            "RemoteRoZone": [
                                "ap-beijing-1",
                                "ap-beijing-2",
                                "ap-beijing-3"
                            ],
                            "SellType": [
                                {
                                    "ConfigIds": [],
                                    "EngineVersion": [],
                                    "TypeName": "CVM"
                                },
                                {
                                    "ConfigIds": [
                                        11,
                                        12,
                                        175
                                    ],
                                    "EngineVersion": [
                                        "5.5",
                                        "5.6",
                                        "5.7",
                                        "8.0"
                                    ],
                                    "TypeName": "Z3"
                                }
                            ],
                            "Status": 3,
                            "Zone": "ap-shanghai-1",
                            "ZoneConf": {
                                "BackupZone": [
                                    "ap-shanghai-1"
                                ],
                                "DeployMode": [
                                    0,
                                    1
                                ],
                                "MasterZone": [
                                    "ap-shanghai-1"
                                ],
                                "SlaveZone": [
                                    "ap-shanghai-1"
                                ]
                            },
                            "ZoneId": 200001,
                            "ZoneName": "上海一区"
                        }
                    ],
                    "RegionName": "上海"
                }
            ]
        },
        "RequestId": "33ad58ce-64d3-5ef4-101a-1823da6f7cad"
    }
}
```

