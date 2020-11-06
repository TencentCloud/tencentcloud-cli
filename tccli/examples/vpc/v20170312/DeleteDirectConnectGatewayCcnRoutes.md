**Example 1: Deleting CCN routes of a Direct Connect gateway**



Input: 

```
tccli vpc DeleteDirectConnectGatewayCcnRoutes --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-prpqlmg1 \
    --RouteIds ccnr-bvipc87w ccnr-oc61so0o
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

