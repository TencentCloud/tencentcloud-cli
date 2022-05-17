**Example 1: 查询专用集群支持的可用区列表**



Input: 

```
tccli cdc DescribeDedicatedSupportedZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "RegionId": 1,
                "Zones": [
                    {
                        "Zone": "ap-guangzhou-1",
                        "ZoneName": "广州一区",
                        "ZoneId": "100001",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-guangzhou-2",
                        "ZoneName": "广州二区",
                        "ZoneId": "100002",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-guangzhou-3",
                        "ZoneName": "广州三区",
                        "ZoneId": "100003",
                        "ZoneState": "AVAILABLE"
                    },
                    {
                        "Zone": "ap-guangzhou-4",
                        "ZoneName": "广州四区",
                        "ZoneId": "100004",
                        "ZoneState": "AVAILABLE"
                    }
                ]
            }
        ],
        "RequestId": "e3d77a1b-dc45-49b0-a9ee-2e97807b8f8e"
    }
}
```

