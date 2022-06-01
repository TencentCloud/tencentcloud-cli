**Example 1: 创建应用代理规则**



Input: 

```
tccli teo CreateApplicationProxyRule --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --Proto TCP \
    --Port 80 90 99-110 \
    --OriginType custom \
    --OriginValue 1.1.1.1:80 \
    --ForwardClientIp TOA \
    --SessionPersist False
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RuleId": "rule-xxx"
    }
}
```

