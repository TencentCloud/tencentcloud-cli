**Example 1: 创建SSL-VPN-CLIENT**

创建SSL-VPN-CLIENT

Input: 

```
tccli vpc CreateVpnGatewaySslClient --cli-unfold-argument  \
    --SslVpnServerId vpns-5au854w1 \
    --SslVpnClientName test
```

Output: 
```
{
    "Response": {
        "SslVpnClientId": "vpnc-f5yln4n3",
        "RequestId": "13322b62-5943-41c9-4a1c-4bff13f56aeb",
        "TaskId": 1
    }
}
```

