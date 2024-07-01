**Example 1: 修改私网NAT网关源端转换规则**

修改私网NAT网关源端转换规则

Input: 

```
tccli vpc ModifyPrivateNatGatewayTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationNatRules.0.TranslationDirection LOCAL \
    --TranslationNatRules.0.TranslationType NETWORK_LAYER \
    --TranslationNatRules.0.OriginalIp 10.0.0.14 \
    --TranslationNatRules.0.OldOriginalIp 10.0.0.90 \
    --TranslationNatRules.0.TranslationIp 10.0.0.24 \
    --TranslationNatRules.0.OldTranslationIp 10.0.0.123 \
    --TranslationNatRules.0.Description desc
```

Output: 
```
{
    "Response": {
        "RequestId": "41fe53eb-6f90-4fde-9e37-c48fa4f8f2ed"
    }
}
```

