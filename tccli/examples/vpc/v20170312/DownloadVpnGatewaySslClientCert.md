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
        "RequestId": "aeabeab6-f74b-453a-b25d-d7b460193c3b",
        "SslClientConfigsSet": "xxx"
    }
}
```

