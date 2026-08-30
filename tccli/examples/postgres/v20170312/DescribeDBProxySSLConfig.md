**Example 1: 查询代理 SSL 配置**

查询代理 SSL 配置成功，返回 SSL 开启状态、连接地址及 CA 证书下载链接。

Input: 

```
tccli postgres DescribeDBProxySSLConfig --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx \
    --ProxyGroupId proxy-group-xxxxxxxx \
    --ProxyAddressId proxy-address-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "SSLEnabled": true,
        "ConnectAddress": "10.0.0.1",
        "CAUrl": "https://example.com/ca-cert.pem",
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c"
    }
}
```

