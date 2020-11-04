**Example 1: 查询区域可用情况**



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
                        "ZoneCnName": "广州二区",
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
                        "ZoneCnName": "广州三区",
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
                        "ZoneCnName": "广州四区",
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

