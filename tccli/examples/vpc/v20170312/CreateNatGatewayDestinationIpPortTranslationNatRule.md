**Example 1: 创建NAT的转发规则**



Input: 

```
tccli vpc CreateNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --DestinationIpPortTranslationNatRules.0.IpProtocol TCP \
    --DestinationIpPortTranslationNatRules.0.PublicIpAddress 139.199.232.238 \
    --DestinationIpPortTranslationNatRules.0.PublicPort 8989 \
    --DestinationIpPortTranslationNatRules.0.PrivateIpAddress 10.80.80.41 \
    --DestinationIpPortTranslationNatRules.0.PrivatePort 8989 \
    --DestinationIpPortTranslationNatRules.0.Description test_dnapt
```

Output: 
```
{
    "Response": {
        "RequestId": "14f7ea4e-8452-4742-84b5-5a3aee304967"
    }
}
```

