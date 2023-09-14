**Example 1: 获取云数据库可售卖规格**

获取云数据库可售卖规格

Input: 

```
tccli cdb DescribeDBZoneConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
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
                            "ap-shanghai-1"
                        ],
                        "RemoteRoZone": [
                            "ap-shanghai-2"
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
                                    "5.7",
                                    "8.0"
                                ],
                                "Configs": [
                                    {
                                        "Device": "Z3",
                                        "Type": "高可用版",
                                        "CdbType": "CUSTOM",
                                        "DeviceTypeName": "通用型",
                                        "DeviceType": "UNIVERSAL",
                                        "EngineType": "InnoDB",
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

