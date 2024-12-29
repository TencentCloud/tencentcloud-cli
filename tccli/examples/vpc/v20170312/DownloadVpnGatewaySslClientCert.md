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
        "SslClientConfigsSet": "{\"SslVpnClientConfiguration\": \"-config-\"......}",
        "SslClientConfig": [
            {
                "SslVpnClientConfiguration": "config...",
                "SslVpnRootCert": "CERTIFICATE...",
                "SslVpnKey": "PRIVATE KEY...",
                "SslVpnCert": "CERTIFICATE...",
                "SslVpnClientId": "vpnc-axa315c"
            }
        ],
        "Authenticated": 1,
        "RequestId": "8e08f027-048b-41e8-ac99-77e954ca15c5"
    }
}
```

