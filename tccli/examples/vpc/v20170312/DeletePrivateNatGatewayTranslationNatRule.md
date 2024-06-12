**Example 1: 删除私网NAT网关源端转换规则**



Input: 

```
tccli vpc DeletePrivateNatGatewayTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationNatRules.0.TranslationDirection PEER \
    --TranslationNatRules.0.TranslationType NETWORK_LAYER \
    --TranslationNatRules.0.OriginalIp 10.0.0.34 \
    --TranslationNatRules.0.TranslationIp 10.0.0.56 \
    --TranslationNatRules.0.Description desc
```

Output: 
```
{
    "Response": {
        "NatGatewayId": "intranat-0g3blj80",
        "RequestId": "e6da1f54-293d-4fda-a2e2-6f4c6f2bd97e"
    }
}
```

