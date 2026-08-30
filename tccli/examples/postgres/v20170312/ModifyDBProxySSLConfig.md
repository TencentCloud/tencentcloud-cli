**Example 1: 开启代理 SSL**

为指定代理连接地址开启 SSL，需传入与代理地址 Vip 一致的 ConnectAddress

Input: 

```
tccli postgres ModifyDBProxySSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx \
    --ProxyGroupId proxygrp-xxxxxxxx \
    --ProxyAddressId proxyaddr-xxxxxxxx \
    --SSLEnabled True \
    --ConnectAddress 10.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c",
        "TaskId": "12"
    }
}
```

**Example 2: 关闭代理 SSL**

关闭指定代理连接地址的 SSL，无需传 ConnectAddress

Input: 

```
tccli postgres ModifyDBProxySSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx \
    --ProxyGroupId proxygrp-xxxxxxxx \
    --ProxyAddressId proxyaddr-xxxxxxxx \
    --SSLEnabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c",
        "TaskId": "13"
    }
}
```

