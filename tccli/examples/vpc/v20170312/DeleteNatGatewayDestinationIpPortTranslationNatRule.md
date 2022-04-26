**Example 1: 删除NAT的端口转发规则**

删除NAT的端口转发规则，只需要传递DestinationIpPortTranslationNatRule结构体中的IpProtocol，PublicIpAddress，PublicPort字段。

Input: 

```
tccli vpc DeleteNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --DestinationIpPortTranslationNatRules.0.Description xx \
    --DestinationIpPortTranslationNatRules.0.PublicIpAddress 139.199.232.238 \
    --DestinationIpPortTranslationNatRules.0.PrivatePort 9999 \
    --DestinationIpPortTranslationNatRules.0.IpProtocol TCP \
    --DestinationIpPortTranslationNatRules.0.PublicPort 999 \
    --DestinationIpPortTranslationNatRules.0.PrivateIpAddress 10.0.9.2
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

