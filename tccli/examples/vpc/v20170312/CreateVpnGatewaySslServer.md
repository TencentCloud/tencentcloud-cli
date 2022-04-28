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
        "SslVpnServerId": "xx",
        "TaskId": 123,
        "RequestId": "xx"
    }
}
```

