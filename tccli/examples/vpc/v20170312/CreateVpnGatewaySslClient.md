**Example 1: 创建SSL-VPN-CLIENT**



Input: 

```
tccli vpc CreateVpnGatewaySslClient --cli-unfold-argument  \
    --SslVpnServerId vpns-xxxx \
    --SslVpnClientName test
```

Output: 
```
{
    "Response": {
        "SslVpnClientId": "xx",
        "RequestId": "xx",
        "TaskId": 1
    }
}
```

