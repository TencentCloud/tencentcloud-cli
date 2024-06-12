**Example 1: 修改私网NAT网关目的端口转换规则**

修改私网NAT网关目的端口转换规则

Input: 

```
tccli vpc ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --LocalDestinationIpPortTranslationNatRules.0.OldProtocol TCP \
    --LocalDestinationIpPortTranslationNatRules.0.OldTranslationPort 5666 \
    --LocalDestinationIpPortTranslationNatRules.0.OldTranslationIp 10.0.0.34 \
    --LocalDestinationIpPortTranslationNatRules.0.OldOriginalPort 8888 \
    --LocalDestinationIpPortTranslationNatRules.0.OldOriginalIp 10.0.0.88 \
    --LocalDestinationIpPortTranslationNatRules.0.Protocol TCP \
    --LocalDestinationIpPortTranslationNatRules.0.TranslationPort 5666 \
    --LocalDestinationIpPortTranslationNatRules.0.TranslationIp 10.0.0.34 \
    --LocalDestinationIpPortTranslationNatRules.0.OriginalPort 8888 \
    --LocalDestinationIpPortTranslationNatRules.0.OriginalIp 10.0.0.88 \
    --LocalDestinationIpPortTranslationNatRules.0.Description chdesc
```

Output: 
```
{
    "Response": {
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

