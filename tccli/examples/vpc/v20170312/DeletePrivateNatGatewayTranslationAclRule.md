**Example 1: 删除私网NAT网关源端转换访问控制规则**

删除私网NAT网关源端转换访问控制规则

Input: 

```
tccli vpc DeletePrivateNatGatewayTranslationAclRule --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationDirection LOCAL \
    --TranslationType NETWORK_LAYER \
    --TranslationIp 10.0.0.24 \
    --OriginalIp 10.0.0.14 \
    --AclRuleIds 26
```

Output: 
```
{
    "Response": {
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

