**Example 1: 创建专线网关云联网路由**



Input: 

```
tccli vpc CreateDirectConnectGatewayCcnRoutes --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-prpqlmg1 \
    --Routes.0.DestinationCidrBlock 10.2.2.0/24 \
    --Routes.1.DestinationCidrBlock 10.2.3.0/24
```

Output: 
```
{
    "Response": {
        "RequestId": "6e446c86-d8c9-4981-9b33-d10956585058"
    }
}
```

