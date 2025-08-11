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
                "StandbyZoneSet": null,
                "Zone": "ap-guangzhou-1",
                "ZoneId": 100001,
                "ZoneName": "广州一区",
                "ZoneState": "UNAVAILABLE",
                "ZoneSupportIpv6": 0
            },
            {
                "StandbyZoneSet": [
                    "ap-guangzhou-4",
                    "ap-guangzhou-6",
                    "ap-guangzhou-7"
                ],
                "Zone": "ap-guangzhou-7",
                "ZoneId": 100007,
                "ZoneName": "广州七区",
                "ZoneState": "AVAILABLE",
                "ZoneSupportIpv6": 0
            },
            {
                "StandbyZoneSet": [
                    "ap-guangzhou-4",
                    "ap-guangzhou-6",
                    "ap-guangzhou-7"
                ],
                "Zone": "ap-guangzhou-4",
                "ZoneId": 100004,
                "ZoneName": "广州四区",
                "ZoneState": "AVAILABLE",
                "ZoneSupportIpv6": 0
            }
        ]
    }
}
```

