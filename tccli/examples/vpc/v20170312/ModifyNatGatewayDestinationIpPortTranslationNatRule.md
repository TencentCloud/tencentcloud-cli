**Example 1: Modifying the port forwarding rules of a NAT**

When modifying the forwarding rule of a NAT, SourceNatRule only needs to pass IpProtocol, PublicIpAddress, and PublicPort. All DestinationNatRule parameters can be modified.

Input: 

```
tccli vpc ModifyNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --SourceNatRule.IpProtocol TCP \
    --SourceNatRule.PublicIpAddress 139.199.232.238 \
    --SourceNatRule.PublicPort 8989 \
    --DestinationNatRule.IpProtocol UDP \
    --DestinationNatRule.PublicIpAddress 139.199.232.226 \
    --DestinationNatRule.PublicPort 8586 \
    --DestinationNatRule.PrivateIpAddress 10.80.80.41 \
    --DestinationNatRule.PrivatePort 8586 \
    --DestinationNatRule.Description test_modify
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

