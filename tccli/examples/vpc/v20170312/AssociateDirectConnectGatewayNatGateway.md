**Example 1: 专线网关绑定NAT网关**

绑定专线网关与公网NAT网关实例

Input: 

```
tccli vpc AssociateDirectConnectGatewayNatGateway --cli-unfold-argument  \
    --VpcId vpc-8xpno8ee \
    --DirectConnectGatewayId dcg-fxa6gh5t \
    --NatGatewayId nat-ig8xpno8
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

