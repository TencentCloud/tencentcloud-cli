**Example 1: 创建NAT网关的SNAT规则**



Input: 

```
tccli vpc CreateNatGatewaySourceIpTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --SourceIpTranslationNatRules.0.ResourceId cvm-24796297 \
    --SourceIpTranslationNatRules.0.ResourceType NETWORKINTERFACE \
    --SourceIpTranslationNatRules.0.PrivateIpAddress 10.80.80.41 \
    --SourceIpTranslationNatRules.0.PublicIpAddresses 180.12.59.43 \
    --SourceIpTranslationNatRules.0.Description test_snat
```

Output: 
```
{
    "Response": {
        "RequestId": "14f7ea4e-8452-4742-84b5-5a4aee304968"
    }
}
```

