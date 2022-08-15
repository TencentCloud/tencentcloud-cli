**Example 1: 创建应用代理**



Input: 

```
tccli teo CreateApplicationProxy --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ZoneName test.com \
    --ProxyName instancd-name \
    --ProxyType instance \
    --PlatType ip \
    --SecurityType 1 \
    --AccelerateType 1 \
    --ForwardClientIp  \
    --SessionPersist False \
    --SessionPersistTime 3600 \
    --Ipv6.Switch on \
    --Rule.0.Proto TCP \
    --Rule.0.Port 80 90 99-110 \
    --Rule.0.OriginType custom \
    --Rule.0.OriginValue 1.1.1.1:80 \
    --Rule.1.Proto UDP \
    --Rule.1.Port 999 888 99-110 \
    --Rule.1.OriginType custom \
    --Rule.1.OriginValue 1.1.1.1:80 2.2.2.2:80
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "ProxyId": "proxy-537f5b41-162a-11ed-abaa-525400c5da15"
    }
}
```

