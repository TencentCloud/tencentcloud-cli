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
                "RegionCnName": "广州",
                "Zones": [
                    {
                        "Zone": "ap-guangzhou-3",
                        "ZoneId": 100003,
                        "ZoneCnName": "广州三区",
                        "ZoneName": "广州三区",
                        "Types": [
                            {
                                "Type": "SD",
                                "Version": "v1.5",
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
                                "Prepayment": true
                            },
                            {
                                "Type": "HP",
                                "Version": "v1.5",
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    }
                                ],
                                "Prepayment": false
                            },
                            {
                                "Type": "SD",
                                "Version": "v3.1",
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
                                "Prepayment": true
                            },
                            {
                                "Type": "HP",
                                "Version": "v3.1",
                                "Protocols": [
                                    {
                                        "Protocol": "NFS",
                                        "SaleStatus": "saling"
                                    },
                                    {
                                        "Protocol": "CIFS",
                                        "SaleStatus": "no_saling"
                                    }
                                ],
                                "Prepayment": false
                            },
                            {
                                "Type": "TB",
                                "Version": "v4.0",
                                "Protocols": [
                                    {
                                        "Protocol": "TURBO",
                                        "SaleStatus": "sale_out"
                                    }
                                ],
                                "Prepayment": false
                            },
                            {
                                "Type": "TP",
                                "Version": "v4.0",
                                "Protocols": [
                                    {
                                        "Protocol": "TURBO",
                                        "SaleStatus": "sale_out"
                                    }
                                ],
                                "Prepayment": false
                            }
                        ]
                    }
                ],
                "RegionStatus": "AVAILABLE"
            }
        ],
        "RequestId": "02f70cc9-3c48-4a34-9491-31faec9944af"
    },
    "code": 0
}
```

