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
                "RegionCnName": "广州",
                "RegionName": "gz",
                "RegionStatus": "AVAILABLE",
                "Zones": [
                    {
                        "Types": [
                            {
                                "Prepayment": true,
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    },
                                    {
                                        "Protocol": "CIFS",
                                        "SaleStatus": "saling"
                                    }
                                ],
                                "Type": "SD"
                            }
                        ],
                        "Zone": "ap-guangzhou-3",
                        "ZoneCnName": "广州三区",
                        "ZoneId": 100003,
                        "ZoneName": "广州三区"
                    },
                    {
                        "Types": [
                            {
                                "Prepayment": true,
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    },
                                    {
                                        "Protocol": "CIFS",
                                        "SaleStatus": "saling"
                                    }
                                ],
                                "Type": "SD"
                            }
                        ],
                        "Zone": "ap-guangzhou-4",
                        "ZoneCnName": "广州四区",
                        "ZoneId": 100004,
                        "ZoneName": "广州四区"
                    },
                    {
                        "Types": [
                            {
                                "Prepayment": true,
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    },
                                    {
                                        "Protocol": "CIFS",
                                        "SaleStatus": "saling"
                                    }
                                ],
                                "Type": "SD"
                            }
                        ],
                        "Zone": "ap-guangzhou-6",
                        "ZoneCnName": "广州六区",
                        "ZoneId": 100006,
                        "ZoneName": "广州六区"
                    }
                ]
            }
        ],
        "RequestId": "f3585511-5134-43f2-ba14-b4b528119fa3"
    }
}
```

