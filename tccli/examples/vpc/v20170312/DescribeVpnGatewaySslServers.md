**Example 1: 查询SSL-VPN-SERVER**

查询SSL-VPN-SERVER

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
                "VpcId": "abc",
                "SslVpnServerId": "abc",
                "VpnGatewayId": "abc",
                "SslVpnServerName": "abc",
                "LocalAddress": [
                    "abc"
                ],
                "RemoteAddress": "abc",
                "MaxConnection": 1,
                "WanIp": "abc",
                "SslVpnProtocol": "abc",
                "SslVpnPort": 1,
                "EncryptAlgorithm": "abc",
                "IntegrityAlgorithm": "abc",
                "Compress": 1,
                "CreateTime": "abc",
                "State": 1,
                "SsoEnabled": 1,
                "EiamApplicationId": "abc",
                "AccessPolicyEnabled": 1,
                "AccessPolicy": [
                    {
                        "TargetCidr": "abc",
                        "VpnGatewayIdSslAccessPolicyId": "abc",
                        "ForAllClient": 1,
                        "UserGroupIds": [
                            "abc"
                        ],
                        "UpdateTime": "abc",
                        "Remark": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

