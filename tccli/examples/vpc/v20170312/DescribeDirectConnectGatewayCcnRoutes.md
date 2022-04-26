**Example 1: 查询专线网关云联网路由**



Input: 

```
tccli vpc DescribeDirectConnectGatewayCcnRoutes --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-prpqlmg1
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": "ccnr-bvipc87w",
                "DestinationCidrBlock": "10.33.0.0/24",
                "UpdateTime": "xx",
                "Description": "xx",
                "ASPath": [
                    "1000",
                    "2000",
                    "3000"
                ]
            },
            {
                "RouteId": "ccnr-oc61so0o",
                "DestinationCidrBlock": "192.168.0.0/24",
                "UpdateTime": "xx",
                "Description": "xx",
                "ASPath": []
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

