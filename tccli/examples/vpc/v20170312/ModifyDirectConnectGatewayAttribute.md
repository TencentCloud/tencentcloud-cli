**Example 1: Modifying the attributes of a direct connect gateway**



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

