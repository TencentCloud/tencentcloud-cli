**Example 1: 下载SSL-VPN-CLIENT配置**



Input: 

```
tccli vpc DownloadVpnGatewaySslClientCert --cli-unfold-argument  \
    --SslVpnClientId vpnc--84tby4k2
```

Output: 
```
{
    "Response": {
        "SslClientConfig": [
            {
                "SslVpnCert": "xx",
                "SslVpnKey": "xx",
                "SslVpnRootCert": "xx",
                "SslVpnClientConfiguration": "xx"
            }
        ],
        "Authenticated": 1,
        "RequestId": "xx",
        "SslClientConfigsSet": "xx"
    }
}
```

