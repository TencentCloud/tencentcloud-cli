**Example 1: 修改私网NAT网关属性**

修改私网NAT网关属性

Input: 

```
tccli vpc ModifyPrivateNatGatewayAttribute --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --NatGatewayName new_name
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

