**Example 1: 创建SSL-VPN-SERVER**

创建SSL-VPN-SERVER

Input: 

```
tccli vpc CreateVpnGatewaySslServer --cli-unfold-argument  \
    --RemoteAddress 172.0.0.0/16 \
    --LocalAddress 10.0.0.0/16 \
    --VpnGatewayId vpngw-awd2451x \
    --SslVpnServerName test
```

Output: 
```
{
    "Response": {
        "SslVpnServerId": "vpns-cik6bjct",
        "TaskId": 12233,
        "RequestId": "b0ef44b0-410a-400f-8aa2-a8abedb26b3a"
    }
}
```

