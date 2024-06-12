**Example 1: 删除私网NAT网关目的端口转换规则**

删除私网NAT网关目的端口转换规则

Input: 

```
tccli vpc DeletePrivateNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --LocalDestinationIpPortTranslationNatRules.0.Protocol TCP \
    --LocalDestinationIpPortTranslationNatRules.0.TranslationPort 5666 \
    --LocalDestinationIpPortTranslationNatRules.0.TranslationIp 10.0.0.14 \
    --LocalDestinationIpPortTranslationNatRules.0.OriginalPort 8888 \
    --LocalDestinationIpPortTranslationNatRules.0.OriginalIp 10.0.0.26 \
    --LocalDestinationIpPortTranslationNatRules.0.Description desc
```

Output: 
```
{
    "Response": {
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

