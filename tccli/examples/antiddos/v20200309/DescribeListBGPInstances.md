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
                        "1.1.1.1"
                    ],
                    "InstanceId": "id-xxx"
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
                    "Region": "guangzhou"
                },
                "Status": "1",
                "CreatedTime": "2020-09-22 00:00:00",
                "ExpiredTime": "2020-09-22 00:00:00",
                "Name": "name",
                "PackInfo": {
                    "PackType": "type",
                    "PackId": "id"
                },
                "EipProductInfos": [
                    {
                        "Ip": "1.1.1.1",
                        "BizType": "eip",
                        "DeviceType": "eip",
                        "InstanceId": "ins-xx",
                        "Domain": "www.abc.com"
                    }
                ],
                "BoundStatus": "creat",
                "DDoSLevel": "1",
                "CCEnable": 0,
                "TagInfoList": [
                    {
                        "TagKey": "key",
                        "TagValue": "value"
                    }
                ],
                "IpCountNewFlag": 1,
                "VitalityVersion": 1,
                "Line": 1,
                "FreeServiceBandwidth": 1,
                "ElasticServiceBandwidth": 1,
                "GiftServiceBandWidth": 0,
                "ModifyTime": "2024.12.1",
                "BasicPlusFlag": 1
            }
        ],
        "RequestId": "08afbb87-5a2c-4562-acbd-eef06a47c7db"
    }
}
```

