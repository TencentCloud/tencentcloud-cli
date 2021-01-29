**Example 1: 删除NAT网关的SNAT转发规则**



Input: 

```
tccli vpc DeleteNatGatewaySourceIpTranslationNatRule --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --NatGatewaySnatIds snat-3ixd0hr0
```

Output: 
```
{
    "Response": {
        "RequestId": "14f7ea4e-8452-4742-84b5-5a4aee304968"
    }
}
```

