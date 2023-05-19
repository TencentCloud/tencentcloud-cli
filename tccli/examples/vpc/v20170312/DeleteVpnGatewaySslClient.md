**Example 1: 删除SSL-VPN-CLIENT**

删除SSL-VPN-CLIENT

Input: 

```
tccli vpc DeleteVpnGatewaySslClient --cli-unfold-argument  \
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

