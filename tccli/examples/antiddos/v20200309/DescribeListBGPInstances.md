**Example 1: 获取高防包资产实例列表**

获取高防包资产实例列表

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
        "Total": 1,
        "InstanceList": [
            {
                "InstanceDetail": {
                    "EipList": [
                        "abc"
                    ],
                    "InstanceId": "abc"
                },
                "SpecificationLimit": {
                    "ProtectBandwidth": 1,
                    "ProtectCountLimit": 1,
                    "ProtectIPNumberLimit": 1,
                    "AutoRenewFlag": 1,
                    "UnionPackFlag": 1,
                    "ServiceBandWidth": 1,
                    "BattleEditionFlag": 1,
                    "ChannelEditionFlag": 1,
                    "EnterpriseFlag": 1,
                    "ElasticLimit": 1,
                    "DownGradeProtect": 1
                },
                "Usage": {
                    "ProtectCountUsage": 1,
                    "ProtectIPNumberUsage": 1,
                    "Last7DayAttackCount": 1
                },
                "Region": {
                    "Region": "abc"
                },
                "Status": "abc",
                "CreatedTime": "2020-09-22 00:00:00",
                "ExpiredTime": "2020-09-22 00:00:00",
                "Name": "abc",
                "PackInfo": {
                    "PackType": "abc",
                    "PackId": "abc"
                },
                "EipProductInfos": [
                    {
                        "Ip": "abc",
                        "BizType": "abc",
                        "DeviceType": "abc",
                        "InstanceId": "abc",
                        "Domain": "abc"
                    }
                ],
                "BoundStatus": "abc",
                "DDoSLevel": "abc",
                "CCEnable": 0,
                "TagInfoList": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "IpCountNewFlag": 1,
                "VitalityVersion": 1,
                "Line": 1,
                "FreeServiceBandwidth": 1,
                "ElasticServiceBandwidth": 1,
                "GiftServiceBandWidth": 0,
                "ModifyTime": "abc",
                "BasicPlusFlag": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

