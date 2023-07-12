**Example 1: 修改应用代理规则**

修改应用代理规则

Input: 

```
tccli teo ModifyApplicationProxyRule --cli-unfold-argument  \
    --ZoneId zone-276zs184g93m \
    --ProxyId proxy-19389e5dwwxfs \
    --RuleId rule-5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707 \
    --Proto TCP \
    --Port 99-110 \
    --OriginType custom \
    --OriginValue 1.1.1.1 \
    --OriginPort 99-110 \
    --ForwardClientIp TOA \
    --SessionPersist False
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

