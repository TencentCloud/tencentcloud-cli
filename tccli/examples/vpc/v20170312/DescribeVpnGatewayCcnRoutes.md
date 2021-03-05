**Example 1: 查询VPN网关云联网路由**



Input: 

```
tccli vpc DescribeVpnGatewayCcnRoutes --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-12345678
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": "xxx-xxxxxx",
                "Status": "ENABLE"
            },
            {
                "RouteId": "xxx-xxxxxx",
                "Status": "ENABLE"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

