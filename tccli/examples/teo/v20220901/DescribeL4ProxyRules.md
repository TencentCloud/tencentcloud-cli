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
                    "test.origin.com"
                ],
                "OriginPortRange": "90",
                "ClientIPPassThroughMode": "TOA",
                "SessionPersist": "on",
                "SessionPersistTime": 3600,
                "RuleTag": "origin",
                "Status": "online"
            }
        ],
        "RequestId": "6f8h5358-cdda-4f82-b7sc-0aef4a219244"
    }
}
```

**Example 2: 查询指定转发规则 ID 下的四层代理实例转发规则列表**

查询 Zoneld 为 zone-2zzj3cyeonyy 下 Proxyld 为 sid-33ik2zqsvcqq，指定转发规则ID为 rule-33ik84rw3nuu 下的转发规则列表。

Input: 

```
tccli teo DescribeL4ProxyRules --cli-unfold-argument  \
    --ZoneId zone-2zzj3cyeonyy \
    --ProxyId sid-33ik2zqsvcqq \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name rule-id \
    --Filters.0.Values rule-33ik84rw3nuu
```

Output: 
```
{
    "Response": {
        "L4ProxyRules": [
            {
                "ClientIPPassThroughMode": "TOA",
                "OriginPortRange": "20",
                "OriginType": "IP_DOMAIN",
                "OriginValue": [
                    "test.origin.com"
                ],
                "PortRange": [
                    "10"
                ],
                "Protocol": "TCP",
                "RemoteAuth": {
                    "Address": "",
                    "ServerFaultyBehavior": "allow",
                    "Switch": "off"
                },
                "RuleId": "rule-33ik84rw3nuu",
                "RuleTag": "tag",
                "SessionPersist": "on",
                "SessionPersistTime": 2000,
                "Status": "online"
            }
        ],
        "RequestId": "7bea447f-ec2f-41d2-bd49-5dc566359777",
        "TotalCount": 1
    }
}
```

