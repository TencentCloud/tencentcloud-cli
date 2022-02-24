**Example 1: 创建SSL-VPN-SERVER**



Input: 

```
tccli vpc CreateVpnGatewaySslServer --cli-unfold-argument  \
    --SslVpnProtocol xx \
    --IntegrityAlgorithm xx \
    --RemoteAddress xx \
    --EncryptAlgorithm xx \
    --Compress True \
    --LocalAddress xx \
    --VpnGatewayId xx \
    --SslVpnServerName xx \
    --SslVpnPort 0
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

