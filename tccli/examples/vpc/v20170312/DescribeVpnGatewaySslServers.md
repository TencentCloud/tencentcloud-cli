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
        "SslVpnSeverSet": [
            {
                "SslVpnProtocol": "xx",
                "SsoEnabled": 1,
                "VpcId": "xx",
                "IntegrityAlgorithm": "xx",
                "RemoteAddress": "xx",
                "EncryptAlgorithm": "xx",
                "Compress": 1,
                "LocalAddress": [
                    "xx"
                ],
                "AccessPolicy": [
                    {
                        "UserGroupIds": [
                            "xx"
                        ],
                        "VpnGatewayIdSslAccessPolicyId": "xx",
                        "UpdateTime": "xx",
                        "TargetCidr": "xx",
                        "ForAllClient": 1
                    }
                ],
                "State": 1,
                "MaxConnection": 1,
                "EiamApplicationId": "xx",
                "VpnGatewayId": "xx",
                "SslVpnServerId": "xx",
                "WanIp": "xx",
                "AccessPolicyEnabled": 1,
                "SslVpnServerName": "xx",
                "CreateTime": "xx",
                "SslVpnPort": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

