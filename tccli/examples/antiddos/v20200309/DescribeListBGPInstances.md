**Example 1: 获取高防包资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPInstances --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --FilterInstanceId bgp-00000001 \
    --FilterIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "Total": 20,
        "RequestId": "0381c271-292d-4e2a-adcc-cd7bcd6977a7",
        "InstanceList": [
            {
                "InstanceDetail": {
                    "EipList": [
                        "1.1.1.1"
                    ],
                    "InstanceId": "bgp-00000001"
                },
                "SpecificationLimit": {
                    "ProtectBandwidth": 560000,
                    "ProtectCountLimit": 999999999,
                    "ProtectIPNumberLimit": 10,
                    "AutoRenewFlag": 0,
                    "ServiceBandWidth": 150,
                    "UnionPackFlag": 0,
                    "BattleEditionFlag": 0,
                    "ChannelEditionFlag": 0,
                    "EnterpriseFlag": 1,
                    "ElasticLimit": 0
                },
                "Usage": {
                    "ProtectCountUsage": 999999999,
                    "ProtectIPNumberUsage": 1,
                    "Last7DayAttackCount": 1
                },
                "Region": {
                    "Region": "ap-hongkong"
                },
                "PackInfo": {
                    "PackType": "zbhh",
                    "PackId": "zbhh-00000001"
                },
                "Name": "zbhh",
                "Status": "idle",
                "BoundStatus": "idle",
                "ExpiredTime": "2023-12-08 18:55:54",
                "CreatedTime": "2022-12-08 18:55:54",
                "IpCountNewFlag": 0,
                "VitalityVersion": 0,
                "DDoSLevel": "high",
                "CCEnable": 1,
                "EipProductInfos": [
                    {
                        "Ip": "1.1.1.1",
                        "BizType": "public",
                        "DeviceType": "eip",
                        "InstanceId": "eip-00000001"
                    }
                ],
                "TagInfoList": [
                    {
                        "TagKey": "test1",
                        "TagValue": "test"
                    }
                ]
            }
        ]
    }
}
```

