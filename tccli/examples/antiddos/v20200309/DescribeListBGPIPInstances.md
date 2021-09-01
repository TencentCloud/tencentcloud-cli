**Example 1: 获取高防IP资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPIPInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-00000001 \
    --FilterLine 1 \
    --FilterRegion ap-guangzhou \
    --FilterName test \
    --FilterEipType 1 \
    --FilterEipEipAddressStatus BIND BINDING
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "InstanceList": [
            {
                "Status": "xx",
                "EipAddressStatus": "xx",
                "Name": "xx",
                "StaticPackRelation": {
                    "ForwardRulesLimit": 1,
                    "AutoRenewFlag": 1,
                    "ProtectBandwidth": 1,
                    "CurDeadline": "xx",
                    "NormalBandwidth": 1
                },
                "Region": {
                    "Region": "xx"
                },
                "EipAddressPackRelation": {
                    "AutoRenewFlag": 1,
                    "CurDeadline": "2020-09-22 00:00:00",
                    "IpCount": 1
                },
                "EipFlag": 1,
                "InstanceDetail": {
                    "InstanceId": "xx",
                    "EipList": [
                        "1.1.1.1"
                    ]
                },
                "CreatedTime": "2020-09-22 00:00:00",
                "ExpiredTime": "2020-09-22 00:00:00",
                "EipAddressInfo": {
                    "EipBoundRscIns": "xx",
                    "EipBoundRscVip": "xx",
                    "EipBoundRscEni": "xx",
                    "EipAddressRegion": "xx"
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
                "Usage": {
                    "PortRulesUsage": 1,
                    "DomainRulesUsage": 1,
                    "Last7DayAttackCount": 1
                },
                "PackInfo": {
                    "PackId": "xx",
                    "PackType": "xx"
                },
                "ZoneId": 1,
                "Tgw": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

