**Example 1: 修改私网NAT网关源端转换访问控制规则**

修改私网NAT网关源端转换访问控制规则

Input: 

```
tccli vpc ModifyPrivateNatGatewayTranslationAclRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationDirection LOCAL \
    --TranslationType TRANSPORT_LAYER \
    --TranslationIp 10.0.0.156-10.0.0.200 \
    --TranslationAclRules.0.AclRuleId 26 \
    --TranslationAclRules.0.Protocol TCP \
    --TranslationAclRules.0.SourcePort 5666 \
    --TranslationAclRules.0.SourceCidr 10.0.0.34 \
    --TranslationAclRules.0.DestinationPort 8888 \
    --TranslationAclRules.0.DestinationCidr 10.0.0.24
```

Output: 
```
{
    "Response": {
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

