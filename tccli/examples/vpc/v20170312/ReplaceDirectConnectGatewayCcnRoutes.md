**Example 1: 替换专线网关云联网路由**



Input: 

```
tccli vpc ReplaceDirectConnectGatewayCcnRoutes --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-prpqlmg1 \
    --Routes.0.RouteId dcr-bvipc87w \
    --Routes.0.DestinationCidrBlock 10.2.2.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

