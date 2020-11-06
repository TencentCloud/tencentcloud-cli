**Example 1: Deleting a port forwarding rule of the NAT**

To delete a port forwarding rule of the NAT, you only need to pass the IpProtocol, PublicIpAddress, and PublicPort fields in the DestinationIpPortTranslationNatRule structure.

Input: 

```
tccli vpc DeleteNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --DestinationIpPortTranslationNatRules.0.IpProtocol TCP \
    --DestinationIpPortTranslationNatRules.0.PublicIpAddress 139.199.232.238 \
    --DestinationIpPortTranslationNatRules.0.PublicPort 8989
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

