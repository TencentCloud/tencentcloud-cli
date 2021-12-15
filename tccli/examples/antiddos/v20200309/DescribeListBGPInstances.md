**Example 1: 获取高防包资产实例列表**



Input: 

```
tccli antiddos DescribeListBGPInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgp-00000001 \
    --FilterRegion ap-guangzhou \
    --FilterName test
```

Output: 
```
{
    "Response": {
        "RequestId": "5d362f93-9a48-4194-995f-d3dd377c770d",
        "InstanceList": [
            {
                "InstanceDetail": {
                    "EipList": [
                        "1.1.1.1"
                    ],
                    "InstanceId": "bgp-00000001"
                },
                "PackInfo": {
                    "PackId": "",
                    "PackType": ""
                },
                "SpecificationLimit": {
                    "ProtectBandwidth": 20000,
                    "ProtectCountLimit": 0,
                    "ProtectIPNumberLimit": 5,
                    "AutoRenewFlag": 0
                },
                "Usage": {
                    "ProtectCountUsage": 0,
                    "ProtectIPNumberUsage": 0,
                    "Last7DayAttackCount": 0
                },
                "Region": {
                    "Region": "ap-guangzhou"
                },
                "Name": "123test",
                "DDoSLevel": "low",
                "CCEnable": 1,
                "Status": "idle",
                "ExpiredTime": "2020-04-11 14:28:55",
                "CreatedTime": "2020-03-11 14:28:55",
                "EipProductInfos": [
                    {
                        "Ip": "1.1.1.1",
                        "BizType": "public",
                        "DeviceType": "cvm",
                        "InstanceId": "ins-f2f9ssbo"
                    }
                ],
                "BoundStatus": "idle"
            }
        ],
        "Total": 1
    }
}
```

