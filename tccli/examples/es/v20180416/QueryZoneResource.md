**Example 1: 获取可用区资源情况**

获取可用区资源情况

Input: 

```
tccli es QueryZoneResource --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --Zones ap-beijing-3 ap-beijing-4 \
    --OptType create \
    --ChargeType PREPAID \
    --EsVersion 7.5.1
```

Output: 
```
{
    "Response": {
        "ZoneResources": [
            {
                "Available": true,
                "NodeTypeList": [
                    {
                        "Available": true,
                        "LocalDiskInfo": {
                            "LocalDiskType": "abc",
                            "LocalDiskSize": 1,
                            "LocalDiskCount": 1
                        },
                        "DiskCountRange": {
                            "Max": 1,
                            "Min": 1
                        },
                        "SsdAvailable": false,
                        "SsdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Max": 1,
                            "Min": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "SsdSoldOutReason": "abc",
                        "BssdAvailable": true,
                        "BssdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Max": 1,
                            "Min": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BssdSoldOutReason": "abc",
                        "NodeTypeInfo": {
                            "Mem": 1,
                            "Cpu": 1,
                            "Desc": "abc"
                        },
                        "SataAvailable": false,
                        "NodeTypeName": "abc",
                        "SataSoldOutReason": "abc",
                        "SataDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Max": 1,
                            "Min": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputAvailable": true,
                        "HSsdDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputSoldOutReason": "abc",
                        "HSsdSoldOutReason": "abc",
                        "HSsdAvailable": true,
                        "ThroughputDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BigDataAvailable": true,
                        "BigDataSoldOutReason": "abc",
                        "BigDataDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "HighIOAvailable": true,
                        "HighIOSoldOutReason": "abc",
                        "HighIODiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        }
                    },
                    {
                        "Available": true,
                        "LocalDiskInfo": {
                            "LocalDiskType": "abc",
                            "LocalDiskSize": 1,
                            "LocalDiskCount": 1
                        },
                        "DiskCountRange": {
                            "Max": 1,
                            "Min": 1
                        },
                        "SsdAvailable": false,
                        "SsdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "SsdSoldOutReason": "abc",
                        "BssdAvailable": false,
                        "BssdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BssdSoldOutReason": "abc",
                        "NodeTypeInfo": {
                            "Mem": 1,
                            "Cpu": 1,
                            "Desc": "abc"
                        },
                        "SataAvailable": false,
                        "NodeTypeName": "abc",
                        "SataSoldOutReason": "abc",
                        "SataDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputAvailable": true,
                        "HSsdDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputSoldOutReason": "abc",
                        "HSsdSoldOutReason": "abc",
                        "HSsdAvailable": true,
                        "ThroughputDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BigDataAvailable": true,
                        "BigDataSoldOutReason": "abc",
                        "BigDataDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "HighIOAvailable": true,
                        "HighIOSoldOutReason": "abc",
                        "HighIODiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        }
                    },
                    {
                        "Available": true,
                        "LocalDiskInfo": {
                            "LocalDiskType": "abc",
                            "LocalDiskSize": 1,
                            "LocalDiskCount": 1
                        },
                        "DiskCountRange": {
                            "Max": 1,
                            "Min": 1
                        },
                        "SsdAvailable": false,
                        "SsdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "SsdSoldOutReason": "abc",
                        "BssdAvailable": false,
                        "BssdDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BssdSoldOutReason": "abc",
                        "NodeTypeInfo": {
                            "Mem": 1,
                            "Cpu": 1,
                            "Desc": "abc"
                        },
                        "SataAvailable": false,
                        "NodeTypeName": "abc",
                        "SataSoldOutReason": "abc",
                        "SataDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Min": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputAvailable": true,
                        "HSsdDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "ThroughputSoldOutReason": "abc",
                        "HSsdSoldOutReason": "abc",
                        "HSsdAvailable": true,
                        "ThroughputDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "BigDataAvailable": true,
                        "BigDataSoldOutReason": "abc",
                        "BigDataDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        },
                        "HighIOAvailable": true,
                        "HighIOSoldOutReason": "abc",
                        "HighIODiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1,
                            "DiskCountMin": 1,
                            "DiskCountMax": 1
                        }
                    }
                ],
                "AvailNodeFamilies": [
                    "abc"
                ],
                "ZoneName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

