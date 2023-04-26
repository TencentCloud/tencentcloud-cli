**Example 1: 创建应用代理**

创建应用代理。

Input: 

```
tccli teo CreateApplicationProxy --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ProxyName instancd-name \
    --ProxyType instance \
    --PlatType ip \
    --SecurityType 1 \
    --AccelerateType 1 \
    --SessionPersistTime 3600 \
    --Ipv6.Switch on \
    --ApplicationProxyRules.0.Proto TCP \
    --ApplicationProxyRules.0.Port 80 90 99-110 \
    --ApplicationProxyRules.0.OriginType custom \
    --ApplicationProxyRules.0.OriginValue 1.1.1.1:80 \
    --ApplicationProxyRules.1.Proto UDP \
    --ApplicationProxyRules.1.Port 999 888 99-110 \
    --ApplicationProxyRules.1.OriginType custom \
    --ApplicationProxyRules.1.OriginValue 1.1.1.1:80 2.2.2.2:80
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

