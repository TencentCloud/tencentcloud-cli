**Example 1: Binding an EIP to the NAT gateway**



Input: 

```
tccli vpc AssociateNatGatewayAddress --cli-unfold-argument  \
    --NatGatewayId nat-mdbjfr0y\
    --PublicIpAddresses 139.199.232.212
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

