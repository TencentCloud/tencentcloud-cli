**Example 1: 示例**



Input: 

```
tccli tchousex DescribeMCPRegionZone --cli-unfold-argument  \
    --InstanceType mcp
```

Output: 
```
{
    "Response": {
        "ClusterTypes": [
            0
        ],
        "ErrorMsg": "",
        "IsYunti": false,
        "Items": [
            {
                "Desc": "",
                "Name": "china",
                "Regions": [
                    {
                        "Count": 6,
                        "Desc": "",
                        "Name": "ap-chongqing",
                        "OfflineResource": 0,
                        "OfflineResourceLimit": 128,
                        "RealtimeResource": 0,
                        "RealtimeResourceLimit": 128,
                        "RegionID": 19,
                        "RegionId": 0,
                        "Zones": [
                            {
                                "Desc": "",
                                "Encrypt": 0,
                                "Name": "ap-chongqing-1",
                                "ZoneID": 190001,
                                "ZoneId": 190001
                            }
                        ]
                    },
                    {
                        "Count": 0,
                        "Desc": "",
                        "Name": "ap-guagnzhou",
                        "OfflineResource": 0,
                        "OfflineResourceLimit": 128,
                        "RealtimeResource": 0,
                        "RealtimeResourceLimit": 128,
                        "RegionID": 1,
                        "RegionId": 0,
                        "Zones": [
                            {
                                "Desc": "",
                                "Encrypt": 0,
                                "Name": "ap-guangzhou-3",
                                "ZoneID": 100003,
                                "ZoneId": 100003
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "7a1763fe-3d42-4fa1-91b5-c102348d301d",
        "VersionInfos": [
            {
                "ClusterType": 0,
                "Versions": [
                    "1.1.0_REL",
                    "1.0.0_REL"
                ]
            }
        ],
        "Versions": [
            "1.1.0_REL",
            "1.0.0_REL"
        ]
    }
}
```

