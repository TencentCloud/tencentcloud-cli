**Example 1: 获取高防包资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPInstances --cli-unfold-argument  \
    --FilterRegion ap-guangzhou \
    --FilterName test \
    --Limit 25 \
    --Offset 0 \
    --FilterInstanceId bgp-00000001 \
    --FilterIp 1.1.1.1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "InstanceList": [
            {
                "Status": "xx",
                "EipProductInfos": [
                    {
                        "BizType": "xx",
                        "Ip": "xx",
                        "InstanceId": "xx",
                        "DeviceType": "xx"
                    }
                ],
                "Name": "xx",
                "CCEnable": 1,
                "Region": {
                    "Region": "xx"
                },
                "InstanceDetail": {
                    "InstanceId": "xx",
                    "EipList": [
                        "1.1.1.1"
                    ]
                },
                "CreatedTime": "2020-09-22 00:00:00",
                "ExpiredTime": "2020-09-22 00:00:00",
                "VitalityVersion": 1,
                "IpCountNewFlag": 1,
                "TagInfoList": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "Usage": {
                    "ProtectCountUsage": 1,
                    "ProtectIPNumberUsage": 1,
                    "Last7DayAttackCount": 1
                },
                "DDoSLevel": "xx",
                "PackInfo": {
                    "PackId": "xx",
                    "PackType": "xx"
                },
                "SpecificationLimit": {
                    "EnterpriseFlag": 1,
                    "ElasticLimit": 1,
                    "BattleEditionFlag": 1,
                    "ServiceBandWidth": 1,
                    "AutoRenewFlag": 1,
                    "ProtectBandwidth": 1,
                    "ProtectCountLimit": 1,
                    "UnionPackFlag": 1,
                    "ChannelEditionFlag": 1,
                    "ProtectIPNumberLimit": 1
                },
                "BoundStatus": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

