**Example 1: 专线网关解绑NAT网关**

解绑专线网关与公网NAT网关

Input: 

```
tccli vpc DisassociateDirectConnectGatewayNatGateway --cli-unfold-argument  \
    --VpcId "vpc-8xpno8ee" \
    --DirectConnectGatewayId "dcg-fxa6gh5t" \
    --NatGatewayId "nat-ig8xpno8"
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

