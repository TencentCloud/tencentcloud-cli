**Example 1: 查询专用集群支持的可用区列表**



Input: 

```
tccli cdc DescribeDedicatedSupportedZones --cli-unfold-argument  \
    --Regions 4
```

Output: 
```
{
    "Response": {
        "RequestId": "932b1bb8-8b29-405a-a4f9-1a46213c05f6",
        "ZoneSet": [
            {
                "RegionId": 4,
                "Zones": [
                    {
                        "Zone": "ap-shanghai-1",
                        "ZoneId": 200001,
                        "ZoneName": "上海一区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-2",
                        "ZoneId": 200002,
                        "ZoneName": "上海二区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-3",
                        "ZoneId": 200003,
                        "ZoneName": "上海三区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-4",
                        "ZoneId": 200004,
                        "ZoneName": "上海四区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-5",
                        "ZoneId": 200005,
                        "ZoneName": "上海五区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-6",
                        "ZoneId": 200006,
                        "ZoneName": "上海六区",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-shanghai-7",
                        "ZoneId": 200007,
                        "ZoneName": "上海七区",
                        "ZoneState": "AVAILABLE"
                    }
                ]
            }
        ]
    }
}
```

