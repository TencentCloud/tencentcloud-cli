**Example 1: 获取Logstash可用区资源情况**

获取Logstash可用区资源情况

Input: 

```
tccli es QueryZoneResourceForLogstash --cli-unfold-argument  \
    --Zones ap-beijing-3 ap-beijing-4 \
    --ChargeType PREPAID
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
                            "LocalDiskType": "t",
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
                            "DiskCountMax": 1,
                            "DiskCountMin": 1
                        },
                        "SsdSoldOutReason": "te",
                        "NodeTypeInfo": {
                            "Mem": 1,
                            "Cpu": 1,
                            "Desc": "1"
                        },
                        "SataAvailable": false,
                        "NodeTypeName": "tes",
                        "SataSoldOutReason": "test",
                        "SataDiskSizeRange": {
                            "Med": 1,
                            "Sml": 1,
                            "Max": 1,
                            "Min": 1
                        },
                        "ThroughputAvailable": true,
                        "HSsdDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1
                        },
                        "ThroughputSoldOutReason": "test",
                        "HSsdSoldOutReason": "test",
                        "HSsdAvailable": true,
                        "ThroughputDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1
                        },
                        "HighIOSoldOutReason": "",
                        "HighIODiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1
                        },
                        "BigDataSoldOutReason": "",
                        "BigDataDiskSizeRange": {
                            "Min": 1,
                            "Sml": 1,
                            "Med": 1,
                            "Max": 1
                        },
                        "BigDataAvailable": false,
                        "HighIOAvailable": false
                    }
                ],
                "AvailNodeFamilies": [
                    "test"
                ],
                "ZoneName": "test"
            }
        ],
        "RequestId": "xxxx-xxx-test-1"
    }
}
```

