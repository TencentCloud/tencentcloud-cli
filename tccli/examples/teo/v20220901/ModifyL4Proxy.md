**Example 1: 修改 IPv6 访问配置**

将 ZoneId 为 zone-24wjy25v1cwi 下 ProxyId 为 sid-2qwk27xf7j9g 的四层代理实例的 IPv6 访问配置调整为开启。

Input: 

```
tccli teo ModifyL4Proxy --cli-unfold-argument  \
    --ZoneId zone-24wjy25v1cwi \
    --ProxyId sid-2qwk27xf7j9g \
    --Ipv6 on
```

Output: 
```
{
    "Response": {
        "RequestId": "fbdb42f0-6a1e-4d397783c36csdf"
    }
}
```

