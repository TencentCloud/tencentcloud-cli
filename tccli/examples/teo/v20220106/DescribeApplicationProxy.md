**Example 1: 获取应用代理列表**



Input: 

```
tccli teo DescribeApplicationProxy --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ZoneId zone-21xfqlh4qjee
```

Output: 
```
{
    "Response": {
        "RequestId": "a84ae15a-aca5-4c24-a4f4-c419cf2c18af",
        "Data": [
            {
                "HostId": "",
                "ProxyType": "instance",
                "ForwardClientIp": "OFF",
                "SessionPersistTime": 1,
                "AccelerateType": 1,
                "PlatType": "domain",
                "ProxyId": "proxy-34c74aa7-9a9f-11ec-bcb0-52540015711d",
                "ProxyName": "zone-f835533b8998f",
                "ZoneId": "zone-21xfqlh4qjee",
                "ZoneName": "123.com",
                "Rule": [
                    {
                        "OriginType": "custom",
                        "OriginValue": [
                            "81.69.174.153:80"
                        ],
                        "Port": [
                            "80"
                        ],
                        "Proto": "TCP",
                        "Status": "online",
                        "ForwardClientIp": "off",
                        "SessionPersist": true,
                        "RuleId": "rule-34c74ab8-9a9f-11ec-bcb0-52540015711d"
                    },
                    {
                        "OriginType": "custom",
                        "OriginValue": [
                            "81.69.174.153:553"
                        ],
                        "Port": [
                            "553"
                        ],
                        "Proto": "UDP",
                        "Status": "online",
                        "ForwardClientIp": "off",
                        "SessionPersist": true,
                        "RuleId": "rule-4bc1d3d6-9aa0-11ec-bcb0-52540015711d"
                    }
                ],
                "ScheduleValue": [],
                "SecurityType": 1,
                "Ipv6": {
                    "Switch": "on"
                },
                "SessionPersist": false,
                "Status": "progress",
                "UpdateTime": "2022-03-03T06:06:10Z"
            }
        ],
        "TotalCount": 1,
        "IpCount": 1,
        "DomainCount": 1,
        "Quota": 0
    }
}
```

