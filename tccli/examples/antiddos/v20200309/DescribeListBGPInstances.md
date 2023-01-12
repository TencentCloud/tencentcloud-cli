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
        "InstanceList": [
            {
                "BoundStatus": "idle",
                "CCEnable": 0,
                "CreatedTime": "2022-12-08 18:55:54",
                "DDoSLevel": "high",
                "EipProductInfos": [],
                "ElasticServiceBandwidth": 0,
                "ExpiredTime": "2023-12-08 18:55:54",
                "InstanceDetail": {
                    "EipList": [],
                    "InstanceId": "bgp-00000001"
                },
                "IpCountNewFlag": 0,
                "Line": 1,
                "Name": "zbhh",
                "PackInfo": {
                    "PackId": "zbhh-00000001",
                    "PackType": "zbhh"
                },
                "Region": {
                    "Region": "ap-hongkong"
                },
                "SpecificationLimit": {
                    "AutoRenewFlag": 0,
                    "BattleEditionFlag": 0,
                    "ChannelEditionFlag": 0,
                    "ElasticLimit": 0,
                    "EnterpriseFlag": 1,
                    "ProtectBandwidth": 560000,
                    "ProtectCountLimit": 999999999,
                    "ProtectIPNumberLimit": 10,
                    "ServiceBandWidth": 150,
                    "UnionPackFlag": 0
                },
                "Status": "idle",
                "TagInfoList": [
                    {
                        "TagKey": "xxx",
                        "TagValue": "test"
                    }
                ],
                "Usage": {
                    "Last7DayAttackCount": 0,
                    "ProtectCountUsage": 999999999,
                    "ProtectIPNumberUsage": 0
                },
                "VitalityVersion": 0
            }
        ],
        "RequestId": "0381c271-292d-4e2a-adcc-cd7bcd6977a7",
        "Total": 53
    }
}
```

