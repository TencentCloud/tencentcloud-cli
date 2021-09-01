**Example 1: 修改专线网关属性**



Input: 

```
tccli vpc ModifyDirectConnectGatewayAttribute --cli-unfold-argument  \
    --DirectConnectGatewayId dcg-k6cswwhx \
    --DirectConnectGatewayName new+name \
    --CcnRouteType BGP
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

