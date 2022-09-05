**Example 1: 获取应用代理详细信息**



Input: 

```
tccli teo DescribeApplicationProxyDetail --cli-unfold-argument  \
    --ProxyId proxy-f11f7ab4-1632-11ed-9fe6-52540033158e \
    --ZoneId zone-24j9wpas4c62
```

Output: 
```
{
    "Response": {
        "RequestId": "c7870673-3982-4636-a721-c00e54f81d19",
        "AccelerateType": 1,
        "ForwardClientIp": "OFF",
        "HostId": "edgeone-24j9wpas4c62",
        "Ipv6": {
            "Switch": "on"
        },
        "Area": "overseas",
        "PlatType": "domain",
        "ProxyId": "proxy-f11f7ab4-1632-11ed-9fe6-52540033158e",
        "ProxyName": "test-ipv6-l4",
        "ProxyType": "instance",
        "Rule": [
            {
                "ForwardClientIp": "OFF",
                "OriginType": "origins",
                "OriginValue": [
                    "origin-537f5b41-162a-11ed-abaa-525400c5da15"
                ],
                "Port": [
                    "88"
                ],
                "Proto": "TCP",
                "RuleId": "rule-f11f7ac4-1632-11ed-9fe6-52540033158e",
                "SessionPersist": false,
                "Status": "online"
            }
        ],
        "ScheduleValue": [],
        "SecurityType": 1,
        "SessionPersist": false,
        "SessionPersistTime": 3600,
        "Status": "progress",
        "UpdateTime": "2022-08-10T04:38:03Z",
        "ZoneId": "zone-24j9wpas4c62",
        "ZoneName": "test.com"
    }
}
```

