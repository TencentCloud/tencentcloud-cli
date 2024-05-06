**Example 1: 查询SSL-VPN-SERVER**

查询SSL-VPN-SERVER

Input: 

```
tccli vpc DescribeVpnGatewaySslServers --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpn-gateway-id \
    --Filters.0.Values vpngw-0zowp2z9
```

Output: 
```
{
    "Response": {
        "RequestId": "1d0c0675-d1cb-4d28-99af-bf093a7d62d2",
        "SslVpnSeverSet": [
            {
                "VpcId": "vpc-1tqv6my1",
                "SslVpnServerId": "vpns-fofx7shn",
                "VpnGatewayId": "vpngw-0zowp2z9",
                "SslVpnServerName": "test",
                "LocalAddress": [
                    "10.17.0.0/24"
                ],
                "RemoteAddress": "10.12.0.0/24",
                "MaxConnection": 5,
                "WanIp": "1.14.55.188",
                "SslVpnProtocol": "UDP",
                "SslVpnPort": 1194,
                "EncryptAlgorithm": "none",
                "IntegrityAlgorithm": "none",
                "Compress": 0,
                "CreateTime": "2023-01-11 11:37:41",
                "State": 6,
                "SsoEnabled": 0,
                "SpName": "",
                "EiamApplicationId": "",
                "AccessPolicyEnabled": 0,
                "AccessPolicy": []
            }
        ],
        "TotalCount": 1
    }
}
```

