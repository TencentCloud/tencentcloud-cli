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
        "RequestId": "aeabeab6-f74b-453a-b25d-d7b460193c3b",
        "TaskId": 123
    }
}
```

