**Example 1: 查询四层代理实例转发规则列表**

查询 Zoneld 为 zone-24wjy25v1cwi 下 Proxyld 为 sid-2qwk27xf7j9g 下的转发规则列表。

Input: 

```
tccli teo DescribeL4ProxyRules --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --Offset 1 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "L4ProxyRules": [
            {
                "RuleId": "rule-2qzkbvx3hxl1",
                "Protocol": "TCP",
                "PortRange": [
                    "80"
                ],
                "OriginType": "IP_DOMAIN",
                "OriginValue": [
                    "119.23.100.45"
                ],
                "OriginPortRange": "90",
                "ClientIPPassThroughMode": "TOA",
                "SessionPersist": "on",
                "SessionPersistTime": 3600,
                "RuleTag": "test",
                "Status": "online"
            }
        ],
        "RequestId": "6f8h5358-cdda-4f82-b7sc-0aef4a219244"
    }
}
```

