**Example 1: 创建私网NAT网关源端转换规则**

创建私网NAT网关源端转换规则

Input: 

```
tccli vpc CreatePrivateNatGatewayTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationNatRules.0.TranslationDirection PEER \
    --TranslationNatRules.0.TranslationType NETWORK_LAYER \
    --TranslationNatRules.0.OriginalIp 10.0.0.86 \
    --TranslationNatRules.0.TranslationIp 10.0.0.222 \
    --TranslationNatRules.0.Description desc \
    --TranslationNatRules.1.TranslationDirection PEER \
    --TranslationNatRules.1.TranslationType NETWORK_LAYER \
    --TranslationNatRules.1.OriginalIp 10.0.0.34 \
    --TranslationNatRules.1.TranslationIp 10.0.0.56 \
    --TranslationNatRules.1.Description desc \
    --TranslationNatRules.2.TranslationDirection LOCAL \
    --TranslationNatRules.2.TranslationType NETWORK_LAYER \
    --TranslationNatRules.2.OriginalIp 10.0.0.90 \
    --TranslationNatRules.2.TranslationIp 10.0.0.123 \
    --TranslationNatRules.2.Description desc \
    --TranslationNatRules.3.TranslationDirection LOCAL \
    --TranslationNatRules.3.TranslationType TRANSPORT_LAYER \
    --TranslationNatRules.3.TranslationIp 10.0.0.156-10.0.0.200 \
    --TranslationNatRules.3.Description desc
```

Output: 
```
{
    "Response": {
        "NatGatewayId": "intranat-0g3blj80",
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

