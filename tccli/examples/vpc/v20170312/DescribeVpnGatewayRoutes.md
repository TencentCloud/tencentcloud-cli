**Example 1: 查询VPN网关目的路由**



Input: 

```
tccli vpc DescribeVpnGatewayRoutes --cli-unfold-argument  \
    --VpnGatewayId vpn-ngenl4az \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name DestinationCidr \
    --Filters.0.Values 192.241.0.0/24
```

Output: 
```
{
    "Response": {
        "Routes": [
            {
                "DestinationCidrBlock": "192.241.0.0/24",
                "Status": "ENABLE",
                "InstanceId": "vpnx-ng2asdew",
                "InstanceType": "VPNCONN",
                "Priority": 100
            }
        ],
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

