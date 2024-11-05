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
        "Total": 1,
        "VpcFwGroupLst": [
            {
                "FwGroupId": "cfwg-48b0ce59",
                "FwGroupName": "[autotest][勿删]自动化测试",
                "Mode": 1,
                "SwitchMode": 1,
                "FwVpcCidr": "10.0.0.1/24",
                "Status": 0,
                "CdcId": "cdc-1903e2",
                "CdcName": "自动化上海CDC",
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
                        "PeerConnectionId": [],
                        "PeerConnectionName": [],
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

