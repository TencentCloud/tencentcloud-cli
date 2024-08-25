**Example 1: 下载SSL-VPN-CLIENT配置**

下载SSL-VPN-CLIENT配置

Input: 

```
tccli vpc DownloadVpnGatewaySslClientCert --cli-unfold-argument  \
    --SslVpnClientId vpnc--84tby4k2
```

Output: 
```
{
    "Response": {
        "SslClientConfigsSet": "abc",
        "SslClientConfig": [
            {
                "SslVpnClientConfiguration": "abc",
                "SslVpnRootCert": "abc",
                "SslVpnKey": "abc",
                "SslVpnCert": "abc",
                "SslVpnClientId": "abc"
            }
        ],
        "Authenticated": 1,
        "RequestId": "abc"
    }
}
```

