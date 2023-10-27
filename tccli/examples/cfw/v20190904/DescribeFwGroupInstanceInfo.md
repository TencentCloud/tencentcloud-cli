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
        "RequestId": "71ed010b-b157-48fb-9439-89aa4549f08b",
        "Total": 4,
        "VpcFwGroupLst": [
            {
                "FwGroupId": "cfwg-bf5fc35b",
                "FwGroupName": "v_tximtan云",
                "Mode": 1,
                "SwitchMode": 4,
                "FwVpcCidr": "",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "CrossUserMode": "0",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-guangzhou"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-bf5fc35b",
                        "FwInsName": "v_tximtan云-广州",
                        "FwInsId": "cfwew-b84148d5",
                        "FwMode": 1,
                        "CcnId": [
                            "ccn-d7vwven5"
                        ],
                        "CcnName": [
                            "v_tximtan云联网testtest"
                        ],
                        "PeerConnectionId": null,
                        "PeerConnectionName": null,
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-b84148d5",
                                "Region": "ap-guangzhou",
                                "RegionZh": "广州",
                                "RegionDetail": "华南地区",
                                "ZoneZh": "广州三区",
                                "ZoneZhBack": "广州三区",
                                "BandWidth": 200
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "VPC",
                                "Num": 3
                            }
                        ],
                        "JoinInsIdLst": [
                            "vpc-i5qssbsx",
                            "vpc-4dte07m3",
                            "vpc-ozfpqh4b"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-03zh52mu",
                                "VpcId": "vpc-losit83n",
                                "IpAddress": "10.174.0.4"
                            }
                        ],
                        "JoinInsNum": 3,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-10-23 10:50:39",
                        "Width": 200,
                        "UserVpcWidth": 11264,
                        "RuleUsed": 56,
                        "RuleMax": 5000,
                        "FlowMax": 116,
                        "EngineVersion": "cfw_v4.cfw4.iteration.1052",
                        "UpdateEnable": 1,
                        "TrafficMode": "Normal"
                    }
                ]
            },
            {
                "FwGroupId": "cfwg-5ddd4aba",
                "FwGroupName": "11",
                "Mode": 0,
                "SwitchMode": 1,
                "FwVpcCidr": "auto",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "CrossUserMode": "0",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-beijing"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-5ddd4aba",
                        "FwInsName": "11-实例1",
                        "FwInsId": "cfwew-aeb45a76",
                        "FwMode": 0,
                        "CcnId": null,
                        "CcnName": null,
                        "PeerConnectionId": [
                            "pcx-98s94zkn"
                        ],
                        "PeerConnectionName": [
                            "11"
                        ],
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-aeb45a76",
                                "Region": "ap-beijing",
                                "RegionZh": "北京",
                                "RegionDetail": "华北地区",
                                "ZoneZh": "北京三区",
                                "ZoneZhBack": "北京三区",
                                "BandWidth": 1300
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "VPC",
                                "Num": 2
                            }
                        ],
                        "JoinInsIdLst": [
                            "vpc-406waega",
                            "vpc-rkm452h0"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-3b8pxpvj",
                                "VpcId": "vpc-406waega",
                                "IpAddress": "192.168.16.52"
                            },
                            {
                                "GatewayId": "havip-aw5siltn",
                                "VpcId": "vpc-rkm452h0",
                                "IpAddress": "172.21.2.36"
                            }
                        ],
                        "JoinInsNum": 2,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-10-20 15:45:47",
                        "Width": 1300,
                        "UserVpcWidth": 11264,
                        "RuleUsed": 54,
                        "RuleMax": 20000,
                        "FlowMax": 3292,
                        "EngineVersion": "cfw_v4.cfw4.iteration.1053",
                        "UpdateEnable": 0,
                        "TrafficMode": "Normal"
                    }
                ]
            },
            {
                "FwGroupId": "cfwg-231dcfcc",
                "FwGroupName": "云联网模式测试---勿删",
                "Mode": 1,
                "SwitchMode": 4,
                "FwVpcCidr": "",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "CrossUserMode": "0",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-beijing"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-231dcfcc",
                        "FwInsName": "云联网模式测试---勿删-北京test",
                        "FwInsId": "cfwew-96389e55",
                        "FwMode": 1,
                        "CcnId": [
                            "ccn-8tvs4l0r"
                        ],
                        "CcnName": [
                            "自定义模式测试中"
                        ],
                        "PeerConnectionId": null,
                        "PeerConnectionName": null,
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-96389e55",
                                "Region": "ap-beijing",
                                "RegionZh": "北京",
                                "RegionDetail": "华北地区",
                                "ZoneZh": "北京三区",
                                "ZoneZhBack": "北京三区",
                                "BandWidth": 1024
                            }
                        ],
                        "JoinInsLst": [
                            {
                                "JoinType": "DIRECTCONNECT",
                                "Num": 2
                            },
                            {
                                "JoinType": "VPC",
                                "Num": 6
                            }
                        ],
                        "JoinInsIdLst": [
                            "dcg-1cwj8teq",
                            "dcg-i3ojjsrm",
                            "vpc-m8zwspqm",
                            "vpc-apg8bqow",
                            "vpc-2moj664m",
                            "vpc-obppmht3",
                            "vpc-e37znkkp",
                            "vpc-3cj1twht"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-mxu8e6j5",
                                "VpcId": "vpc-k0c0xlie",
                                "IpAddress": "10.175.0.4"
                            }
                        ],
                        "JoinInsNum": 8,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-10-12 20:12:32",
                        "Width": 1024,
                        "UserVpcWidth": 11264,
                        "RuleUsed": 56,
                        "RuleMax": 20000,
                        "FlowMax": 886,
                        "EngineVersion": "cfw_v4.0.2.1050",
                        "UpdateEnable": 1,
                        "TrafficMode": "Normal"
                    }
                ]
            },
            {
                "FwGroupId": "cfwg-48b0ce59",
                "FwGroupName": "[autotest][勿删]自动化测试",
                "Mode": 1,
                "SwitchMode": 1,
                "FwVpcCidr": "",
                "Status": 0,
                "CdcId": "",
                "CdcName": "",
                "CrossUserMode": "0",
                "FwSwitchNum": 1,
                "RegionLst": [
                    "ap-shanghai"
                ],
                "FwInstanceLst": [
                    {
                        "FwGroupId": "cfwg-48b0ce59",
                        "FwInsName": "[autotest]【勿动】自动化测试-上海",
                        "FwInsId": "cfwew-091fafd3",
                        "FwMode": 1,
                        "CcnId": [
                            "ccn-2stwf6cr"
                        ],
                        "CcnName": [
                            "[autotest][勿删]自动化测试"
                        ],
                        "PeerConnectionId": null,
                        "PeerConnectionName": null,
                        "FwCvmLst": [
                            {
                                "FwInsId": "cfwew-091fafd3",
                                "Region": "ap-shanghai",
                                "RegionZh": "上海",
                                "RegionDetail": "华东地区",
                                "ZoneZh": "上海二区",
                                "ZoneZhBack": "上海二区",
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
                            "vpc-msa9dvac",
                            "vpc-q9h93ip4"
                        ],
                        "FwGateway": [
                            {
                                "GatewayId": "havip-0zv7jxun",
                                "VpcId": "vpc-eo9n3mq2",
                                "IpAddress": "10.183.0.4"
                            }
                        ],
                        "JoinInsNum": 2,
                        "FwSwitchNum": 1,
                        "Status": 0,
                        "Time": "2023-09-07 12:55:14",
                        "Width": 1024,
                        "UserVpcWidth": 11264,
                        "RuleUsed": 56,
                        "RuleMax": 20000,
                        "FlowMax": 29322,
                        "EngineVersion": "cfw_v4.0.2.1050",
                        "UpdateEnable": 1,
                        "TrafficMode": "Normal"
                    }
                ]
            }
        ]
    }
}
```

