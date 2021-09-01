**Example 1: 修改NAT的SNAT转发规则**

修改NAT的SNAT转发规则时，SourceIpTranslationNatRule只需要传递NatGatewaySnatId，PublicIpAddresses，Description。

Input: 

```
tccli vpc ModifyNatGatewaySourceIpTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --SourceIpTranslationNatRule.NatGatewaySnatId snat-4cnwed83 \
    --SourceIpTranslationNatRule.ResourceId cvm-24796297 \
    --SourceIpTranslationNatRule.ResourceType NETWORKINTERFACE \
    --SourceIpTranslationNatRule.PrivateIpAddress 10.80.80.41 \
    --SourceIpTranslationNatRule.PublicIpAddresses 180.12.59.43 \
    --SourceIpTranslationNatRule.Description test_snat
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

