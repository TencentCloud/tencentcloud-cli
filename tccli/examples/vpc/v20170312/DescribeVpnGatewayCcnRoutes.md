**Example 1: Querying VPN gateway-based CCN routes**



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
                "DestinationCidrBlock": "10.33.0.0/24",
                "Status": "ENABLE"
            },
            {
                "RouteId": "xxx-xxxxxx",
                "DestinationCidrBlock": "192.168.0.0/24",
                "Status": "ENABLE"
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

