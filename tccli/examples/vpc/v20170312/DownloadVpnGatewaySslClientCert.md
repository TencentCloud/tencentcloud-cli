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
        "SslClientConfig": [
            {
                "SslVpnCert": "-----BEGIN CERTIFICATE-----......",
                "SslVpnKey": "-----BEGIN PRIVATE KEY-----......",
                "SslVpnRootCert": "-----BEGIN CERTIFICATE-----......",
                "SslVpnClientConfiguration": "client\ndev tun\nproto udp\nremote......"
            }
        ],
        "Authenticated": 1,
        "RequestId": "d3c01d8b-0363-41d4-a8be-3cfcf2c69711",
        "SslClientConfigsSet": "${SslClientConfigsSet}"
    }
}
```

