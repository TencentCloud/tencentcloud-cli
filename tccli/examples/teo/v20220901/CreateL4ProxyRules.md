**Example 1: 创建四层代理转发规则**

在 ZoneId 为 zone-24wjy25v1cwi 下 ProxyId 为 sid-2qwk27xf7j9g 的实例中创建一条转发规则。

Input: 

```
tccli teo CreateL4ProxyRules --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --L4ProxyRules.0.Protocol TCP \
    --L4ProxyRules.0.PortRange 80 \
    --L4ProxyRules.0.OriginType IP_DOMAIN \
    --L4ProxyRules.0.OriginValue 119.23.100.45 \
    --L4ProxyRules.0.OriginPortRange 90 \
    --L4ProxyRules.0.ClientIPPassThroughMode TOA \
    --L4ProxyRules.0.SessionPersist on \
    --L4ProxyRules.0.SessionPersistTime 3600 \
    --L4ProxyRules.0.RuleTag test
```

Output: 
```
{
    "Response": {
        "RequestId": "6f8h5358-df6d-4d2a-ac39-1706cbf8a707",
        "L4ProxyRuleIds": [
            "rule-2qzkbvx3hxl1"
        ]
    }
}
```

