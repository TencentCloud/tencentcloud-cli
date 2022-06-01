**Example 1: 修改应用代理**



Input: 

```
tccli teo ModifyApplicationProxy --cli-unfold-argument  \
    --ZoneId zone-id123 \
    --ProxyId proxy-id123 \
    --ProxyName 123.123.com \
    --ProxyType hostname \
    --ForwardClientIp  \
    --SessionPersist False \
    --SessionPersistTime 3600
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "ProxyId": "proxy-xxx"
    }
}
```

