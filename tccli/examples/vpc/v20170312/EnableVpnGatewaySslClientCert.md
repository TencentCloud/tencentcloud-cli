**Example 1: 启用SSL-VPN-CLIENT证书**

启用SSL-VPN-CLIENT证书

Input: 

```
tccli vpc EnableVpnGatewaySslClientCert --cli-unfold-argument  \
    --SslVpnClientId vpnc-xxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "aeabeab6-f74b-453a-b25d-d7b460193c3b",
        "TaskId": 123
    }
}
```

