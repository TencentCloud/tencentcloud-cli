**Example 1: 查询特定地域下的可用区**



Input: 

```
tccli postgres DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "59c438d4-95ab-4865-993d-dc388d2660d8",
        "TotalCount": 3,
        "ZoneSet": [
            {
                "Zone": "ap-guangzhou-2",
                "ZoneName": "广州二区",
                "ZoneId": 100002,
                "ZoneState": "AVAILABLE",
                "ZoneSupportIpv6": 0,
                "StandbyZoneSet": [
                    "ap-guangzhou-2",
                    "ap-guangzhou-3"
                ]
            },
            {
                "Zone": "ap-guangzhou-3",
                "ZoneName": "广州三区",
                "ZoneId": 100003,
                "ZoneState": "AVAILABLE",
                "ZoneSupportIpv6": 0,
                "StandbyZoneSet": [
                    "ap-guangzhou-2",
                    "ap-guangzhou-3"
                ]
            },
            {
                "Zone": "ap-guangzhou-4",
                "ZoneName": "广州四区",
                "ZoneId": 100004,
                "ZoneState": "AVAILABLE",
                "ZoneSupportIpv6": 0,
                "StandbyZoneSet": [
                    "ap-guangzhou-4"
                ]
            }
        ]
    }
}
```

