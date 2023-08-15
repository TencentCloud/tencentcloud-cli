**Example 1: 查询应用代理列表**



Input: 

```
tccli teo DescribeApplicationProxies --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "a84ae15a-aca5-4c24-a4f4-c419cf2c18af",
        "ApplicationProxies": [
            {
                "HostId": "",
                "ProxyType": "instance",
                "Area": "mainland",
                "AccelerateType": 1,
                "SessionPersistTime": 100,
                "PlatType": "domain",
                "ProxyId": "proxy-34c74aa7-9a9f-11ec-bcb0-52540015711d",
                "ProxyName": "zone-f835533b8998f",
                "ZoneId": "zone-21xfqlh4qjee",
                "ZoneName": "123.com",
                "ApplicationProxyRules": [
                    {
                        "OriginType": "custom",
                        "OriginValue": [
                            "81.69.174.153:80"
                        ],
                        "Port": [
                            "80"
                        ],
                        "OriginPort": "8080",
                        "SessionPersistTime": 100,
                        "Proto": "TCP",
                        "Status": "online",
                        "ForwardClientIp": "off",
                        "SessionPersist": true,
                        "RuleId": "rule-34c74ab8-9a9f-11ec-bcb0-52540015711d",
                        "RuleTag": "rule-for-cgi"
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
                        "OriginPort": "8080",
                        "SessionPersistTime": 100,
                        "RuleId": "rule-4bc1d3d6-9aa0-11ec-bcb0-52540015711d",
                        "RuleTag": "rule-for-logic"
                    }
                ],
                "AccelerateMainland": {
                    "Switch": "off"
                },
                "ScheduleValue": [],
                "SecurityType": 1,
                "Ipv6": {
                    "Switch": "on"
                },
                "Status": "progress",
                "BanStatus": "recover",
                "UpdateTime": "2022-03-03T06:06:10Z"
            }
        ],
        "TotalCount": 1
    }
}
```

