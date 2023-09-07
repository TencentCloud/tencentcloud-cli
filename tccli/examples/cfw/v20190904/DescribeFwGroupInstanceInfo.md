**Example 1: 获取租户所有VPC防火墙(组)及VPC防火墙实例卡片信息**

获取租户所有VPC防火墙(组)及VPC防火墙实例卡片信息

Input: 

```
tccli cfw DescribeFwGroupInstanceInfo --cli-unfold-argument  \
    --Filters.0.Name FwGroupId \
    --Filters.0.Values cfwg-xxxxxxxx \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 0 \
    --StartTime 2023-02-08 20:19:13 \
    --EndTime 2023-02-08 20:19:13 \
    --Order desc \
    --By FwGroupId
```

Output: 
```
{
    "Response": {
        "RequestId": "1433cc95-0a1e-41e9-8c80-773452c3956a",
        "Total": 3,
        "VpcFwGroupLst": [
            {
                "FwGroupId": "cfwg-091403ba",
                "FwGroupName": "vpc11",
                "Mode": 0,
                "SwitchMode": 1,
                "FwVpcCidr": "",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-singapore"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-091403ba",
                        "FwInsName": "vpc11-Singapore",
                        "FwInsId": "cfwew-091403ba",
                        "FwMode": 0,
                        "CcnId": null,
                        "CcnName": null,
                        "PeerConnectionId": [
                            "pcx-agelgm26"
                        ],
                        "PeerConnectionName": [
                            "dora对等连接"
                        ],
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-091403ba",
                                "Region": "ap-singapore",
                                "RegionZh": "Singapore",
                                "RegionDetail": "Southeast Asia",
                                "ZoneZh": "Singapore Zone 1",
                                "ZoneZhBack": "Singapore Zone 1",
                                "BandWidth": 1024
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "VPC",
                                "Num": 2
                            }
                        ],
                        "JoinInsIdLst": [
                            "vpc-1mu72m45",
                            "vpc-evukp8gr"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-mowa99k4",
                                "VpcId": "vpc-1mu72m45",
                                "IpAddress": "172.18.1.20"
                            },
                            {
                                "GatewayId": "havip-h4fk33t8",
                                "VpcId": "vpc-evukp8gr",
                                "IpAddress": "192.168.1.4"
                            }
                        ],
                        "JoinInsNum": 2,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-01-16 13:32:02",
                        "Width": 1024,
                        "UserVpcWidth": 6144,
                        "RuleUsed": 17,
                        "RuleMax": 0,
                        "FlowMax": 0
                    }
                ]
            },
            {
                "FwGroupId": "cfwg-bd65c35d",
                "FwGroupName": "ill-VPC防火墙",
                "Mode": 0,
                "SwitchMode": 1,
                "FwVpcCidr": "",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "na-siliconvalley"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-bd65c35d",
                        "FwInsName": "ill-VPC防火墙-Silicon Valley",
                        "FwInsId": "cfwew-bd65c35d",
                        "FwMode": 0,
                        "CcnId": null,
                        "CcnName": null,
                        "PeerConnectionId": [
                            "pcx-qc3u5vny"
                        ],
                        "PeerConnectionName": [
                            "ill-AC对等"
                        ],
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-bd65c35d",
                                "Region": "na-siliconvalley",
                                "RegionZh": "Silicon Valley",
                                "RegionDetail": "US West",
                                "ZoneZh": "Silicon Valley Zone 1",
                                "ZoneZhBack": "Silicon Valley Zone 1",
                                "BandWidth": 1026
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "VPC",
                                "Num": 2
                            }
                        ],
                        "JoinInsIdLst": [
                            "vpc-bogtkdw5",
                            "vpc-lryryblf"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-qv2vu0ko",
                                "VpcId": "vpc-bogtkdw5",
                                "IpAddress": "10.1.0.4"
                            },
                            {
                                "GatewayId": "havip-pnhsiig8",
                                "VpcId": "vpc-lryryblf",
                                "IpAddress": "192.168.0.4"
                            }
                        ],
                        "JoinInsNum": 2,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-03-02 15:02:05",
                        "Width": 1026,
                        "UserVpcWidth": 6144,
                        "RuleUsed": 19,
                        "RuleMax": 20000,
                        "FlowMax": 0
                    }
                ]
            },
            {
                "FwGroupId": "cfwg-9d364c8c",
                "FwGroupName": "ill-vpc",
                "Mode": 0,
                "SwitchMode": 1,
                "FwVpcCidr": "auto",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-guangzhou"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-9d364c8c",
                        "FwInsName": "ill-vpc-实例",
                        "FwInsId": "cfwew-6ea63bd1",
                        "FwMode": 0,
                        "CcnId": null,
                        "CcnName": null,
                        "PeerConnectionId": [
                            "pcx-jbd9cfr2"
                        ],
                        "PeerConnectionName": [
                            "01-02"
                        ],
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-6ea63bd1",
                                "Region": "ap-guangzhou",
                                "RegionZh": "Guangzhou",
                                "RegionDetail": "South China",
                                "ZoneZh": "Guangzhou Zone 3",
                                "ZoneZhBack": "Guangzhou Zone 3",
                                "BandWidth": 1024
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "VPC",
                                "Num": 2
                            }
                        ],
                        "JoinInsIdLst": [
                            "vpc-oqkl55nv",
                            "vpc-r275qh7n"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-pcvydwd0",
                                "VpcId": "vpc-oqkl55nv",
                                "IpAddress": "10.1.0.4"
                            },
                            {
                                "GatewayId": "havip-4jkwh854",
                                "VpcId": "vpc-r275qh7n",
                                "IpAddress": "10.2.0.4"
                            }
                        ],
                        "JoinInsNum": 2,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-05-18 12:12:50",
                        "Width": 1024,
                        "UserVpcWidth": 6144,
                        "RuleUsed": 17,
                        "RuleMax": 20000,
                        "FlowMax": 0
                    }
                ]
            }
        ]
    }
}
```

