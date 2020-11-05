**Example 1: Querying the CCN routes of a Direct Connect gateway**



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
                "ASPath": [
                    "1000",
                    "2000",
                    "3000"
                ]
            },
            {
                "RouteId": "ccnr-oc61so0o",
                "DestinationCidrBlock": "192.168.0.0/24",
                "ASPath": []
            }
        ],
        "TotalCount": 2,
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

