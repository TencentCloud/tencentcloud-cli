**Example 1: 获取高防IP资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPIPInstances --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0381c271-292d-4e2a-adcc-cd7bcd6977a7",
        "InstanceList": [
            {
                "InstanceDetail": {
                    "EipList": [
                        "2402:4e00:31:804::17"
                    ],
                    "InstanceId": "bgpip-00000001"
                },
                "SpecificationLimit": {
                    "ProtectBandwidth": 30000,
                    "ProtectCCQPS": 40000,
                    "ElasticBandwidth": 50000,
                    "NormalBandwidth": 1000,
                    "ForwardRulesLimit": 60,
                    "AutoRenewFlag": 0,
                    "Line": 1
                },
                "Usage": {
                    "PortRulesUsage": 0,
                    "DomainRulesUsage": 0,
                    "Last7DayAttackCount": 0
                },
                "Region": {
                    "Region": "ap-shanghai"
                },
                "PackInfo": null,
                "StaticPackRelation": null,
                "EipAddressPackRelation": null,
                "AnycastOutPackRelation": null,
                "Tgw": 2,
                "ZoneId": 0,
                "Name": "",
                "V6Flag": 1,
                "Domain": "",
                "Status": "idle",
                "ExpiredTime": "2023-01-08 21:22:24",
                "CreatedTime": "2022-12-08 21:22:24",
                "EipAddressStatus": "",
                "EipFlag": 0,
                "EipAddressInfo": null,
                "ConvoyId": "",
                "DamDDoSStatus": 0,
                "BGPIPChannelFlag": 0,
                "TagInfoList": [],
                "InstanceVersion": 3
            }
        ],
        "Total": 12
    }
}
```

