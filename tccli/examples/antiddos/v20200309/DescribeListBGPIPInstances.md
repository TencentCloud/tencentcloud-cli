**Example 1: 获取高防IP资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPIPInstances --cli-unfold-argument  \
    --FilterEipType 1 \
    --FilterRegion ap-guangzhou \
    --FilterName test \
    --FilterDamDDoSStatus 0 \
    --Limit 25 \
    --FilterEipEipAddressStatus BINDING BIND \
    --Offset 0 \
    --FilterInstanceId bgpip-00000001 \
    --FilterIp 1.1.1.1 \
    --FilterLine 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "InstanceList": [
            {
                "Usage": {
                    "PortRulesUsage": 1,
                    "DomainRulesUsage": 1,
                    "Last7DayAttackCount": 1
                },
                "ExpiredTime": "2020-09-22 00:00:00",
                "EipAddressInfo": {
                    "EipBoundRscIns": "xx",
                    "EipBoundRscVip": "xx",
                    "EipBoundRscEni": "xx",
                    "EipAddressRegion": "xx",
                    "ModifyTime": "xx"
                },
                "TagInfoList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "CreatedTime": "2020-09-22 00:00:00",
                "Status": "xx",
                "StaticPackRelation": {
                    "ForwardRulesLimit": 1,
                    "AutoRenewFlag": 1,
                    "ProtectBandwidth": 1,
                    "CurDeadline": "xx",
                    "NormalBandwidth": 1
                },
                "EipAddressPackRelation": {
                    "AutoRenewFlag": 1,
                    "CurDeadline": "2020-09-22 00:00:00",
                    "IpCount": 1
                },
                "SpecificationLimit": {
                    "ProtectCCQPS": 1,
                    "NormalBandwidth": 1,
                    "ElasticBandwidth": 1,
                    "AutoRenewFlag": 1,
                    "ProtectBandwidth": 1,
                    "ForwardRulesLimit": 1,
                    "Line": 1
                },
                "AnycastOutPackRelation": {
                    "ForwardRulesLimit": 1,
                    "AutoRenewFlag": 1,
                    "CurDeadline": "xx",
                    "NormalBandwidth": 1
                },
                "Name": "xx",
                "Region": {
                    "Region": "xx"
                },
                "DamDDoSStatus": 1,
                "EipFlag": 1,
                "PackInfo": {
                    "PackId": "xx",
                    "PackType": "xx"
                },
                "EipAddressStatus": "xx",
                "Domain": "xx",
                "Tgw": 1,
                "InstanceDetail": {
                    "InstanceId": "xx",
                    "EipList": [
                        "1.1.1.1"
                    ]
                },
                "V6Flag": 1,
                "BGPIPChannelFlag": 1,
                "InstanceVersion": 1,
                "ZoneId": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

