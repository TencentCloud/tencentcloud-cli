**Example 1: 删除专线网关云联网路由**



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

