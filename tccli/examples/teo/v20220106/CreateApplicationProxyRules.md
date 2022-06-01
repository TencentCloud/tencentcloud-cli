**Example 1: 批量创建应用代理规则**



Input: 

```
tccli teo CreateApplicationProxyRules --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --Rule.0.Proto TCP \
    --Rule.0.Port 80 90 99-110 \
    --Rule.0.OriginType custom \
    --Rule.0.OriginValue 1.1.1.1:80 \
    --Rule.0.ForwardClientIp TOA \
    --Rule.0.SessionPersist False
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RuleId": [
            "rule-xxx"
        ]
    }
}
```

