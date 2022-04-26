**Example 1: 修改NAT的端口转发规则**

修改NAT的端口转发规则时，SourceNatRule只需要传递IpProtocol，PublicIpAddress，PublicPort，对于DestinationNatRule参数都可以进行修改的。

Input: 

```
tccli vpc ModifyNatGatewayDestinationIpPortTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --SourceNatRule.IpProtocol TCP \
    --SourceNatRule.PublicIpAddress 139.199.232.238 \
    --SourceNatRule.PublicPort 8989 \
    --SourceNatRule.Description xx \
    --SourceNatRule.PrivateIpAddress 10.0.8.9 \
    --SourceNatRule.PrivatePort 9090 \
    --DestinationNatRule.IpProtocol UDP \
    --DestinationNatRule.PublicIpAddress 139.199.232.226 \
    --DestinationNatRule.PublicPort 8586 \
    --DestinationNatRule.PrivateIpAddress 10.80.80.41 \
    --DestinationNatRule.PrivatePort 8586 \
    --DestinationNatRule.Description test_modify
```

Output: 
```
{
    "Response": {
        "RequestId": "dbffc3f0-1807-4683-89ee-2d2b96425ee1"
    }
}
```

