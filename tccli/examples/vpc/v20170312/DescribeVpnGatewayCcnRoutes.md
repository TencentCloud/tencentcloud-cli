**Example 1: 查询VPN网关云联网路由**

查询VPN网关云联网路由

Input: 

```
tccli vpc DescribeVpnGatewayCcnRoutes --cli-unfold-argument  \
    --VpnGatewayId vpngw-qol17bjx \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": "vpnr-00wv1z75",
                "DestinationCidrBlock": "10.33.0.0/24",
                "Status": "ENABLE"
            },
            {
                "RouteId": "vpnr-11xe2z54",
                "DestinationCidrBlock": "192.168.0.0/24",
                "Status": "ENABLE"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

