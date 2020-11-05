**Example 1: Querying the availability of a region**



Input: 

```
tccli cfs DescribeAvailableZoneInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionZones": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "gz",
                "RegionStatus": "AVAILABLE",
                "Zones": [
                    {
                        "Zone": "ap-guangzhou-2",
                        "ZoneId": 100002,
                        "ZoneCnName": "Guangzhou Zone 2",
                        "Types": [
                            {
                                "Type": "SD",
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Zone": "ap-guangzhou-3",
                        "ZoneId": 100003,
                        "ZoneCnName": "Guangzhou Zone 3",
                        "Types": [
                            {
                                "Type": "SD",
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Zone": "ap-guangzhou-4",
                        "ZoneId": 100004,
                        "ZoneCnName": "Guangzhou Zone 4",
                        "Types": [
                            {
                                "Type": "SD",
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "a7493b9c-8650-409a-a950-8d4afa18b5ec"
    }
}
```

