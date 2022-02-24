**Example 1: 查询SSL-VPN-SERVER**



Input: 

```
tccli vpc DescribeVpnGatewaySslServers --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpn-gateway-id \
    --Filters.0.Values vpn-123456
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "a5852809-b825-4e56-a52a-db8daeb8833c",
        "SslVpnSeverSet": [
            {
                "VpcId": "vpc-j522iytf",
                "VpnGatewayId": "vpngw-aw2tu307",
                "SslVpnServerName": "SERVER-004",
                "LocalAddress": "172.16.0.0/16",
                "RemoteAddress": "192.168.0.0/16",
                "MaxConnection": 5,
                "WanIp": "42.193.56.85",
                "SslVpnProtocol": "UDP",
                "SslVpnPort": 1194,
                "EncryptAlgorithm": "AES-128-CBC",
                "IntegrityAlgorithm": "SHA1",
                "Compress": 0,
                "CreateTime": "2021-07-13 11:25:57",
                "State": 6
            }
        ]
    }
}
```

